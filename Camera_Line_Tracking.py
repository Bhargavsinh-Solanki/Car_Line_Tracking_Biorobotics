import time
from picamera.array import PiRGBArray # Generates a 3D RGB array
from picamera import PiCamera # Provides a Python interface for the RPi Camera Module
import time # Provides time-related functions
import cv2 # OpenCV library
import numpy as np
from Motor import *
import RPi.GPIO as GPIO
class Line_Tracking:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
    def run(self):
        left_circum_engaged = False
        # left_circum_counter = 0
        right_circum_engaged = False
        # right_circum_counter = 0
        straight_engaged = False
        straight_counter = 0
        counter_IR01 = 0
        counter_IR02 = 0
        counter_IR03 = 0


        
        while True:
            self.LMR=0x00
            if GPIO.input(self.IR01)==True:
                self.LMR=(self.LMR | 4)
            if GPIO.input(self.IR02)==True:
                self.LMR=(self.LMR | 2)
            if GPIO.input(self.IR03)==True:
                self.LMR=(self.LMR | 1)

            # abhi
            # Straight
            if self.LMR==2 or self.LMR==5:
                if counter_IR01 > 0:
                    counter_IR02 += 1
                    counter_IR03 = 0
                if counter_IR03 > 0:
                    counter_IR02 += 1
                    counter_IR01 = 0
                PWM.setMotorModel(2200,2200,2200,2200)

            # left
            elif self.LMR==4:
                counter_IR01 += 1
                if counter_IR01 > 10 and counter_IR02 > 10:
                        left_circum_engaged = True
                        counter_IR01 = 0
                        counter_IR02 = 0
                        counter_IR03 = 0
                        print("Left Circum Engaged!")
                        if right_circum_engaged:
                            right_circum_engaged = False
                if left_circum_engaged:
                    counter_IR03 = 0
                    counter_IR02 = 0
                    counter_IR01 = 0
                    if right_circum_engaged:
                            right_circum_engaged = False
                    print("turning left with Circum Engaged")
                    PWM.setMotorModel(0, 0, 5000, 5000)
                else:
                    print("turning left WITHOUT Circum Engaged")
                    PWM.setMotorModel(-4000,-4000, 4000, 4000)

            # right
            elif self.LMR==1:

                counter_IR03 += 1
                if counter_IR03 > 10 and counter_IR02 > 10:
                        right_circum_engaged = True
                        counter_IR03 = 0
                        counter_IR02 = 0
                        counter_IR01 = 0
                        print("Right Circum Engaged!")
                        if left_circum_engaged:
                            left_circum_engaged = False
                if right_circum_engaged:
                    counter_IR03 = 0
                    counter_IR02 = 0
                    counter_IR01 = 0
                    if left_circum_engaged:
                            left_circum_engaged = False
                    print("turning right with Circum Engaged")
                    PWM.setMotorModel(5000, 5000, 0, 0)
                else:
                    print("turning right WITHOUT Circum Engaged")
                    PWM.setMotorModel(4000, 4000, -4000, -4000)

            # right strong
            elif self.LMR==3:

                left_circum_engaged = False
                right_circum_engaged = False
                counter_IR01 = 0
                counter_IR02 = 0
                counter_IR03 = 0
                print("strong RIGHT turn => circums DISENGAGED")
                PWM.setMotorModel(8000,8000,-4000,-4000)

            # left strong
            elif self.LMR==6:
                left_circum_engaged = False
                right_circum_engaged = False
                counter_IR01 = 0
                counter_IR02 = 0
                counter_IR03 = 0
                print("strong LEFT turn <= circums DISENGAGED")
                PWM.setMotorModel(-4000,-4000,8000,8000)

            elif self.LMR==7:
                pass

            # if self.LMR==2:
            #  PWM.setMotorModel(2250,2250,2250,2250)
            # elif self.LMR==4:
            #  PWM.setMotorModel(0, 0,3000,3000)
            # elif self.LMR==6:
            #  PWM.setMotorModel(-4000,-4000,8000,8000)
            # elif self.LMR==1:
            #  PWM.setMotorModel(3000,3000,0,0)
            # elif self.LMR==3:
            #  PWM.setMotorModel(8000,8000,-4000,-4000)
            # elif self.LMR==7:
            #  pass
            #  #PWM.setMotorModel(0,0,0,0)
    def get_feed(self):
        # Initialize the camera
        camera = PiCamera()
         
        # Set the camera resolution
        camera.resolution = (640, 480)
         
        # Set the number of frames per second
        camera.framerate = 32
         
        # Generates a 3D RGB array and stores it in rawCapture
        raw_capture = PiRGBArray(camera, size=(640, 480))
         
        # Wait a certain number of seconds to allow the camera time to warmup
        time.sleep(0.1)
         
        # Capture frames continuously from the camera
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
             
            # Grab the raw NumPy array representing the image
            image = frame.array
             
            # Display the frame using OpenCV
            cv2.imshow("Frame", image)
             
            # Wait for keyPress for 1 millisecond
            key = cv2.waitKey(1) & 0xFF
             
            # Clear the stream in preparation for the next frame
            raw_capture.truncate(0)
             
            # If the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

    def get_video(self):
        val = 1200
        cap = cv2.VideoCapture(-1)
        cap.set(3, 160)
        cap.set(4, 120)
        while True:
            ret, frame = cap.read()
            crop_img = frame[60:120, 0:160]
            gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),0)
            ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
            contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

            # low_b = np.uint8([5,5,5])
            # high_b = np.uint8([0,0,0])
            # mask = cv2.inRange(frame, high_b, low_b)
            # contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
            if len(contours) > 0 :
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)
                if M["m00"] !=0 :
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    if cx >= 120 :
                        print("Turn Left")
                        PWM.setMotorModel(val, val, -val, -val)
                    if cx < 120 and cx > 50 :
                        print("On Track!")
                        PWM.setMotorModel(val,val,val,val)
                    if cx <=50 :
                        print("Turn Right")
                        PWM.setMotorModel(-val, -val, val, val)
            else :
                print("No line")
            if cv2.waitKey(1) & 0xff == ord('q'):   # 1 is the time in ms
                PWM.setMotorModel(0, 0, 0, 0)
                break
        cap.release()
        cv2.destroyAllWindows()



infrared=Line_Tracking()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.get_video()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
        PWM.setMotorModel(0,0,0,0)