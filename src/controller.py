from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow  # Assurez-vous que c'est le bon nom de classe
from database import DatabaseManager
from components.form_manager import FormManager

class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_manager = DatabaseManager("sales.db")
        self.form_manager = FormManager(self.ui)
        #self.db_manager.add_entry("Filiale 1", "France", "2021-01-01", 1000, 500, 10, 2, 80, 100)
        self.load_data_into_table()

        self.ui.data_tb_wgt.setAlternatingRowColors(True)  # Alternance des couleurs des lignes
        # self.ui.data_tb_wgt.setStyleSheet("QTableWidget {background-color: #f0f0f0; gridline-color: #cccccc;}")
        self.ui.data_tb_wgt.horizontalHeader().setStyleSheet("QHeaderView::section {background-color: #cccccc;}")
        column_width = 120  # Largeur souhaitée pour chaque colonne, ajustez selon vos besoins
        for i in range(3, 9):  # Les index des 6 dernières colonnes de 3 à 8
            self.ui.data_tb_wgt.setColumnWidth(i, column_width)
        # # Connecter les signaux et les slots
        self.ui.add_btn.clicked.connect(self.add_data)  # Assurez-vous qu'il y a un bouton submitButton

    def add_data(self):
        data = self.form_manager.collect_data()
        if data and self.form_manager.validate_data(data):
            self.db_manager.add_entry(**data)
            self.load_data_into_table()

        # Ajouter les données à la base de données
        # self.db_manager.add_entry(filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs)
        # self.load_data_into_table()

    def load_data_into_table(self):
        self.ui.data_tb_wgt.setRowCount(0)  # Effacer les lignes existantes
        for row_data in self.db_manager.fetch_all():
            row_number = self.ui.data_tb_wgt.rowCount()
            self.ui.data_tb_wgt.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.data_tb_wgt.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def closeEvent(self, event):
        event.accept()
