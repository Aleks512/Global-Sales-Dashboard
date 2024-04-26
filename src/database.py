import os
import sqlite3

class DatabaseManager:
    """
    A singleton class to manage database operations for a sales application.

    This class ensures that only one instance of the database connection is created,
    using the Singleton design pattern. It provides methods to interact with the
    database, such as adding, fetching, updating, and deleting records.

    Attributes:
        db_filename (str): The path to the SQLite database file.
        connection (sqlite3.Connection): The SQLite connection object.
        cursor (sqlite3.Cursor): The cursor object used to execute SQL commands.
    """

    _instance = None  # Singleton instance

    def __new__(cls, db_path='sales.db'):
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.db_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), db_path)
            cls._instance.connection = sqlite3.connect(cls._instance.db_filename, check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.initialize_database()
        return cls._instance

    def initialize_database(self):
        """
        Creates the sales_data table in the database if it does not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filiale_name TEXT,
                country TEXT,
                date TEXT,
                monthly_revenue REAL,
                monthly_costs REAL,
                sales_volume INTEGER,
                new_clients INTEGER,
                satisfaction_rate INTEGER,
                advertising_costs REAL
            );
        """)
        self.connection.commit()

    def add_entry(self, filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients,
                  satisfaction_rate, advertising_costs):
        """
        Adds a new entry to the sales_data table.
        """
        try:
            self.cursor.execute("""
                INSERT INTO sales_data (filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def fetch_all(self):
        """
        Fetches all entries from the sales_data table.
        """
        self.cursor.execute("SELECT * FROM sales_data")
        return self.cursor.fetchall()

    def update_entry(self, id, filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs):
        """
        Updates an entry in the sales_data table based on the given id.
        """
        try:
            self.cursor.execute("""
                UPDATE sales_data SET
                filiale_name = ?, country = ?, date = ?, monthly_revenue = ?, monthly_costs = ?, sales_volume = ?, new_clients = ?, satisfaction_rate = ?, advertising_costs = ?
                WHERE id = ?
            """, (filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs, id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Update error: {e}")
            self.connection.rollback()
    def delete_entry(self, id):
        """
        Deletes an entry from the sales_data table based on the given id.
        """
        self.cursor.execute("DELETE FROM sales_data WHERE id = ?", (id,))
        self.connection.commit()

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()

