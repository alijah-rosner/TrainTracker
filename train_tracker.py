import sys
from get_train_info import create_feed, arrivals_for_stop
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QPalette, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QStackedLayout, QHBoxLayout,QSizePolicy




class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("M Train Times")
        self.rows = []
        mainLayout = QVBoxLayout()

        firstRow, firstTime = self.populate_row( "#18233e", "Manhattan", "m_train_logo.png", "M05N", 0)
        secondRow, secondTime = self.populate_row("#18233e", "Manhattan", "m_train_logo.png", "M05N", 1)

        mainLayout.addLayout(firstRow)
        mainLayout.addLayout(secondRow)
        

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(600, 200))
        self.rows.append(("M05N", 0, firstTime))
        self.rows.append(("M05N", 1, secondTime))
    
    def populate_row(self, color: str, text: str, image: str, stop: str, index: int):

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        containerLayout = QHBoxLayout()
        containerLayout.setContentsMargins(0,0,0,0)
        container.setLayout(containerLayout)

        palette = container.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        container.setAutoFillBackground(True)
        container.setPalette(palette)

        label = QLabel()
        pixmap = QPixmap(image)
        scaled = pixmap.scaled(
            95, 95,                             
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        label.setPixmap(scaled)
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        stationLabel = QLabel(text)
        stationLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        stationLabel.setContentsMargins(0,5,0,0)

        stationLabel.setStyleSheet("""
            font-family: "Arial";
            font-weight: 600;      /* Medium */
            font-size: 48px;
            color: white;
        """)
        updatedTime = str(arrivals_for_stop(stop)[index])
        timeLabel = QLabel(updatedTime)
        timeLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        timeLabel.setContentsMargins(0,0,20,0)

        timeLabel.setStyleSheet("""
            font-family: "Arial";
            font-weight: 600;     /* Bold */
            font-size: 64px;
            color: white;
        """)



        containerLayout.addWidget(label, 0, Qt.AlignmentFlag.AlignVCenter)
        containerLayout.addWidget(stationLabel, 1)
        containerLayout.addWidget(timeLabel, 0)

        row.addWidget(container)

        return row, timeLabel


class Color(QWidget):
    def __init__(self, color, text=''):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

        layout = QVBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)
        self.setLayout(layout)
        label.setStyleSheet('font: 30pt Helvetica; color: black;')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


