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
        self.lower_hsv = np.array([80, 100, 100])
        self.upper_hsv = np.array([130, 255, 255])
        self.PIXELS_PER_CM = 400 / 30.8
        self.OBJECT_DIAMETER_CM = 4.0
        self.show_coordinates = False
        
    def calculate_distance(self, pixel_diameter):
        # Direct conversion using pixels per cm
        distance_cm = pixel_diameter / self.PIXELS_PER_CM
        return distance_cm

    def run(self):
        self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap1.set(5, 60)
        
        # Get camera parameters
        frame_width = self.cap1.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = self.cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
        origin_x = frame_width / 2 - 5  # Origin X at center
        origin_y = 47  # Origin Y at top
        
        while True:
            ret1, image1 = self.cap1.read()
            if ret1:
                result = image1.copy()
                
                # Only draw origin and axes if coordinates should be shown
                if self.show_coordinates:
                    # Draw origin point
                    cv2.circle(result, (int(origin_x), int(origin_y)), 5, (0, 0, 255), -1)
                    
                    # Draw X axis with arrow
                    cv2.line(result, (int(origin_x), int(origin_y)), (int(origin_x), int(origin_y + 50)), (0, 0, 255), 2)
                    pts_x = np.array([[int(origin_x), int(origin_y + 50)],
                                    [int(origin_x - 5), int(origin_y + 40)],
                                    [int(origin_x + 5), int(origin_y + 40)]], np.int32)
                    cv2.fillPoly(result, [pts_x], (0, 0, 255))
                    cv2.putText(result, "X", (int(origin_x) - 20, int(origin_y + 70)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    
                    # Draw Y axis with arrow
                    cv2.line(result, (int(origin_x), int(origin_y)), (int(origin_x + 50), int(origin_y)), (0, 0, 255), 2)
                    pts_y = np.array([[int(origin_x + 50), int(origin_y)],
                                    [int(origin_x + 40), int(origin_y - 5)],
                                    [int(origin_x + 40), int(origin_y + 5)]], np.int32)
                    cv2.fillPoly(result, [pts_y], (0, 0, 255))
                    cv2.putText(result, "Y", (int(origin_x + 70), int(origin_y) + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, self.lower_hsv, self.upper_hsv)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 1000:
                        cv2.drawContours(result, [contour], -1, (0, 0, 255), 2)
                        M = cv2.moments(contour)
                        if M["m00"] != 0:
                            cx = int(M["m10"] / M["m00"])
                            cy = int(M["m01"] / M["m00"])
                            
                            # Draw center point
                            cv2.circle(result, (cx, cy), 5, (0, 255, 0), -1)
                            
                            # Only show coordinates if enabled
                            if self.show_coordinates:
                                x_distance_cm = cy / self.PIXELS_PER_CM + 8
                                y_distance_cm = (cx - origin_x) / self.PIXELS_PER_CM + 1
                                
                                # Draw coordinates at bottom-left
                                coord_text = f"X: {x_distance_cm:.1f}cm Y: {y_distance_cm:.1f}cm"
                                
                                # Draw black background
                                cv2.rectangle(result, 
                                            (10, int(frame_height) - 40), 
                                            (250, int(frame_height) - 10),
                                            (0, 0, 0), 
                                            -1)
                                
                                # Draw the text
                                cv2.putText(result, 
                                          coord_text,
                                          (20, int(frame_height) - 20),
                                          cv2.FONT_HERSHEY_SIMPLEX, 
                                          0.6,
                                          (255, 255, 255),
                                          2)

                # Convert and emit image
                rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_format = QtGui.QImage.Format_RGB888
                p = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, qt_format)
                self.changePixmap.emit(p)

    def update_hsv_values(self, lower, upper):
        self.lower_hsv = np.array(lower)
        self.upper_hsv = np.array(upper)
        self.show_coordinates = True

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
        # Reset coordinate display
        self.thread1.show_coordinates = False
        
        if color == "red":
            lower = [0, 100, 100]
            upper = [10, 255, 255]
        elif color == "yellow":
            lower = [20, 100, 100]
            upper = [30, 255, 255]
        elif color == "blue":
            lower = [80, 100, 100]
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
