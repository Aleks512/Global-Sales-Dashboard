from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from database import DatabaseManager

class TableManager:
    """
    Manages the QTableWidget for displaying and interacting with data rows.
    Responsible for setting up the table, loading data from the database,
    and handling CRUD operations directly from the table view.
    """
    def __init__(self, table_widget: QTableWidget, db_manager: DatabaseManager):
        """
        Initializes the TableManager with the table widget and a reference to the database manager.
        Args:
            table_widget (QTableWidget): The table widget this manager will handle.
            db_manager (DatabaseManager): The database manager for executing database operations.
        """
        self.table_widget = table_widget
        self.db_manager = db_manager

    def setup_table(self, headers):
        """
        Sets up the table with specified headers and default properties.
        Args:
            headers (List[str]): A list of header titles for the columns.
        """
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.setAlternatingRowColors(True)

    def load_data(self):
        """
        Loads data from the database and populates the table.
        """
        data = self.db_manager.fetch_all()
        self.table_widget.setRowCount(0)
        for data_row in data:
            self.add_row(data_row)

    def add_row(self, data_row):
        """
        Adds a single row to the table.
        Args:
            data_row (tuple): Data tuple containing fields for a single row.
        """
        row_index = self.table_widget.rowCount()
        self.table_widget.insertRow(row_index)
        for column_index, value in enumerate(data_row):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_index, column_index, item)

    def delete_row(self, row_index):
        """
        Deletes a row from the table and the database.
        Args:
            row_index (int): The index of the row to delete.
        """
        if row_index < self.table_widget.rowCount():
            id = int(self.table_widget.item(row_index, 0).text())
            self.db_manager.delete_entry(id)
            self.table_widget.removeRow(row_index)

    def update_all_rows(self):
        """
        Updates all modified rows in the database based on the current data in the table.
        """
        errors = False
        for row in range(self.table_widget.rowCount()):
            if not self.update_row(row):
                errors = True
                break
        if not errors:
            QMessageBox.information(None, "Success", "All data have been successfully updated.")

    def update_row(self, row):
        """
        Updates a single row in the database.
        """
        id = int(self.table_widget.item(row, 0).text())
        updated_data = {}
        for col in range(1, self.table_widget.columnCount()):
            header_text = self.table_widget.horizontalHeaderItem(col).text()
            cell_value = self.table_widget.item(row, col).text()
            updated_data[header_text.lower().replace(' ', '_')] = cell_value

        try:
            self.db_manager.update_entry(id, **updated_data)
        except ValueError as e:
            QMessageBox.warning(None, "Erreur de saisie", f"Veuillez vérifier vos saisies. Erreur dans la ligne {row + 1}: {e}")
            return False
        return True
