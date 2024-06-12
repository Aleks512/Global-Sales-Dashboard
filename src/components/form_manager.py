from PySide6.QtWidgets import QMessageBox
from datetime import datetime

class FormManager:
    """
    Form Manager for collecting and validating data entered in the user interface.

    This class handles the extraction and validation of data from form fields in a GUI. It ensures
    that the data conforms to expected formats and notifies the user about any input errors.

    Attributes:
        ui (QObject): A reference to the user interface elements, providing access to the widgets.
    """
    def __init__(self, ui_elements):
        """
        Initializes the FormManager with the necessary UI elements.

        Args:
            ui_elements (QObject): The main window or widget containing the UI elements.
        """
        self.ui = ui_elements

    def collect_data(self):
        """
          Collects data from the form fields and returns a dictionary of the data.

          This method attempts to retrieve and convert the data from UI fields to their respective
          data types. If a conversion fails due to an invalid input, it shows an error message
          and returns None.

          Returns:
              dict or None: A dictionary containing the collected data with keys corresponding to
              the form field names if all data is valid, or None if an error occurs.
          """
        try:
            data = {
                "filiale_name": self.ui.fil_name_le.text().strip(), # Remove leading/trailing whitespace
                "country": self.ui.country_le.text().strip(),
                "date": self.ui.dateEdit.date().toString("yyyy-MM-dd"),     # Convert QDate to string
                "monthly_revenue": float(self.ui.revenue_le.text()), # Convert text to float
                "monthly_costs": float(self.ui.costs_le.text()), # Convert text to float
                "sales_volume": int(self.ui.vol_le.text()), # Convert text to integer
                "new_clients": int(self.ui.new_client_nr_le.text()), # Convert text to integer
                "satisfaction_rate": int(self.ui.satisfaction_le.text()), # Convert text to integer
                "advertising_costs": float(self.ui.depense_pub_le.text()) # Convert text to float
            }
            if not self.validate_data(data): # Validate the collected data
                return None # Return None if validation fails
            return data # Return the collected data if validation succeeds
        except ValueError as e:
            QMessageBox.warning(None, "Erreur de saisie", "Veuillez vérifier vos saisies. Tous les champs doivent être correctement remplis.")
            return None

    def validate_data(self, data):
        """
        Validates the collected data.

        This method checks if any of the values in the data dictionary are missing. If data is missing,
        it displays an error message and returns False.

        Args:
            data (dict): The data dictionary collected from the form.

        Returns:
            bool: True if all data is present and valid, False if any fields are missing.
        """
        if not all(data.values()): # Check if all values are present
            QMessageBox.warning(None, "Erreur de saisie", "Veuillez vérifier vos saisies. Tous les champs doivent être correctement remplis.")
            return False
        if any([
            data["monthly_revenue"] < 0, data["monthly_costs"] < 0,     # Check for negative values
            data["sales_volume"] < 0, data["new_clients"] < 0,          # Check for negative values
            data["satisfaction_rate"] < 0 or data["satisfaction_rate"] > 100, # Check for satisfaction rate out of bounds
            data["advertising_costs"] < 0                               # Check for negative values
        ]):
            QMessageBox.warning(None, "Input Error", "Numeric fields must not be negative, and satisfaction rate must be between 0 and 100.")
            return False
        return True

    def reset_inputs(self):
        self.ui.fil_name_le.clear()
        self.ui.country_le.clear()
        self.ui.dateEdit.setDate(datetime.today())  # Reset to today's date
        self.ui.revenue_le.clear()
        self.ui.costs_le.clear()
        self.ui.vol_le.clear()
        self.ui.new_client_nr_le.clear()
        self.ui.satisfaction_le.clear()
        self.ui.depense_pub_le.clear()