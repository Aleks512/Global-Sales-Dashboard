import unittest
from unittest.mock import MagicMock

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QLineEdit, QDateEdit, QApplication
from src.components.form_manager import FormManager

app = QApplication([])
class TestFormManager(unittest.TestCase):
    def setUp(self):
        self.ui_elements = MagicMock()
        self.form_manager = FormManager(self.ui_elements)

    def test_collect_data_with_valid_inputs(self):
        self.ui_elements.fil_name_le = QLineEdit("Test Filiale")
        self.ui_elements.country_le = QLineEdit("Test Country")
        self.ui_elements.dateEdit = QDateEdit(QDate(2023, 1, 1))
        self.ui_elements.revenue_le = QLineEdit("1000.0")
        self.ui_elements.costs_le = QLineEdit("500.0")
        self.ui_elements.vol_le = QLineEdit("100")
        self.ui_elements.new_client_nr_le = QLineEdit("10")
        self.ui_elements.satisfaction_le = QLineEdit("90")
        self.ui_elements.depense_pub_le = QLineEdit("200.0")

        expected_data = {
            "filiale_name": "Test Filiale",
            "country": "Test Country",
            "date": "2023-01-01",
            "monthly_revenue": 1000.0,
            "monthly_costs": 500.0,
            "sales_volume": 100,
            "new_clients": 10,
            "satisfaction_rate": 90,
            "advertising_costs": 200.0
        }

        self.assertEqual(self.form_manager.collect_data(), expected_data)

    def test_collect_data_with_invalid_inputs(self):
        self.ui_elements.fil_name_le = QLineEdit("")
        self.ui_elements.country_le = QLineEdit("")
        self.ui_elements.dateEdit = QDateEdit(QDate(2023, 1, 1))
        self.ui_elements.revenue_le = QLineEdit("abc")
        self.ui_elements.costs_le = QLineEdit("500.0")
        self.ui_elements.vol_le = QLineEdit("100")
        self.ui_elements.new_client_nr_le = QLineEdit("10")
        self.ui_elements.satisfaction_le = QLineEdit("90")
        self.ui_elements.depense_pub_le = QLineEdit("200.0")

        self.assertIsNone(self.form_manager.collect_data())

    def test_validate_data_with_valid_inputs(self):
        data = {
            "filiale_name": "Test Filiale",
            "country": "Test Country",
            "date": "2023-01-01",
            "monthly_revenue": 1000.0,
            "monthly_costs": 500.0,
            "sales_volume": 100,
            "new_clients": 10,
            "satisfaction_rate": 90,
            "advertising_costs": 200.0
        }

        self.assertTrue(self.form_manager.validate_data(data))

    def test_validate_data_with_invalid_inputs(self):
        data = {
            "filiale_name": "",
            "country": "",
            "date": "2023-01-01",
            "monthly_revenue": -1000.0,
            "monthly_costs": 500.0,
            "sales_volume": 100,
            "new_clients": 10,
            "satisfaction_rate": 110,
            "advertising_costs": 200.0
        }

        self.assertFalse(self.form_manager.validate_data(data))

if __name__ == '__main__':
    unittest.main()