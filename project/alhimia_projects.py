import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QGridLayout, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt, QMimeData, QPoint
from PyQt6.QtGui import QDrag, QFont, QColor, QPalette

# РЕЦЕПТЫ
recipes = {
    ("вода", "огонь"): "пар",
    ("вода", "земля"): "грязь",
    ("земля", "огонь"): "лава",
    ("воздух", "огонь"): "энергия",
    ("вода", "воздух"): "дождь",
    ("воздух", "земля"): "пыль",
    ("воздух", "пар"): "облако",
    ("воздух", "облако"): "ветер",
    ("вода", "облако"): "дождь",
    ("дождь", "земля"): "растение",
    ("вода", "лава"): "камень",
    ("камень", "огонь"): "металл",
    ("металл", "огонь"): "инструмент",
    ("огонь", "растение"): "уголь",
    ("грязь", "огонь"): "кирпич",
    ("воздух", "камень"): "песок",
    ("огонь", "песок"): "стекло",
    ("камень", "металл"): "нож",
    ("камень", "энергия"): "молния",
    ("вода", "энергия"): "жизнь",
    ("жизнь", "земля"): "человек",
    ("инструмент", "человек"): "ремесленник",
    ("человек", "человек"): "деревня",
}

# Эмодзи для элементов
ICONS = {
    "вода": "💧", "огонь": "🔥", "земля": "🌍", "воздух": "💨",
    "пар": "♨️", "грязь": "🟫", "лава": "🌋", "энергия": "⚡",
    "дождь": "🌧️", "пыль": "🌫️", "облако": "☁️", "ветер": "🌬️",
    "растение": "🌿", "камень": "🪨", "металл": "⚙️", "инструмент": "🔧",
    "уголь": "🖤", "кирпич": "🧱", "песок": "⏳", "стекло": "🪟",
    "нож": "🔪", "молния": "⚡", "жизнь": "✨", "человек": "🧑",
    "ремесленник": "👷", "деревня": "🏘️",
}


# КНОПКА-ЭЛЕМЕНТ
class ElementButton(QPushButton):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.element_name = name
        icon = ICONS.get(name, "❓")
        self.setText(f"{icon}\n{name}")
        self.setFixedSize(90, 70)
        self.setFont(QFont("Segoe UI", 9))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2d2d44;
                color: white;
                border: 2px solid #555577;
                border-radius: 10px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #3d3d60;
                border: 2px solid #8888ff;
            }
            QPushButton:pressed {
                background-color: #5555aa;
            }
        """)


# СЛОТ ДЛЯ ВЫБРАННОГО ЭЛЕМЕНТА
class SlotLabel(QLabel):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        self.placeholder = placeholder
        self.element_name = None
        self.reset()
        self.setFixedSize(120, 90)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Segoe UI", 10))
        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e30;
                color: #aaaacc;
                border: 2px dashed #555577;
                border-radius: 12px;
            }
        """)

    def set_element(self, name):
        self.element_name = name
        icon = ICONS.get(name, "❓")
        self.setText(f"{icon}\n{name}")
        self.setStyleSheet("""
            QLabel {
                background-color: #2a2a50;
                color: white;
                border: 2px solid #8888ff;
                border-radius: 12px;
                font-weight: bold;
            }
        """)

    def reset(self):
        self.element_name = None
        self.setText(self.placeholder)
        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e30;
                color: #aaaacc;
                border: 2px dashed #555577;
                border-radius: 12px;
            }
        """)


# ГЛАВНОЕ ОКНО
class AlchemyGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.my_elements = ["вода", "огонь", "земля", "воздух"]
        self.setWindowTitle("⚗️ Алхимия")
        self.setMinimumSize(700, 600)
        self.setStyleSheet("background-color: #12121f; color: white;")
        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Заголовок
        title = QLabel("⚗️ АЛХИМИЯ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title.setStyleSheet("color: #aaaaff; letter-spacing: 4px;")
        main_layout.addWidget(title)

        # Счётчик
        self.counter_label = QLabel()
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.counter_label.setFont(QFont("Segoe UI", 10))
        self.counter_label.setStyleSheet("color: #777799;")
        self.update_counter()
        main_layout.addWidget(self.counter_label)

        # Зона комбинации
        combine_frame = QFrame()
        combine_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1a2e;
                border: 1px solid #333355;
                border-radius: 15px;
            }
        """)
        combine_layout = QHBoxLayout(combine_frame)
        combine_layout.setSpacing(15)
        combine_layout.setContentsMargins(20, 15, 20, 15)

        self.slot1 = SlotLabel("[ Элемент 1 ]")
        self.slot2 = SlotLabel("[ Элемент 2 ]")

        plus_label = QLabel("+")
        plus_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        plus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        plus_label.setStyleSheet("color: #8888ff; background: transparent; border: none;")

        equals_label = QLabel("=")
        equals_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        equals_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        equals_label.setStyleSheet("color: #8888ff; background: transparent; border: none;")

        self.result_slot = SlotLabel("[ Результат ]")
        self.result_slot.setStyleSheet("""
            QLabel {
                background-color: #1e1e30;
                color: #aaaacc;
                border: 2px dashed #ffaa44;
                border-radius: 12px;
            }
        """)

        combine_layout.addWidget(self.slot1)
        combine_layout.addWidget(plus_label)
        combine_layout.addWidget(self.slot2)
        combine_layout.addWidget(equals_label)
        combine_layout.addWidget(self.result_slot)
        main_layout.addWidget(combine_frame)

        # Кнопки управления
        btn_layout = QHBoxLayout()

        self.combine_btn = QPushButton("⚗️  Соединить!")
        self.combine_btn.setFixedHeight(45)
        self.combine_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.combine_btn.setStyleSheet("""
            QPushButton {
                background-color: #4444aa;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover { background-color: #5555cc; }
            QPushButton:pressed { background-color: #333388; }
        """)
        self.combine_btn.clicked.connect(self.combine_elements)

        self.reset_btn = QPushButton("🔄  Сбросить")
        self.reset_btn.setFixedHeight(45)
        self.reset_btn.setFont(QFont("Segoe UI", 12))
        self.reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #333344;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover { background-color: #444466; }
            QPushButton:pressed { background-color: #222233; }
        """)
        self.reset_btn.clicked.connect(self.reset_slots)

        btn_layout.addWidget(self.combine_btn)
        btn_layout.addWidget(self.reset_btn)
        main_layout.addLayout(btn_layout)

        # Лог результата
        self.log_label = QLabel("Выбери два элемента и нажми «Соединить»!")
        self.log_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.log_label.setFont(QFont("Segoe UI", 11))
        self.log_label.setStyleSheet("""
            color: #aaaacc;
            background-color: #1a1a2e;
            border-radius: 8px;
            padding: 8px;
        """)
        main_layout.addWidget(self.log_label)

        # Коллекция элементов
        collection_label = QLabel("📦 Твоя коллекция:")
        collection_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        collection_label.setStyleSheet("color: #aaaaff;")
        main_layout.addWidget(collection_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea { border: 1px solid #333355; border-radius: 10px; }
        """)

        self.grid_widget = QWidget()
        self.grid_widget.setStyleSheet("background-color: #16162a;")
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setSpacing(8)
        scroll.setWidget(self.grid_widget)
        main_layout.addWidget(scroll)

        self.refresh_grid()

    # ЛОГИКА
    def refresh_grid(self):
        # Очищаем сетку
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().deleteLater()

        cols = 6
        for i, name in enumerate(self.my_elements):
            btn = ElementButton(name)
            btn.clicked.connect(lambda checked, n=name: self.select_element(n))
            self.grid_layout.addWidget(btn, i // cols, i % cols)

    def select_element(self, name):
        if self.slot1.element_name is None:
            self.slot1.set_element(name)
        elif self.slot2.element_name is None:
            self.slot2.set_element(name)
        else:
            # Оба заняты — перезаписываем первый
            self.slot1.set_element(name)
            self.slot2.reset()
            self.result_slot.reset()

    def combine_elements(self):
        if not self.slot1.element_name or not self.slot2.element_name:
            self.log_label.setText("⚠️ Выбери оба элемента!")
            self.log_label.setStyleSheet("""
                color: #ffaa44;
                background-color: #1a1a2e;
                border-radius: 8px;
                padding: 8px;
            """)
            return

        e1 = self.slot1.element_name
        e2 = self.slot2.element_name
        pair = tuple(sorted([e1, e2]))
        result = recipes.get(pair)

        if result:
            self.result_slot.set_element(result)
            if result not in self.my_elements:
                self.my_elements.append(result)
                self.refresh_grid()
                self.update_counter()
                self.log_label.setText(f"🎉 {e1} + {e2} = {result}! Новый элемент открыт!")
                self.log_label.setStyleSheet("""
                    color: #44ff88;
                    background-color: #1a2e1a;
                    border-radius: 8px;
                    padding: 8px;
                """)
            else:
                self.log_label.setText(f"✅ {e1} + {e2} = {result} (уже есть в коллекции)")
                self.log_label.setStyleSheet("""
                    color: #aaaacc;
                    background-color: #1a1a2e;
                    border-radius: 8px;
                    padding: 8px;
                """)
        else:
            self.result_slot.reset()
            self.log_label.setText(f"❌ {e1} + {e2} = ничего... Попробуй другое сочетание!")
            self.log_label.setStyleSheet("""
                color: #ff5555;
                background-color: #2e1a1a;
                border-radius: 8px;
                padding: 8px;
            """)

    def reset_slots(self):
        self.slot1.reset()
        self.slot2.reset()
        self.result_slot.reset()
        self.log_label.setText("Выбери два элемента и нажми «Соединить»!")
        self.log_label.setStyleSheet("""
            color: #aaaacc;
            background-color: #1a1a2e;
            border-radius: 8px;
            padding: 8px;
        """)

    def update_counter(self):
        self.counter_label.setText(
            f"Открыто элементов: {len(self.my_elements)} / {len(recipes) + 4}"
        )


# ЗАПУСК
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlchemyGame()
    window.show()
    sys.exit(app.exec())
