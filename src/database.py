import os
import sqlite3

class DatabaseManager:
    _instance = None  # Singleton pattern to ensure only one instance exists

    def __new__(cls, db_filename):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            # Initialization of the instance
            cls._instance.db_filename = db_filename
            full_path = os.path.abspath(db_filename)
            cls._instance.connection = sqlite3.connect(full_path, check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.initialize_database()
        return cls._instance

    def initialize_database(self):
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
            )
        """)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_entry(self, filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs):
        try:
            self.cursor.execute("""
                INSERT INTO sales_data (filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs))
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            self.connection.rollback()

    def fetch_all(self):
        self.cursor.execute("SELECT id, filiale_name, country, date, monthly_revenue, monthly_costs, sales_volume, new_clients, satisfaction_rate, advertising_costs FROM sales_data")
        return self.cursor.fetchall()

    def update_entry(self, id, **kwargs):
        columns = ', '.join([f"{k} = ?" for k in kwargs])
        values = list(kwargs.values()) + [id]
        self.cursor.execute(f"UPDATE sales_data SET {columns} WHERE id = ?", values)
        self.connection.commit()

    def delete_entry(self, id):
        self.cursor.execute("DELETE FROM sales_data WHERE id = ?", (id,))
        self.connection.commit()
