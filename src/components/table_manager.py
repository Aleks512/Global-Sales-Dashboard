from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from database import DatabaseManager

class TableManager:
    """
    Manages the QTableWidget for displaying and interacting with data rows of database.
    Its primary role could be focused on handling the operations and interactions of the table data (like CRUD operations),
    without needing to know about the specific columns or context of the data it's displaying.
    This makes TableManager more reusable and generic, which can be adapted to different types of data tables in the same application.
    """
    def __init__(self, table_widget: QTableWidget, db_manager: DatabaseManager):
        self.table_widget = table_widget # table_widget : Instance de QTableWidget utilisée pour afficher les données
        self.db_manager = db_manager # db_manager : Instance de DatabaseManager pour interagir avec la base de données.


    def setup_table(self, headers):
        self.table_widget.setColumnCount(len(headers)) # Set the number of columns
        self.table_widget.setHorizontalHeaderLabels(headers) # Set the column headers
        self.table_widget.setAlternatingRowColors(True) # Set alternate row colors for better readability

    def load_data(self):
        """Fetch all data from the database and populate the table"""
        data = self.db_manager.fetch_all() #("SELECT * FROM sales_data")
        # print(data) [(1, 'Paris', 'France', '2024-01-30', 584963.0, 856.0, 15, 85, 95, 8500.0), (2, 'Celine', 'France', '2024-01-30', 584963.0, 856.0, 15, 85, 95, 8500.0)]
        self.table_widget.setRowCount(0) # clear the data before loading new data
        for data_row in data:
            self.add_row(data_row)
            #print(data_row) (2, 'Celine', 'France', '2024-01-30', 584963.0, 856.0, 15, 85, 95, 8500.0)

    def add_row(self, data_row):
        # Cette méthode permet d'ajouter une nouvelle ligne de données à la table en insérant une nouvelle
        # ligne et en remplissant chaque cellule de cette ligne avec les valeurs fournies
        """Add a single row of data to the table."""
        row_index = self.table_widget.rowCount()
        # méthode de QTableWidget retourne le nombre actuel de lignes dans le widget de table.
        # Cela permet de déterminer l'index de la prochaine ligne vide.
        self.table_widget.insertRow(row_index) # On insère une nouvelle ligne à l'index spécifié (row_index).
        # Cette ligne est ajoutée à la fin de la table.
        for column_index, value in enumerate(data_row): # parcourt chaque valeur dans data_row
            # avec son index de colonne
            item = QTableWidgetItem(str(value)) # On crée un nouvel objet QTableWidgetItem pour chaque valeur,
            # en la convertissant en chaîne de caractères si nécessaire.
            self.table_widget.setItem(row_index, column_index, item)

    def delete_row(self, row_index):
        """Delete a row from the table and the database."""
        if row_index < self.table_widget.rowCount(): # Vérifie si l'index de la ligne est valide (c'est-à-dire
            # qu'il est inférieur au nombre actuel de lignes dans la table)
            id = int(self.table_widget.item(row_index, 0).text()) # récupère l'ID de la ligne à supprimer
            # en accédant à l'élément de la première colonne (0) de la ligne spécifiée (row_index). On convertit ce
            # texte en entier, car l'ID est généralement un entier.
            self.db_manager.delete_entry(id) # appelle la méthode delete_entry du DatabaseManager pour supprimer
            # l'entrée correspondante dans la base de données.
            self.table_widget.removeRow(row_index)
            QMessageBox.information(None, "Success", "The row has been successfully deleted.")

    def header_to_db_column(self, header_text):
        """Map table headers to database column names."""
        # Normalize header text to database column names
        mapping = {
            'ID': 'id',
            'Filiale Name': 'filiale_name',
            'Country': 'country',
            'Date': 'date',
            'Revenue €': 'monthly_revenue',
            'Costs €': 'monthly_costs',
            'Volume': 'sales_volume',
            'Clients': 'new_clients',
            'Satisfaction %': 'satisfaction_rate',
            'Ad Costs': 'advertising_costs'
        }
        return mapping.get(header_text)

    def update_all_rows(self):
        """Update all modified rows in the database."""
        errors = False
        for row in range(self.table_widget.rowCount()):
            if not self.update_row(row):
                self.table_widget.selectRow(row)  # Focus on the problematic row
                QMessageBox.warning(None, "Update Issue",
                                    "An issue occurred during update. Check the row with incorrect inputs.")
                errors = True
                break  # Stop at the first error

        if not errors:
            QMessageBox.information(None, "Success", "All data have been successfully updated.")

    def update_row(self, row):
        """
        Update a single row in the database based on current table data.
        This method includes validation checks and error handling to ensure data integrity.
        """
        id = int(self.table_widget.item(row, 0).text()) # Récupère l'ID de la ligne à mettre à jour
        original_data = { # Récupère les données actuelles de la ligne à mettre à jour
            self.header_to_db_column(self.table_widget.horizontalHeaderItem(col).text()): self.table_widget.item(row,
                                                                                                                 col).text()
            for col in range(1, self.table_widget.columnCount())} # pour chaque colonne de la table
        updated_data = {} # Initialise un dictionnaire pour stocker les données mises à jour
        errors = False # Initialise une variable pour suivre les erreurs de validation

        try:
            for col in range(1, self.table_widget.columnCount()):
                header_text = self.table_widget.horizontalHeaderItem(col).text() # Récupère le texte de l'en-tête de la colonne
                db_column_name = self.header_to_db_column(header_text) # Convertit le texte de l'en-tête en nom de colonne de la base de données
                cell_value = self.table_widget.item(row, col).text() # Récupère la valeur de la cellule à mettre à jour

                if db_column_name in ['filiale_name', 'country']: # Vérifie si la colonne est un texte
                    if not self.is_string(cell_value): # Vérifie si la valeur est une chaîne de caractères valide
                        raise ValueError(f"Expected a text value for '{header_text}'") # Lève une exception si la valeur n'est pas valide
                elif db_column_name in ['monthly_revenue', 'monthly_costs', 'advertising_costs']: # Vérifie si la colonne est un nombre
                    if not self.is_float(cell_value):  # Vérifie si la valeur est un nombre flottant valide
                        raise ValueError(f"Expected a numeric value for '{header_text}'") # Lève une exception si la valeur n'est pas valide
                elif db_column_name in ['sales_volume', 'new_clients', 'satisfaction_rate']: # Vérifie si la colonne est un entier
                    if not self.is_int(cell_value):     # Vérifie si la valeur est un entier valide
                        raise ValueError(f"Expected an integer value for '{header_text}'") # Lève une exception si la valeur n'est pas valide

                updated_data[db_column_name] = cell_value # Stocke la valeur mise à jour dans le dictionnaire des données mises à jour

            if not errors:
                self.db_manager.update_entry(id, **updated_data) # Appelle la méthode update_entry du DatabaseManager pour mettre à jour l'entrée dans la base de données
        except Exception as e:
            QMessageBox.warning(None, "Update Error", f"An error occurred: {str(e)}. Reverting changes.")
            self.db_manager.update_entry(id, **original_data)  # Rollback to original data
            return False

        return True

    def is_float(self, value):
        """Check if a value can be converted to a float."""
        try: # Tente de convertir la valeur en nombre flottant
            float(value)
            return True
        except ValueError: # Si une exception ValueError est levée, la valeur n'est pas un nombre flottant valide
            return False

    def is_int(self, value):
        """Check if a value can be converted to an integer."""
        try:
            int(value)
            return True
        except ValueError: # Si une exception ValueError est levée, la valeur n'est pas un entier valide
            return False

    def is_string(self, value):
        # Check if the input is a string and it's not empty after stripping whitespace
        if isinstance(value, str) and value.strip():
            # Further check to reject strings that are actually numbers or contain unwanted characters
            if value.replace(' ', '').isalpha():  # This checks if the string is all alphabetic
                return True
            else:
                QMessageBox.warning(None, "Input Error", "Please enter a valid text string without numbers.")
                return False
        else:
            QMessageBox.warning(None, "Input Error", "Please enter a valid text string.")
            return False
