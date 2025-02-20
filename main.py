import sys
import random
from PyQt6.QtWidgets import (QApplication, QWidget, QGraphicsScene,
                             QGraphicsEllipseItem, QVBoxLayout,
                             QPushButton, QGraphicsView)
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import QRectF


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Generator")
        self.setGeometry(100, 100, 600, 400)

        # Создаем графическую сцену и представление
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        # Создаем кнопку
        self.button = QPushButton("Добавить окружность")
        self.button.clicked.connect(self.add_circle)

        # Настраиваем layout
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def add_circle(self):
        # Получаем размеры области просмотра
        view_width = self.view.viewport().width()
        view_height = self.view.viewport().height()

        # Генерируем случайные параметры
        diameter = random.randint(10, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        # Вычисляем допустимые координаты
        max_x = max(0, view_width - diameter)
        max_y = max(0, view_height - diameter)

        if max_x <= 0 or max_y <= 0:
            return

        # Создаем и настраиваем окружность
        ellipse = QGraphicsEllipseItem(QRectF(
            random.randint(0, max_x),
            random.randint(0, max_y),
            diameter,
            diameter
        ))
        ellipse.setBrush(QBrush(color))
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())