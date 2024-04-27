import os

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QWidget
import pandas as pd
from ui.kpi_ui import Ui_kpi_window

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame, Spacer, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch


class KPIManager(QMainWindow, Ui_kpi_window):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager  # Utilisation du singleton de la base de données
        self.setupUi(self)  # Initialisation de l'interface utilisateur depuis Ui_kpi_window
        self.pushButton.clicked.connect(self.generate_pdf)
        self.init_widgets()

    def init_widgets(self):
        # Assurez-vous que chaque widget a un QVBoxLayout pour ajouter des tableaux
        self.setup_widget_layout(self.country_wdg)
        self.setup_widget_layout(self.date_wdg)

        # Créer et ajouter les QTableWidgets
        self.country_date_income_table = QTableWidget()
        self.date_country_income_table = QTableWidget()
        self.country_wdg.layout().addWidget(self.country_date_income_table)
        self.date_wdg.layout().addWidget(self.date_country_income_table)

    def setup_widget_layout(self, widget):
        # Crée un QVBoxLayout si le widget n'en a pas déjà un
        if widget.layout() is None:
            layout = QVBoxLayout(widget)
            widget.setLayout(layout)

    def load_data(self):
        """ Chargement des données depuis la base de données. """
        query = "SELECT * FROM sales_data"
        df = pd.read_sql_query(query, self.db_manager.connection)
        return df

    def update_display(self):
        """ Mise à jour de l'affichage en fonction des données chargées. """
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
        self.label_3.setText(f"Net Income: {net_income:,.2f} €")

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
        # Emplacement du fichier PDF
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'KPI_Report.pdf')

        # Créer un document PDF
        doc = SimpleDocTemplate(download_path, pagesize=A4)
        story = []

        # Styles pour le document
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        body_style = styles['BodyText']

        # Ajouter des informations générales
        story.append(Paragraph('KPI Report', header_style))
        story.append(Paragraph(f'Total Revenue: {self.revenue_label.text()}', body_style))
        story.append(Paragraph(f'Total Costs: {self.costs_label.text()}', body_style))
        story.append(Paragraph(f'Net Income: {self.label_3.text()}', body_style))
        story.append(Spacer(1, 0.2 * inch))

        # Préparer les données des tableaux pour inclusion
        # Note: Assurez-vous que les DataFrames sont correctement préparées avant cette étape
        df_country_date, df_date_country = self.prepare_data_for_pdf()

        # Convertir DataFrame en données de tableau pour ReportLab
        data_country_date = [['Country', 'Date', 'Net Income']] + df_country_date.values.tolist()
        data_date_country = [['Date', 'Country', 'Net Income']] + df_date_country.values.tolist()

        # Tables
        table_country_date = Table(data_country_date)
        table_date_country = Table(data_date_country)

        table_country_date.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ]))

        table_date_country.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ]))

        # Ajouter les tables au document
        story.append(Spacer(1, 0.5 * inch))
        story.append(Paragraph('Income by Country and Date', header_style))
        story.append(table_country_date)
        story.append(Spacer(1, 0.5 * inch))
        story.append(Paragraph('Income by Date and Country', header_style))
        story.append(table_date_country)

        # Construire le document PDF
        doc.build(story)
        print(f"PDF created and saved as '{download_path}'.")

    def prepare_data_for_pdf(self):
        # Charger les données depuis la base de données ou les utiliser directement depuis les tableaux
        df = self.load_data()

        # Group and aggregate data for income by country and date
        df_country_date = df.groupby(['country', 'date']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')

        # Group and aggregate data for income by date and country
        df_date_country = df.groupby(['date', 'country']).apply(
            lambda x: x['monthly_revenue'].sum() - x['monthly_costs'].sum() - x['advertising_costs'].sum()).reset_index(name='Net Income')

        return df_country_date, df_date_country

    def add_pdf_table(self, canvas, x_pos, start_y, table_widget, title):
        """ Ajoute un tableau de données à un PDF. """
        # Ajouter le titre du tableau
        canvas.drawString(x_pos, start_y, title)

        # Obtenir les données du tableau
        num_rows = table_widget.rowCount()
        num_cols = table_widget.columnCount()

        # Ecrire les en-têtes
        row_height = 15
        for col in range(num_cols):
            canvas.drawString(x_pos + col * 100, start_y - 15, table_widget.horizontalHeaderItem(col).text())

        # Ecrire les données du tableau
        for row in range(num_rows):
            for col in range(num_cols):
                item = table_widget.item(row, col)
                if item:  # Vérifier si l'item n'est pas None
                    canvas.drawString(x_pos + col * 100, start_y - 30 - (row + 1) * row_height, item.text())

    def show(self):
        """ Afficher le widget et mettre à jour l'affichage. """
        self.update_display()
        super().show()