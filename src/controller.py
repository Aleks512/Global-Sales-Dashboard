import locale
from PySide6.QtWidgets import QMainWindow, QMessageBox, QGraphicsScene
from matplotlib import pyplot as plt

from ui.ui_main import Ui_MainWindow
from components.form_manager import FormManager
from components.table_manager import TableManager
from database import DatabaseManager
from components.kpi_window import KPIManager
import pandas as pd
from PySide6.QtGui import QImage, QIcon
from matplotlib.backends.backend_agg import FigureCanvasAgg


# Set the locale to support thousands' separator
locale.setlocale(locale.LC_ALL, '')


class MainWindowController(QMainWindow):
    """
    Main window controller managing UI interactions and coordinating with the form and table managers.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sales Data Management")
        self.setWindowIcon(QIcon('./assets/sleek_icon.webp'))


        # Initialize database and managers
        self.db_manager = DatabaseManager()
        self.form_manager = FormManager(self.ui)
        self.table_manager = TableManager(self.ui.data_tb_wgt, self.db_manager)
        self.kpi_manager = KPIManager(self.db_manager)  # Assuming db_manager is initialized

        # Setup table with headers
        headers = ['ID', 'Filiale Name', 'Country', 'Date', 'Revenue €', 'Costs €', 'Volume', 'Clients',
                   'Satisfaction %', 'Ad Costs']
        self.table_manager.setup_table(headers)
        self.table_manager.load_data()

        # Connect UI signals to slots
        self.ui.add_btn.clicked.connect(self.add_data)
        self.ui.save_btn.clicked.connect(self.table_manager.update_all_rows)
        self.ui.delete_btn.clicked.connect(self.delete_selected_data)
        self.ui.gen_repport_btn.clicked.connect(self.update_display)
        self.ui.kpi_btn.clicked.connect(self.kpi_manager.show)
        self.ui.image_upload_btn.clicked.connect(self.update_graphics_views)
        # Initialize display with data
        self.update_display()
    def show_kpi(self):
        """
        Displays the KPI Manager widget.
        """
        self.kpi_manager.show()  # Affiche le widget de KPI

    def update_display(self):
        """
        Fetches current data and updates the UI display with formatted numbers.
        """
        df = pd.read_sql_query("SELECT * FROM sales_data", self.db_manager.connection)
        if not df.empty:
            total_revenue = df['monthly_revenue'].sum()
            total_costs = df['monthly_costs'].sum()
            net_income = total_revenue - total_costs - df['advertising_costs'].sum()

            # Format the values with thousands separator and two decimal points
            self.ui.revenue_lb_2.setText(locale.format_string("%0.2f €", total_revenue, grouping=True))
            self.ui.costs_lb_2.setText(locale.format_string("%0.2f €", total_costs, grouping=True))
            self.ui.income_lb.setText(locale.format_string("%0.2f €", net_income, grouping=True))
        else:
            self.ui.revenue_lb_2.setText("No Data")
            self.ui.costs_lb_2.setText("No Data")
            self.ui.income_lb.setText("No Data")

    def add_data(self):
        """
        Collects data from the form, validates it, and adds a new entry to the database.
        """
        data = self.form_manager.collect_data()
        if data and self.form_manager.validate_data(data):
            self.db_manager.add_entry(**data)
            self.table_manager.load_data()
            self.form_manager.reset_inputs()


    def delete_selected_data(self):
        """
        Asks for confirmation before deleting the selected row in the table.
        """
        row_index = self.ui.data_tb_wgt.currentRow()
        if row_index != -1:
            reply = QMessageBox.question(self, 'Confirm Delete', 'Are you sure you want to delete this row?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.table_manager.delete_row(row_index)
                QMessageBox.information(self, "Deletion", "The row has been successfully deleted.")
            else:
                QMessageBox.information(self, "Cancellation", "Deletion cancelled.")

    def update_graphics_views(self):
        revenue_pixmap = self.kpi_manager.create_revenue_graph()
        if revenue_pixmap:
            scene = QGraphicsScene()
            scene.addPixmap(revenue_pixmap)
            self.ui.graphicsView.setScene(scene)

        costs_pixmap = self.kpi_manager.create_costs_graph()
        if costs_pixmap:
            scene2 = QGraphicsScene()
            scene2.addPixmap(costs_pixmap)
            self.ui.graphicsView_2.setScene(scene2)
        else:
            print("Failed to create costs graph.")


    def closeEvent(self, event):
        """
        Ensures database connections are closed when the application is closed.
        """
        self.db_manager.close()
        super().closeEvent(event)
