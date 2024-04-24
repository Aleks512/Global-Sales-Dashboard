from PySide6.QtWidgets import QMainWindow
from ui.ui_main import Ui_MainWindow
from database import DatabaseManager
from components.form_manager import FormManager
from components.table_manager import TableManager
import os

class MainWindowController(QMainWindow):
    """
    Main window controller managing UI interactions and coordinating with the form and table managers.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize managers
        self.db_manager = DatabaseManager(os.path.join(os.path.dirname(__file__), "sales.db"))
        self.form_manager = FormManager(self.ui)
        self.table_manager = TableManager(self.ui.data_tb_wgt, self.db_manager)

        # Setup table
        headers = ['ID', 'Filiale Name', 'Country', 'Date', 'Revenue €', 'Costs €', 'Volume', 'Clients', 'Satisfaction %', 'Ad Costs']
        self.table_manager.setup_table(headers)
        self.table_manager.load_data()

        # Connect UI signals
        self.ui.add_btn.clicked.connect(self.add_data)
        self.ui.save_btn.clicked.connect(self.table_manager.update_all_rows)
        self.ui.delete_btn.clicked.connect(self.delete_data)

    def add_data(self):
        """
        Collects data from the form, validates it, and adds a new entry to the database.
        """
        data = self.form_manager.collect_data()
        if data:
            self.table_manager.db_manager.add_entry(**data)
            self.table_manager.load_data()

    def delete_data(self):
        """
        Deletes the selected row in the table.
        """
        row_index = self.ui.data_tb_wgt.currentRow()
        if row_index != -1:
            self.table_manager.delete_row(row_index)

    def closeEvent(self, event):
        """
        Ensures database connections are closed when the application is closed.
        """
        self.db_manager.close()
        super().closeEvent(event)
