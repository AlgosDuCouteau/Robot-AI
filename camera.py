import sys
import cv2
import numpy as np

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_MainWindow

#https://ru.stackoverflow.com/a/1150993/396441

class Thread1(QtCore.QThread):
    changePixmap = QtCore.pyqtSignal(QtGui.QImage)
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.lower_hsv = np.array([0, 0, 0])
        self.upper_hsv = np.array([0, 0, 0])  # Changed to match UI default

    def run(self):
        self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap1.set(5, 60)
        while True:
            ret1, image1 = self.cap1.read()
            if ret1:
                hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
                
                # Show original image if all values are zero
                if np.all(self.lower_hsv == 0) and np.all(self.upper_hsv == 0):  # Changed condition
                    result = image1
                else:
                    # Create mask
                    mask = cv2.inRange(hsv, self.lower_hsv, self.upper_hsv)
                    
                    # Invert mask
                    mask_inv = cv2.bitwise_not(mask)
                    
                    # Black out the masked area in the original image
                    result = cv2.bitwise_and(image1, image1, mask=mask_inv)

                # Convert the result to RGB for display
                rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_format = QtGui.QImage.Format_RGB888
                p = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, qt_format)

                self.changePixmap.emit(p)

    def update_hsv_values(self, lower, upper):
        self.lower_hsv = np.array(lower)
        self.upper_hsv = np.array(upper)

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.thread1 = Thread1()
        self.thread1.changePixmap.connect(self.update_image)
        self.thread1.start()

        # Initialize labels with current slider values
        self.update_all_labels()

        # Connect sliders to update functions
        self.connect_sliders()

        # Connect color buttons to set_color functions
        self.ui.red.clicked.connect(lambda: self.set_color("red"))
        self.ui.yellow.clicked.connect(lambda: self.set_color("yellow"))
        self.ui.blue.clicked.connect(lambda: self.set_color("blue"))

    def update_image(self, qImg1):
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(qImg1))

    def update_all_labels(self):
        self.ui.value_h_upper.setText(str(self.ui.h_upper.value()))
        self.ui.value_s_upper.setText(str(self.ui.s_upper.value()))
        self.ui.value_v_upper.setText(str(self.ui.v_upper.value()))
        self.ui.value_h_lower.setText(str(self.ui.h_lower.value()))
        self.ui.value_s_lower.setText(str(self.ui.s_lower.value()))
        self.ui.value_v_lower.setText(str(self.ui.v_lower.value()))
        self.update_hsv_values()

    def connect_sliders(self):
        self.ui.h_upper.valueChanged.connect(self.update_h_upper)
        self.ui.s_upper.valueChanged.connect(self.update_s_upper)
        self.ui.v_upper.valueChanged.connect(self.update_v_upper)
        self.ui.h_lower.valueChanged.connect(self.update_h_lower)
        self.ui.s_lower.valueChanged.connect(self.update_s_lower)
        self.ui.v_lower.valueChanged.connect(self.update_v_lower)

    def update_h_upper(self, value):
        self.ui.value_h_upper.setText(str(value))
        if value < self.ui.h_lower.value():
            self.ui.h_lower.setValue(value)
        self.update_hsv_values()

    def update_s_upper(self, value):
        self.ui.value_s_upper.setText(str(value))
        if value < self.ui.s_lower.value():
            self.ui.s_lower.setValue(value)
        self.update_hsv_values()

    def update_v_upper(self, value):
        self.ui.value_v_upper.setText(str(value))
        if value < self.ui.v_lower.value():
            self.ui.v_lower.setValue(value)
        self.update_hsv_values()

    def update_h_lower(self, value):
        self.ui.value_h_lower.setText(str(value))
        if value > self.ui.h_upper.value():
            self.ui.h_upper.setValue(value)
        self.update_hsv_values()

    def update_s_lower(self, value):
        self.ui.value_s_lower.setText(str(value))
        if value > self.ui.s_upper.value():
            self.ui.s_upper.setValue(value)
        self.update_hsv_values()

    def update_v_lower(self, value):
        self.ui.value_v_lower.setText(str(value))
        if value > self.ui.v_upper.value():
            self.ui.v_upper.setValue(value)
        self.update_hsv_values()

    def update_hsv_values(self):
        lower = [
            self.ui.h_lower.value(),
            self.ui.s_lower.value(),
            self.ui.v_lower.value()
        ]
        upper = [
            self.ui.h_upper.value(),
            self.ui.s_upper.value(),
            self.ui.v_upper.value()
        ]
        self.thread1.update_hsv_values(lower, upper)

    def set_color(self, color):
        if color == "red":
            lower = [0, 100, 100]
            upper = [10, 255, 255]
        elif color == "yellow":
            lower = [20, 100, 100]
            upper = [30, 255, 255]
        elif color == "blue":
            lower = [100, 100, 100]
            upper = [130, 255, 255]
        else:
            return

        # Set upper values first to avoid conflicts
        self.ui.h_upper.setValue(upper[0])
        self.ui.s_upper.setValue(upper[1])
        self.ui.v_upper.setValue(upper[2])
        
        # Then set lower values
        self.ui.h_lower.setValue(lower[0])
        self.ui.s_lower.setValue(lower[1])
        self.ui.v_lower.setValue(lower[2])

        self.update_hsv_values()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
