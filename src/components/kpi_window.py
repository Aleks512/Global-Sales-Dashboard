import os
import pandas as pd
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from ui.kpi_ui import Ui_kpi_window



class KPIManager(QMainWindow, Ui_kpi_window):
    """Gestionnaire de KPI pour afficher les indicateurs clés de performance et générer des rapports."""
    def __init__(self, db_manager):
        super().__init__() # Appelle le constructeur des classes parentes.
        self.db_manager = db_manager  # Utilisation du singleton de la base de données
        self.setupUi(self)  # Initialisation de l'interface utilisateur depuis Ui_kpi_window
        #configure les widgets et les layouts définis dans le fichier .ui. Elle prend une instance de QMainWindow
        # (ici self) et configure l'interface utilisateur en conséquence
        self.pushButton.clicked.connect(self.generate_pdf) # Connexion du bouton pour générer un PDF
        self.init_widgets() # Initialisation des widgets
        self.setWindowTitle("Sales Data Management")    # Définition du titre de la fenêtre

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
        """ Chargement des données depuis la base de données dans un DataFrame pandas. . """
        query = "SELECT * FROM sales_data"
        df = pd.read_sql_query(query, self.db_manager.connection)
        print(df.head())
        return df

    def update_kpi_labels(self, df):
        """ egroupe et agrège les données pour les revenus nets par pays et date,
        et par date et pays, puis configure les tables pour afficher ces données. """
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
        table_widget.setRowCount(data_df.shape[0]) # Nombre de lignes
        table_widget.setColumnCount(data_df.shape[1]) # Nombre de colonnes
        table_widget.setHorizontalHeaderLabels(data_df.columns.tolist()) # Noms des colonnes
        for i in range(data_df.shape[0]): # Remplissage des cellules
            for j in range(data_df.shape[1]): # Parcours des lignes et colonnes
                item = QTableWidgetItem(str(data_df.iloc[i, j])) # Création d'un élément de cellule
                table_widget.setItem(i, j, item) # Ajout de l'élément à la table

    def clear_tables(self): # Efface toutes les tables et labels lorsqu'il n'y a pas de données.
        """ Efface toutes les tables et labels lorsqu'il n'y a pas de données. """
        self.revenue_label.setText("No Data") # Affiche "No Data" dans les labels
        self.costs_label.setText("No Data") # Affiche "No Data" dans les labels
        self.label_3.setText("No Data")     # Affiche "No Data" dans les labels
        self.country_date_income_table.clear() # Efface les tables
        self.date_country_income_table.clear() # Efface les tables

    def generate_pdf(self): # Génère un rapport PDF avec les KPI
        """Generates a PDF report detailing KPIs including revenue, costs, and net income by country and date."""
        # Set the path to save the PDF
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'KPI_Report.pdf') # Chemin de téléchargement

        # Create a PDF document template with specified pagesize
        doc = SimpleDocTemplate(download_path, pagesize=A4) # Crée un document PDF avec une taille de page A4
        story = [] # Liste pour stocker les éléments du document

        # Get default styles and customize
        styles = getSampleStyleSheet() # Styles par défaut
        header_style = styles['Heading1'] # Style pour les en-têtes
        body_style = styles['BodyText'] # Style pour le texte

        # Add a title and the KPI summaries to the document
        story.append(Paragraph('KPI Report', header_style)) # Ajoute un titre
        story.append(Paragraph(f'Total Revenue: {self.revenue_label.text()}', body_style))  # Ajoute le total des revenus
        story.append(Paragraph(f'Total Costs: {self.costs_label.text()}', body_style))  # Ajoute le total des coûts
        story.append(Paragraph(f'Net Income: {self.label_3.text()}', body_style))   # Ajoute le revenu net
        story.append(Spacer(1, 0.2 * inch)) # Ajoute un espace

        # Prepare the data for inclusion in the report
        df_country_date, df_date_country = self.prepare_data_for_pdf() # Prépare les données pour le rapport PDF

        # Convert DataFrame data into a format suitable for ReportLab's Table object
        data_country_date = [['Country', 'Date', 'Net Income']] + df_country_date.values.tolist()   # Données par pays et date
        data_date_country = [['Date', 'Country', 'Net Income']] + df_date_country.values.tolist()   # Données par date et pays

        # Create tables for the PDF
        table_country_date = Table(data_country_date, [200, 200, 100]) # Tableau pour les données par pays et date
        table_date_country = Table(data_date_country, [200, 200, 100]) # Tableau pour les données par date et pays

        # Define table styles
        for table in (table_country_date, table_date_country): # Parcours des tables
            table.setStyle(TableStyle([ # Style des tables
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey), # Couleur de fond pour la première ligne
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), # Couleur du texte pour la première ligne
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),      # Alignement du texte au centre
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),   # Police en gras
                ('GRID', (0, 0), (-1, -1), 1, colors.black),    # Couleur de la grille
                ('BOX', (0, 0), (-1, -1), 2, colors.black),    # Couleur de la bordure
            ]))

        # Add tables to the story
        story.append(Spacer(1, 0.5 * inch)) # Ajoute un espace
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

    def create_costs_graph(self):
        """Creates a bar graph for monthly costs by country and returns a QPixmap."""
        df = self.load_data()
        if not df.empty:
            monthly_costs_by_country = df.groupby('country')['monthly_costs'].sum()
            fig, ax = plt.subplots(figsize=(5.44, 2.92))  # Size in inches to match QGraphicView size
            monthly_costs_by_country.plot(kind='bar', color='red', title='Monthly Costs by Country', ax=ax)
            ax.set_ylabel('Costs (€)')
            return self.fig_to_pixmap(fig)
        else:
            print("No data to display.")
            return None

    def create_revenue_graph(self):
        """Creates a bar graph for monthly revenue by country and returns a QPixmap."""
        df = self.load_data()
        if not df.empty:
            fig, ax = plt.subplots(figsize=(5.44, 2.92))  # Size in inches to match QGraphicView size
            monthly_revenue_by_country = df.groupby('country')['monthly_revenue'].sum()
            monthly_revenue_by_country.plot(kind='bar', color='blue', title='Monthly Revenue by Country', ax=ax)
            ax.set_ylabel('Revenue (€)')
            return self.fig_to_pixmap(fig)
        else:
            print("No data to display.")
            return None

    def fig_to_pixmap(self, fig):
        """Converts a matplotlib figure to a QPixmap."""
        canvas = FigureCanvasAgg(fig) # Convertit la figure en un canevas
        canvas.draw() # Dessine le canevas
        buf = canvas.buffer_rgba() # Convertit le canevas en un tampon RGBA
        qimage = QImage(buf, int(fig.get_size_inches()[0] * fig.dpi), int(fig.get_size_inches()[1] * fig.dpi), QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap


    # def first_graph(self):
    #     """Crée un graphique à barres pour afficher les revenus mensuels par pays."""
    #     df = self.load_data()
    #     if not df.empty:
    #         monthly_revenue_by_country = df.groupby('country')['monthly_revenue'].sum()
    #         monthly_revenue_by_country.plot(kind='bar', title='Monthly Revenue by Country')
    #         plt.ylabel('Revenue (€)')
    #         plt.show()
    #     else:
    #         print("No data to display.")
    #
    # def second_graph(self):
    #     """Crée un graphique à barres pour afficher les coûts mensuels par pays."""
    #     df = self.load_data()
    #     if not df.empty:
    #         monthly_costs_by_country = df.groupby('country')['monthly_costs'].sum()
    #         monthly_costs_by_country.plot(kind='bar', title='Monthly Costs by Country')
    #         plt.ylabel('Costs (€)')
    #         plt.show()
    #     else:
    #         print("No data to display.")

    def show(self):
        """ Afficher le widget et mettre à jour l'affichage. """
        self.update_display() # Met à jour l'affichage
        super().show() # Affiche le widget