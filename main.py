import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import QRectF
from PyQt6 import uic


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем интерфейс из файла
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.drawButton.clicked.connect(self.add_circle)

    def add_circle(self):
        # Получаем размеры области просмотра graphicsView
        view_width = self.graphicsView.viewport().width()
        view_height = self.graphicsView.viewport().height()

        # Генерируем случайный диаметр (от 10 до 100)
        diameter = random.randint(10, 100)

        # Вычисляем максимальные координаты для размещения окружности
        max_x = max(0, view_width - diameter)
        max_y = max(0, view_height - diameter)

        # Если места нет, не добавляем окружность
        if max_x <= 0 or max_y <= 0:
            return

        # Случайные координаты
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)

        # Создаем окружность (эллипс с равными осями)
        ellipse = QGraphicsEllipseItem(QRectF(x, y, diameter, diameter))
        ellipse.setBrush(QBrush(QColor(255, 255, 0)))  # Желтый цвет
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())