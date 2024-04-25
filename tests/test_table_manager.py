import unittest
from unittest.mock import Mock, patch
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from src.components.table_manager import TableManager
from database import DatabaseManager

class TestTableManager(unittest.TestCase):

    def setUp(self):
        self.db_manager = Mock(spec=DatabaseManager)
        self.table_widget = Mock(spec=QTableWidget)
        self.table_widget.rowCount.return_value = 0
        self.table_manager = TableManager(self.table_widget, self.db_manager)

    def test_setup_table_with_headers(self):
        headers = ['ID', 'Name', 'Country']
        self.table_manager.setup_table(headers)
        self.table_widget.setColumnCount.assert_called_once_with(len(headers))
        self.table_widget.setHorizontalHeaderLabels.assert_called_once_with(headers)

    def test_load_data_from_database(self):
        data = [(1, 'Test', 'USA')]
        self.db_manager.fetch_all.return_value = data
        self.table_manager.load_data()
        self.table_widget.setRowCount.assert_called_once_with(0)
        self.table_widget.insertRow.assert_called_once_with(0)
        self.table_widget.setItem.assert_called_once()

    def test_add_row_to_table(self):
        data_row = (1, 'Test', 'USA')
        self.table_manager.add_row(data_row)
        self.table_widget.insertRow.assert_called_once_with(self.table_widget.rowCount.return_value)
    def test_delete_row_from_table_and_database(self):
        self.table_manager.delete_row(0)
        self.table_widget.item.assert_called_once_with(0, 0)
        self.db_manager.delete_entry.assert_called_once()
        self.table_widget.removeRow.assert_called_once_with(0)

    def test_update_all_rows_in_database(self):
        self.table_manager.update_all_rows()
        self.table_widget.item.assert_called()
        self.db_manager.update_entry.assert_called()

    def test_update_all_rows_in_database_with_error(self):
        self.db_manager.update_entry.side_effect = ValueError('Test error')
        with self.assertRaises(ValueError):
            self.table_manager.update_all_rows()

if __name__ == '__main__':
    unittest.main()