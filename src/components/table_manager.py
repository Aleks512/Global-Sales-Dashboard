from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from database import DatabaseManager

class TableManager:
    """
    Manages the QTableWidget for displaying and interacting with data rows.
    Responsible for setting up the table, loading data from the database,
    and handling CRUD operations directly from the table view.
    """
    def __init__(self, table_widget: QTableWidget, db_manager: DatabaseManager):
        self.table_widget = table_widget
        self.db_manager = db_manager

    def setup_table(self, headers):
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.setAlternatingRowColors(True)

    def load_data(self):
        data = self.db_manager.fetch_all()
        self.table_widget.setRowCount(0) # clear the data before loading new data
        for data_row in data:
            self.add_row(data_row)

    def add_row(self, data_row):
        row_index = self.table_widget.rowCount()
        self.table_widget.insertRow(row_index)
        for column_index, value in enumerate(data_row):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_index, column_index, item)

    def delete_row(self, row_index):
        if row_index < self.table_widget.rowCount():
            id = int(self.table_widget.item(row_index, 0).text())
            self.db_manager.delete_entry(id)
            self.table_widget.removeRow(row_index)
            QMessageBox.information(None, "Success", "The row has been successfully deleted.")

    def header_to_db_column(self, header_text):
        # Normalize header text to database column names
        mapping = {
            'ID': 'id',
            'Filiale Name': 'filiale_name',
            'Country': 'country',
            'Date': 'date',
            'Revenue €': 'monthly_revenue',
            'Costs €': 'monthly_costs',
            'Volume': 'sales_volume',
            'Clients': 'new_clients',
            'Satisfaction %': 'satisfaction_rate',
            'Ad Costs': 'advertising_costs'
        }
        return mapping.get(header_text)

    def update_all_rows(self):
        errors = False
        for row in range(self.table_widget.rowCount()):
            if not self.update_row(row):
                self.table_widget.selectRow(row)  # Focus on the problematic row
                QMessageBox.warning(None, "Update Issue",
                                    "An issue occurred during update. Check the row with incorrect inputs.")
                errors = True
                break  # Stop at the first error

        if not errors:
            QMessageBox.information(None, "Success", "All data have been successfully updated.")

    def update_row(self, row):
        id = int(self.table_widget.item(row, 0).text())
        original_data = {
            self.header_to_db_column(self.table_widget.horizontalHeaderItem(col).text()): self.table_widget.item(row,
                                                                                                                 col).text()
            for col in range(1, self.table_widget.columnCount())}
        updated_data = {}
        errors = False

        try:
            for col in range(1, self.table_widget.columnCount()):
                header_text = self.table_widget.horizontalHeaderItem(col).text()
                db_column_name = self.header_to_db_column(header_text)
                cell_value = self.table_widget.item(row, col).text()

                if db_column_name in ['filiale_name', 'country']:
                    if not self.is_string(cell_value):
                        raise ValueError(f"Expected a text value for '{header_text}'")
                elif db_column_name in ['monthly_revenue', 'monthly_costs', 'advertising_costs']:
                    if not self.is_float(cell_value):
                        raise ValueError(f"Expected a numeric value for '{header_text}'")
                elif db_column_name in ['sales_volume', 'new_clients', 'satisfaction_rate']:
                    if not self.is_int(cell_value):
                        raise ValueError(f"Expected an integer value for '{header_text}'")

                updated_data[db_column_name] = cell_value

            if not errors:
                self.db_manager.update_entry(id, **updated_data)
        except Exception as e:
            QMessageBox.warning(None, "Update Error", f"An error occurred: {str(e)}. Reverting changes.")
            self.db_manager.update_entry(id, **original_data)  # Rollback to original data
            return False

        return True

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def is_string(self, value):
        # Check if the input is a string and it's not empty after stripping whitespace
        if isinstance(value, str) and value.strip():
            # Further check to reject strings that are actually numbers or contain unwanted characters
            if value.replace(' ', '').isalpha():  # This checks if the string is all alphabetic
                return True
            else:
                QMessageBox.warning(None, "Input Error", "Please enter a valid text string without numbers.")
                return False
        else:
            QMessageBox.warning(None, "Input Error", "Please enter a valid text string.")
            return False
