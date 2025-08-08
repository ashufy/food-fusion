from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow
from app_logic import FoodFusionLogic
import sys

class FoodFusionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Apply color styles
        self.setStyleSheet("""
            QMainWindow { background: #f0f0f5; }
            QWidget { background: #c2d6d6; }
            QPushButton {
                background-color: #ffa64d;
                color: #222;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px 24px;
            }
            QPushButton:hover { background-color: #ff9900; }
            QLineEdit {
                background: #fff;
                font-size: 15px;
                padding: 7px;
                border-radius: 7px;
            }
            QRadioButton {
                font-size: 15px;
                margin-right: 10px;
            }
        """)
        # Attach app logic
        self.logic = FoodFusionLogic(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FoodFusionApp()
    window.show()
    sys.exit(app.exec())
