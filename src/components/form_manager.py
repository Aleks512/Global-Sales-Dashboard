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
            filiale_name = self.ui.fil_name_le.text()
            country = self.ui.country_le.text()
            date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
            monthly_revenue = float(self.ui.revenue_le.text())
            monthly_costs = float(self.ui.costs_le.text())
            sales_volume = int(self.ui.vol_le.text())
            new_clients = int(self.ui.new_client_nr_le.text())
            satisfaction_rate = int(self.ui.satisfaction_le.text())
            advertising_costs = float(self.ui.depense_pub_le.text())
            return {
                "filiale_name": filiale_name,
                "country": country,
                "date": date,
                "monthly_revenue": monthly_revenue,
                "monthly_costs": monthly_costs,
                "sales_volume": sales_volume,
                "new_clients": new_clients,
                "satisfaction_rate": satisfaction_rate,
                "advertising_costs": advertising_costs
            }
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
            QMessageBox.warning(None, "Input Error", "All fields are required.")
            return False
        return True
