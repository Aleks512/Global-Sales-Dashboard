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
                "filiale_name": self.ui.fil_name_le.text().strip(),
                "country": self.ui.country_le.text().strip(),
                "date": self.ui.dateEdit.date().toString("yyyy-MM-dd"),
                "monthly_revenue": float(self.ui.revenue_le.text()),
                "monthly_costs": float(self.ui.costs_le.text()),
                "sales_volume": int(self.ui.vol_le.text()),
                "new_clients": int(self.ui.new_client_nr_le.text()),
                "satisfaction_rate": int(self.ui.satisfaction_le.text()),
                "advertising_costs": float(self.ui.depense_pub_le.text())
            }
            if not self.validate_data(data):
                return None
            return data
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
        if not all(data.values()):
            QMessageBox.warning(None, "Erreur de saisie", "Veuillez vérifier vos saisies. Tous les champs doivent être correctement remplis.")
            return False
        if any([
            data["monthly_revenue"] < 0, data["monthly_costs"] < 0,
            data["sales_volume"] < 0, data["new_clients"] < 0,
            data["satisfaction_rate"] < 0 or data["satisfaction_rate"] > 100,
            data["advertising_costs"] < 0
        ]):
            QMessageBox.warning(None, "Input Error", "Numeric fields must not be negative, and satisfaction rate must be between 0 and 100.")
            return False
        return True
