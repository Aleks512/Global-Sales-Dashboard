import sys
from PySide6.QtWidgets import QApplication
from controller import MainWindowController

def main():
    app = QApplication(sys.argv)
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
