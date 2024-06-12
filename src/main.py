import sys
from PySide6.QtWidgets import QApplication
from controller import MainWindowController
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting application...")
    app = QApplication(sys.argv)
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
