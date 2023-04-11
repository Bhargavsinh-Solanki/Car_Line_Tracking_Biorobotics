import time
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
            #print(self.LMR)
            # if self.LMR==2 or self.LMR==5:
            #     # Straight
            #     print("Straight")
            #     if left_circum_counter > 0:
            #             left_circum_counter += 1
            #     if right_circum_counter > 0:
            #             right_circum_counter += 1
            #     PWM.setMotorModel(2200,2200,2200,2200)
            # elif self.LMR==4:
            #     # Turn Left
            #     print("Left")
            #     left_circum_counter += 1
            #     if left_circum_counter == 3:
            #         # Circumference Engaged
            #         left_circum_engaged = True
            #         left_circum_counter = 0
            #         print("Left Circum Engaged!")

            #     if left_circum_engaged:
            #         PWM.setMotorModel(-800, -800, 3000, 3000)
            #     else:
            #         PWM.setMotorModel(-3000,-2000, 1000, 3000)
            # elif self.LMR==6:
            #     # Turn Left Tez
            #     print("Left Tez")
            #     if right_circum_engaged:
            #         right_circum_engaged = False
            #         print("Right Circum Disengaged!")
            #     if left_circum_engaged:
            #         left_circum_engaged = False
            #         print("Left Circum Disengaged!")

            #     PWM.setMotorModel(-4000, -4000, 4000, 4000)
            #     # PWM.setMotorModel(-4000, -4000, 8000, 8000)
            # elif self.LMR==1:
            #     # Turn Right
            #     print("Right")

            #     right_circum_counter += 1
            #     if right_circum_counter == 3:
            #         # Circumference Engaged
            #         right_circum_engaged = True
            #         right_circum_counter = 0
            #         print("Right Circum Engaged!")

            #     if right_circum_engaged:
            #         PWM.setMotorModel(3000, 3000, -800, -800)
            #     else:
            #         PWM.setMotorModel(1000,3000, -3000, -2000)
            #     # PWM.setMotorModel(3200,3200, -2200, -2200)
            # elif self.LMR==3:
            #     # Turn Right Tezz
            #     print("Right Tez")
            #     if left_circum_engaged:
            #         left_circum_engaged = False
            #         print("Left Circum Disengaged!")
            #     if right_circum_engaged:
            #         right_circum_engaged = False
            #         print("Right Circum Disengaged!")

            #     PWM.setMotorModel(4000, 4000,-4000, -4000)
            #     # PWM.setMotorModel(8000, 8000,-4000, 4000)
            # elif self.LMR==7:
            #     pass
            #     # PWM.setMotorModel(0,0,0,0)

            # abhi
            # Straight
            # if self.LMR==2 or self.LMR==5:
            #     if counter_IR01 > 0:
            #         counter_IR02 += 1
            #         counter_IR03 = 0
            #     if counter_IR03 > 0:
            #         counter_IR02 += 1
            #         counter_IR01 = 0
            #     PWM.setMotorModel(2200,2200,2200,2200)

            # # left
            # elif self.LMR==4:
            #     counter_IR01 += 1
            #     if counter_IR01 > 15 and counter_IR02 > 15:
            #             left_circum_engaged = True
            #             counter_IR01 = 0
            #             counter_IR02 = 0
            #             print("Left Circum Engaged!")
            #             if right_circum_engaged:
            #                 right_circum_engaged = False
            #     if left_circum_engaged:
            #         print("turning left with Circum Engaged")
            #         PWM.setMotorModel(-1000, -1000, 4000, 4000)
            #     else:
            #         print("turning left WITHOUT Circum Engaged")
            #         PWM.setMotorModel(-4000,-4000, 4000, 4000)

            # # right
            # elif self.LMR==1:

            #     counter_IR03 += 1
            #     if counter_IR03 > 15 and counter_IR02 > 15:
            #             right_circum_engaged = True
            #             counter_IR03 = 0
            #             counter_IR02 = 0
            #             print("Right Circum Engaged!")
            #             if left_circum_engaged:
            #                 left_circum_engaged = False
            #     if right_circum_engaged:
            #         print("turning right with Circum Engaged")
            #         PWM.setMotorModel(4000, 4000, -800, -800)
            #     else:
            #         print("turning right WITHOUT Circum Engaged")
            #         PWM.setMotorModel(4000, 4000, -4000, -4000)

            # # right strong
            # elif self.LMR==3:

            #     left_circum_engaged = False
            #     right_circum_engaged = False
            #     counter_IR01 = 0
            #     counter_IR02 = 0
            #     counter_IR03 = 0
            #     print("strong RIGHT turn => circums DISENGAGED")
            #     PWM.setMotorModel(8000,8000,-4000,-4000)

            # # left strong
            # elif self.LMR==6:
            #     left_circum_engaged = False
            #     right_circum_engaged = False
            #     counter_IR01 = 0
            #     counter_IR02 = 0
            #     counter_IR03 = 0
            #     print("strong LEFT turn <= circums DISENGAGED")
            #     PWM.setMotorModel(-4000,-4000,8000,8000)

            # elif self.LMR==7:
            #     pass

            if self.LMR==2:
             PWM.setMotorModel(2150,2150,2150,2150)
            elif self.LMR==4:
             PWM.setMotorModel(-3500, -3500,6000,6000)
            elif self.LMR==6:
             PWM.setMotorModel(1000,1000,3000,3000)
            elif self.LMR==1:
             PWM.setMotorModel(6000,6000,-3500,-3500)
            elif self.LMR==3:
             PWM.setMotorModel(3000,3000,1000,1000)
            elif self.LMR==7:
             pass
             #PWM.setMotorModel(0,0,0,0)

            
infrared=Line_Tracking()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
        PWM.setMotorModel(0,0,0,0)