from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

class TableManager:
    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget

    def setup_table(self, headers):
        # Configure columns and headers
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.setAlternatingRowColors(True)

    def load_data(self, data):
        # Load data into the table
        self.table_widget.setRowCount(0)
        for data_row in data:
            self.add_row(data_row)

    def add_row(self, data_row):
        row_index = self.table_widget.rowCount()
        self.table_widget.insertRow(row_index)
        for column_index, value in enumerate(data_row):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row_index, column_index, item)

    def update_row(self, row_index, data_row):
        if row_index < self.table_widget.rowCount():
            for column_index, value in enumerate(data_row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_index, column_index, item)

    def delete_row(self, row_index):
        if row_index < self.table_widget.rowCount():
            self.table_widget.removeRow(row_index)
