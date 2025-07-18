# :|
from PyQt5.QtWidgets import QApplication
from use_cases.CU06_login_screen import LoginScreen
from main_window import MainWindow

def launch_main(user):
    main = MainWindow(user)
    main.center_on_screen()
    main.show()
    login.close()

app = QApplication([])
login = LoginScreen(on_login_success=launch_main)
login.center_on_screen()
login.show()
app.exec()
