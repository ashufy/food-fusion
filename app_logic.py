from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from recipe_api import search_recipes

class ImageLoaderWorker(QThread):
    imageLoaded = pyqtSignal(int, QPixmap)

    def __init__(self, recipes):
        super().__init__()
        self.recipes = recipes


    def run(self):
        import requests
        for idx, recipe in enumerate(self.recipes):
            pixmap = None
            url = recipe.get("image")
            if url:
                try:
                    img_data = requests.get(url, timeout=6).content
                    pixmap = QPixmap()
                    pixmap.loadFromData(img_data)
                    pixmap = pixmap.scaled(150, 110, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                except Exception:
                    pixmap = None
            self.imageLoaded.emit(idx, pixmap)

class FoodFusionLogic:
    def __init__(self, ui):
        self.ui = ui
        self.ui.searchButton.clicked.connect(self.handle_search)
        self.ui.resetButton.clicked.connect(self.reset_app)
        self.image_labels = []
        self.recipe_cards = []

    def handle_search(self):
        ingredients_text = self.ui.ingredientsEdit.text().strip()
        if not ingredients_text:
            self.ui.statusLabel.setText("Please enter at least one ingredient.")
            return
        ingredients = [i.strip() for i in ingredients_text.split(",") if i.strip()]
        category = "veg" if self.ui.vegRadio.isChecked() else "nonveg"
        self.ui.statusLabel.setText("Loading recipes...")
        self.ui.searchButton.setDisabled(True)
        QApplication.processEvents()

        # Clear previous results
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.image_labels.clear()
        self.recipe_cards.clear()

        recipes = search_recipes(ingredients, category)
        QApplication.processEvents()

        if not recipes:
            self.ui.statusLabel.setText("No recipes found for the given ingredients.")
            self.ui.searchButton.setDisabled(False)
            return

        max_items = min(15, len(recipes))
        cols = 3
        for idx, recipe in enumerate(recipes[:max_items]):
            row, col = idx // cols, idx % cols
            card = self.create_recipe_card(recipe, idx)
            self.ui.gridLayout.addWidget(card, row, col)
            self.recipe_cards.append(card)

        # Start threaded image loading
        self.loader_thread = ImageLoaderWorker(recipes[:max_items])
        self.loader_thread.imageLoaded.connect(self.update_card_image)
        self.loader_thread.finished.connect(self.finish_loading)
        self.loader_thread.start()

    def create_recipe_card(self, recipe, idx):
        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setStyleSheet("""
            QFrame {
                background: #fff;
                border-radius: 13px;
                border: 2px solid #e2f7e1;
                
                padding: 6px;
            }
            QFrame:hover {
                border: 2px solid #ffa64d;
            }
        """)
        vbox = QVBoxLayout(card)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        img_label = QLabel()
        img_label.setFixedSize(150, 110)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_label.setText("Loading image...")
        self.image_labels.append(img_label)
        vbox.addWidget(img_label)

        # Recipe name as clickable label
        name_label = QLabel(f"<a href='{recipe['link']}'>{recipe['name']}</a>")
        name_label.setOpenExternalLinks(True)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("""
            QLabel {
                font-size:14px; color:#ffa64d;
                margin-top:6px; margin-bottom:1px;
            }
            QLabel:hover { color: #222; }
        """)
        vbox.addWidget(name_label)
        return card

    def update_card_image(self, idx, pixmap):
        if 0 <= idx < len(self.image_labels):
            label = self.image_labels[idx]
            if pixmap:
                label.setPixmap(pixmap)
                label.setText("")
            else:
                label.setText("No Image")

    def finish_loading(self):
        self.ui.statusLabel.setText("")
        self.ui.searchButton.setDisabled(False)

    def reset_app(self):
        self.ui.ingredientsEdit.clear()
        self.ui.vegRadio.setChecked(True)
        self.ui.statusLabel.clear()
        # Remove previous results
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.image_labels.clear()
        self.recipe_cards.clear()
        self.ui.searchButton.setDisabled(False)

