# ui_main_window.py
from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Title
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.titleLabel)

        # Category choice
        self.categoryLayout = QtWidgets.QHBoxLayout()
        self.vegRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.vegRadio.setText("Veg")
        self.vegRadio.setChecked(True)
        self.categoryLayout.addWidget(self.vegRadio)
        self.nonVegRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.nonVegRadio.setText("Non-Veg")
        self.categoryLayout.addWidget(self.nonVegRadio)
        self.verticalLayout.addLayout(self.categoryLayout)

        # Ingredients
        self.ingLabel = QtWidgets.QLabel(self.centralwidget)
        self.ingLabel.setObjectName("ingLabel")
        self.verticalLayout.addWidget(self.ingLabel)

        self.ingredientsEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ingredientsEdit.setObjectName("ingredientsEdit")
        self.verticalLayout.addWidget(self.ingredientsEdit)

        # Search button
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout.addWidget(self.searchButton)

        # Reset Button:
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)

        # Loader/Status
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setObjectName("statusLabel")
        self.statusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.statusLabel)

        # Results grid area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollWidget)
        self.scrollArea.setWidget(self.scrollWidget)
        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FoodFusion"))
        self.titleLabel.setText(_translate("MainWindow", "🍽️ FoodFusion Recipe Finder"))
        self.ingLabel.setText(_translate("MainWindow", "Enter ingredients (comma-separated):"))
        self.searchButton.setText(_translate("MainWindow", "Search Recipes"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.statusLabel.setText(_translate("MainWindow", ""))