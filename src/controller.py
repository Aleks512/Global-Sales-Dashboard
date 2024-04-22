from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow  # Make sure this is the correct class name
from database import DatabaseManager
from components.form_manager import FormManager
from components.table_manager import TableManager  # Assuming this is the correct import path


class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize database manager
        self.db_manager = DatabaseManager("../sales.db")

        # Initialize form manager
        self.form_manager = FormManager(self.ui)

        # Initialize table manager
        self.table_manager = TableManager(self.ui.data_tb_wgt)
        headers = ['ID','Filiale Name', 'Country', 'Date', 'Revenue €', 'Costs €', 'Volume', 'Clients', 'Satisfaction %',
                   'Ad Costs']
        self.table_manager.setup_table(headers)

        # Load data into table
        self.load_data_into_table()

        # Connect UI signals to slots
        self.ui.save_btn.clicked.connect(self.save_data)
        self.ui.update_btn.clicked.connect(self.update_data)
        self.ui.delete_btn.clicked.connect(self.delete_data)

        #self.ui.data_tb_wgt.cellClicked.connect(self.cell_was_clicked)

    def add_data(self):
        data = self.form_manager.collect_data()
        if data and self.form_manager.validate_data(data):
            self.db_manager.add_entry(**data)
            self.load_data_into_table()

    def load_data_into_table(self):
        data = self.db_manager.fetch_all()
        self.table_manager.load_data(data)


    #self.ui.data_tb_wgt.itemSelectionChanged.connect(self.selection_changed)

    # def update_data(self):
    #     row_index = self.ui.data_tb_wgt.currentRow()
    #     if row_index != -1:
    #         data = self.form_manager.collect_data()
    #         if data and self.form_manager.validate_data(data):
    #             id = int(self.ui.data_tb_wgt.item(row_index, 0).text())  # Assuming the ID is in the first column
    #             self.db_manager.update_entry(id, **data)
    #             self.load_data_into_table()

    def save_data(self):
        # Iterate over each row and save changes to the database
        for row in range(self.table_manager.table_widget.rowCount()):
            id = int(self.table_manager.table_widget.item(row, 0).text())  # Assuming the ID is in the first column
            updated_data = {
                'filiale_name': self.table_manager.table_widget.item(row, 1).text(),
                'country': self.table_manager.table_widget.item(row, 2).text(),
                'date': self.table_manager.table_widget.item(row, 3).text(),
                'monthly_revenue': float(self.table_manager.table_widget.item(row, 4).text()),
                'monthly_costs': float(self.table_manager.table_widget.item(row, 5).text()),
                'sales_volume': int(self.table_manager.table_widget.item(row, 6).text()),
                'new_clients': int(self.table_manager.table_widget.item(row, 7).text()),
                'satisfaction_rate': int(self.table_manager.table_widget.item(row, 8).text()),
                'advertising_costs': float(self.table_manager.table_widget.item(row, 9).text())
            }
            self.db_manager.update_entry(id, **updated_data)

    def update_data(self):
        row_index = self.table_manager.table_widget.currentRow()
        if row_index != -1:
            id = int(self.table_manager.table_widget.item(row_index, 0).text())
            updated_data = {
                'filiale_name': self.table_manager.table_widget.item(row_index, 1).text(),
                'country': self.table_manager.table_widget.item(row_index, 2).text(),
                'date': self.table_manager.table_widget.item(row_index, 3).text(),
                'monthly_revenue': float(self.table_manager.table_widget.item(row_index, 4).text()),
                'monthly_costs': float(self.table_manager.table_widget.item(row_index, 5).text()),
                'sales_volume': int(self.table_manager.table_widget.item(row_index, 6).text()),
                'new_clients': int(self.table_manager.table_widget.item(row_index, 7).text()),
                'satisfaction_rate': int(self.table_manager.table_widget.item(row_index, 8).text()),
                'advertising_costs': float(self.table_manager.table_widget.item(row_index, 9).text())
            }
            self.db_manager.update_entry(id, **updated_data)
    def delete_data(self):
        row_index = self.ui.data_tb_wgt.currentRow()
        if row_index != -1:
            id = int(self.ui.data_tb_wgt.item(row_index, 0).text())
            self.db_manager.delete_entry(id)
            self.table_manager.delete_row(row_index)  # Using TableManager to handle row deletion


    def closeEvent(self, event):
        self.db_manager.close()
        event.accept()
