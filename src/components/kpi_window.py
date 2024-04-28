import os
import pandas as pd
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem
from matplotlib import pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from ui.kpi_ui import Ui_kpi_window


class KPIManager(QMainWindow, Ui_kpi_window):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager  # Utilisation du singleton de la base de données
        self.setupUi(self)  # Initialisation de l'interface utilisateur depuis Ui_kpi_window
        self.pushButton.clicked.connect(self.generate_pdf)
        self.init_widgets()

    def setup_widget_layout(self, widget):
        # Crée un QVBoxLayout si le widget n'en a pas déjà un
        if widget.layout() is None:
            layout = QVBoxLayout(widget)
            widget.setLayout(layout)

    def init_widgets(self):
        self.setup_widget_layout(self.country_wdg)
        self.setup_widget_layout(self.date_wdg)

        # Créer et ajouter les QTableWidgets
        self.country_date_income_table = QTableWidget()
        self.date_country_income_table = QTableWidget()
        self.country_wdg.layout().addWidget(self.country_date_income_table)
        self.date_wdg.layout().addWidget(self.date_country_income_table)

    def load_data(self):
        """ Chargement des données depuis la base de données. """
        query = "SELECT * FROM sales_data"
        df = pd.read_sql_query(query, self.db_manager.connection)
        print(df.head())
        return df

    def update_kpi_labels(self, df):
        total_revenue = df['monthly_revenue'].sum()
        total_costs = df['monthly_costs'].sum()
        net_income = total_revenue - total_costs - df['advertising_costs'].sum()

        self.revenue_label.setText(f"Total Revenue: {total_revenue:,.2f} €")
        self.costs_label.setText(f"Total Costs: {total_costs:,.2f} €")
        self.label_3.setText(f"Net Income: {net_income:,.2f} €")

    def update_display(self):
        """ Mise à jour de l'affichage en fonction des données chargées. """
        df = self.load_data()
        if not df.empty:
            self.update_kpi_labels(df)
            self.update_income_tables(df)
        else:
            self.clear_tables()


    def first_graph(self):
        """Crée un graphique à barres pour afficher les revenus mensuels par pays."""
        df = self.load_data()
        if not df.empty:
            monthly_revenue_by_country = df.groupby('country')['monthly_revenue'].sum()
            monthly_revenue_by_country.plot(kind='bar', title='Monthly Revenue by Country')
            plt.ylabel('Revenue (€)')
            plt.show()
        else:
            print("No data to display.")

    def second_graph(self):
        """Crée un graphique à barres pour afficher les coûts mensuels par pays."""
        df = self.load_data()
        if not df.empty:
            monthly_costs_by_country = df.groupby('country')['monthly_costs'].sum()
            monthly_costs_by_country.plot(kind='bar', title='Monthly Costs by Country')
            plt.ylabel('Costs (€)')
            plt.show()
        else:
            print("No data to display.")

    def update_income_tables(self, df):
        # Group and aggregate data for income by country and date
        income_by_country_date = df.groupby(['country', 'date']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')
        income_by_date_country = df.groupby(['date', 'country']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')

        self.setup_table(self.country_date_income_table, income_by_country_date)
        self.setup_table(self.date_country_income_table, income_by_date_country)

    def setup_table(self, table_widget, data_df):
        """ Configure un QTableWidget avec des données DataFrame. """
        table_widget.setRowCount(data_df.shape[0])
        table_widget.setColumnCount(data_df.shape[1])
        table_widget.setHorizontalHeaderLabels(data_df.columns.tolist())
        for i in range(data_df.shape[0]):
            for j in range(data_df.shape[1]):
                item = QTableWidgetItem(str(data_df.iloc[i, j]))
                table_widget.setItem(i, j, item)

    def clear_tables(self):
        """ Efface toutes les tables et labels lorsqu'il n'y a pas de données. """
        self.revenue_label.setText("No Data")
        self.costs_label.setText("No Data")
        self.label_3.setText("No Data")
        self.country_date_income_table.clear()
        self.date_country_income_table.clear()

    def generate_pdf(self):
        """Generates a PDF report detailing KPIs including revenue, costs, and net income by country and date."""
        # Set the path to save the PDF
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'KPI_Report.pdf')

        # Create a PDF document template with specified pagesize
        doc = SimpleDocTemplate(download_path, pagesize=A4)
        story = []

        # Get default styles and customize
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        body_style = styles['BodyText']

        # Add a title and the KPI summaries to the document
        story.append(Paragraph('KPI Report', header_style))
        story.append(Paragraph(f'Total Revenue: {self.revenue_label.text()}', body_style))
        story.append(Paragraph(f'Total Costs: {self.costs_label.text()}', body_style))
        story.append(Paragraph(f'Net Income: {self.label_3.text()}', body_style))
        story.append(Spacer(1, 0.2 * inch))

        # Prepare the data for inclusion in the report
        df_country_date, df_date_country = self.prepare_data_for_pdf()

        # Convert DataFrame data into a format suitable for ReportLab's Table object
        data_country_date = [['Country', 'Date', 'Net Income']] + df_country_date.values.tolist()
        data_date_country = [['Date', 'Country', 'Net Income']] + df_date_country.values.tolist()

        # Create tables for the PDF
        table_country_date = Table(data_country_date, [200, 200, 100])
        table_date_country = Table(data_date_country, [200, 200, 100])

        # Define table styles
        for table in (table_country_date, table_date_country):
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ]))

        # Add tables to the story
        story.append(Spacer(1, 0.5 * inch))
        story.append(Paragraph('Income by Country and Date', header_style))
        story.append(table_country_date)
        story.append(Spacer(1, 0.5 * inch))
        story.append(Paragraph('Income by Date and Country', header_style))
        story.append(table_date_country)

        # Build the PDF document
        doc.build(story)
        print(f"PDF created and saved as '{download_path}'.")

    def prepare_data_for_pdf(self):
        """Prepares data for PDF report by querying the database and grouping it by country/date and date/country."""
        df = self.load_data()  # Load data from the database

        # Group and aggregate data for income by country and date
        df_country_date = df.groupby(['country', 'date']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(
            name='Net Income')

        # Group and aggregate data for income by date and country
        df_date_country = df.groupby(['date', 'country']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(
            name='Net Income')

        return df_country_date, df_date_country

    def show(self):
        """ Afficher le widget et mettre à jour l'affichage. """
        self.update_display()
        super().show()