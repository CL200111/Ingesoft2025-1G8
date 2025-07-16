from PyQt6.QtWidgets import QApplication
import sys
from login import LoginWindow

def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()