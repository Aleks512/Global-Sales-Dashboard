from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
import pandas as pd
from ui.kpi_ui import Ui_kpi_window
from database import DatabaseManager

class KPIManager(QMainWindow, Ui_kpi_window):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager  # Use the database manager singleton
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate_pdf)

    def setupUi(self, kpi_window):
        super().setupUi(kpi_window)
        self.layout = QVBoxLayout(self.centralwidget)  # Create a QVBoxLayout

        # Create labels and tables for displaying KPIs
        self.revenue_label = QLabel("Total Revenue:")
        self.costs_label = QLabel("Total Costs:")
        self.income_label = QLabel("Net Income:")
        self.country_date_income_table = QTableWidget()
        self.date_country_income_table = QTableWidget()

        # Add widgets to the layout
        self.layout.addWidget(self.revenue_label)
        self.layout.addWidget(self.costs_label)
        self.layout.addWidget(self.income_label)
        self.layout.addWidget(self.country_date_income_table)
        self.layout.addWidget(self.date_country_income_table)

    def load_data(self):
        """ Fetches data from the database and returns it as a DataFrame. """
        query = "SELECT * FROM sales_data"
        df = pd.read_sql_query(query, self.db_manager.connection)
        return df

    def update_display(self):
        """ Updates the display with formatted data. """
        df = self.load_data()
        if not df.empty:
            self.update_kpi_labels(df)
            self.update_income_tables(df)
        else:
            self.clear_tables()

    def update_kpi_labels(self, df):
        total_revenue = df['monthly_revenue'].sum()
        total_costs = df['monthly_costs'].sum()
        net_income = total_revenue - total_costs - df['advertising_costs'].sum()

        self.revenue_label.setText(f"Total Revenue: {total_revenue:,.2f} €")
        self.costs_label.setText(f"Total Costs: {total_costs:,.2f} €")
        self.income_label.setText(f"Net Income: {net_income:,.2f} €")

    def update_income_tables(self, df):
        # Group and aggregate data for income by country and date
        income_by_country_date = df.groupby(['country', 'date']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')
        income_by_date_country = df.groupby(['date', 'country']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')

        self.setup_table(self.country_date_income_table, income_by_country_date)
        self.setup_table(self.date_country_income_table, income_by_date_country)

    def setup_table(self, table_widget, data_df):
        """ Sets up a QTableWidget with DataFrame data. """
        table_widget.setRowCount(data_df.shape[0])
        table_widget.setColumnCount(data_df.shape[1])
        table_widget.setHorizontalHeaderLabels(data_df.columns.tolist())

        for i in range(data_df.shape[0]):
            for j in range(data_df.shape[1]):
                item = QTableWidgetItem(str(data_df.iloc[i, j]))
                table_widget.setItem(i, j, item)

    def clear_tables(self):
        """ Clears all tables and labels when no data is available. """
        self.revenue_label.setText("No Data")
        self.costs_label.setText("No Data")
        self.income_label.setText("No Data")
        self.country_date_income_table.setRowCount(0)
        self.date_country_income_table.setRowCount(0)

    def generate_pdf(self):
        """ Logic to generate and save a PDF report based on the current data displayed. """
        pass

    def show(self):
        """ Show the widget and update display. """
        self.update_display()
        super().show()  # Ensure the updated display is shown
