from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QSizePolicy, QVBoxLayout, QHBoxLayout, \
    QPushButton, QFrame
import sys
import numpy as np
from vispy import scene


list_of_matrices = [np.random.random((18, 18)).astype('float32') for _ in range(10)]


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameStyle(QFrame.NoFrame)
        self.scroll_area.setGeometry(0, 0, 1000, 1000)

        scroll_widget = QWidget()
        self.scroll_area.setWidget(scroll_widget)
        scroll_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        scroll_area_layout = QVBoxLayout(scroll_widget)

        for matrix in list_of_matrices:
            graphplace_widget = QWidget()
            graphplace_layout = QHBoxLayout(graphplace_widget)

            canvas = scene.SceneCanvas(keys='interactive', bgcolor='w', size=(500, 500))
            view = canvas.central_widget.add_view()
            view.camera = scene.PanZoomCamera(aspect=1)
            scene.visuals.Image(matrix, parent=view.scene)
            view.camera.set_range()
            
            graphplace_layout.addWidget(canvas.native)
            scroll_area_layout.addWidget(graphplace_widget)

        self.move(QApplication.desktop().availableGeometry().topLeft())
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    main = Main()
    sys.exit(App.exec_())
