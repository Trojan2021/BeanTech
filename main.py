import RPi.GPIO as GPIO
import time
import serial
import sys
import keyboard


# Desired temp for Room 1
desiredTemp = float(sys.argv[1])
outsideTemp = float(sys.argv[2])
case = int(sys.argv[3])

# Define the serial port and baud rate.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Setup proper board type
GPIO.setmode(GPIO.BCM)


# ON OFF CONTROLS
# Air conditioning, heaters, and middle fan power

# Set the GPIO pin values
r1ac = 22
r1h1 = 23
r1h2 = 25
r2ac = 6
r2h1 = 5
r2h2 = 12
mfp = 17

# GPIO setup
GPIO.setup(r1ac, GPIO.OUT)
GPIO.setup(r1h1, GPIO.OUT)
GPIO.setup(r1h2, GPIO.OUT)
GPIO.setup(r2ac, GPIO.OUT)
GPIO.setup(r2h1, GPIO.OUT)
GPIO.setup(r2h2, GPIO.OUT)
GPIO.setup(mfp, GPIO.OUT)



# SERVO CONTROL
# Windows and middle flap

# Set the GPIO pin values
r1w = 27
r2w = 21
mfs = 18

# Set the PWM frequency to 50 Hz
pwm_frequency = 50

# Set the duty cycle range (in percent) for the servo motor
duty_cycle_min = 2
duty_cycle_max = 12

# Setup the GPIO pin as a PWM output
GPIO.setup(r1w, GPIO.OUT)
GPIO.setup(r2w, GPIO.OUT)
GPIO.setup(mfs, GPIO.OUT)
r1wpwm = GPIO.PWM(r1w, pwm_frequency)
r2wpwm = GPIO.PWM(r2w, pwm_frequency)
mfspwm = GPIO.PWM(mfs, pwm_frequency)

# Start the PWM output with a 0% duty cycle
r1wpwm.start(0)
r2wpwm.start(0)
mfspwm.start(0)

# Function to set the servo position
def set_servo_position(pwm, angle):
    duty_cycle = ((angle / 180) * (duty_cycle_max - duty_cycle_min)) + duty_cycle_min
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    
# Variables
# For state variables, True is open/on
r1wState = False
r1acState = False
r1hState = False
r2wState = False
r2acState = False
r2hState = False
mfpState = False
mfsState = False


stop_loop = False

try:
    data = ser.readline().decode('utf-8').rstrip()
except UnicodeDecodeError as e:
    pass
    
while not stop_loop:
    
    r1wState = False
    r1acState = False
    r1hState = False
    r2wState = False
    r2acState = False
    r2hState = False
    mfpState = False
    mfsState = False
    
    try:
        data = ser.readline().decode('utf-8').rstrip()
        values = data.split(",")
        Room1temp = float(values[0])
        Room2temp = float(values[1])
        Room1Light = float(values[2])
        Room2Light = float(values[3])
        Rotary = float(values[4])
        
    except UnicodeDecodeError as e:
        pass
    
    # Goal: Get Room 1 Cold
    # if Room 1 Warm:
    # if desiredTemp < Room1temp:
    if case == 1:
    #     Turn on AC
        r1acState = True
    #     Check Room 2
    #     Check Outside
    #     if Room 2 Warm && Outside Warm:
    #     if Room2temp > desiredTemp and outsideTemp > desiredTemp:
    # #         if Room 1 Window Open:
    #         if r1wState:
    # #             Close
    #             r1wState = False
    # #         if Middle Fan Open:
    #         if mfpState:
    # #             Close
    #             mfpState = False
    #             mfsState = False
    #     else if Room 2 Cold && Outside Warm:
        if Room2temp <= desiredTemp and outsideTemp > desiredTemp:
    #         if Room 1 Window Open:
    #         if r1wState:
    # #             Close
    #             r1wState = False
    # #         if Middle Fan Close:
            # if not mfpState:
    #             Open
            mfsState = True
            mfpState = True
    #     else if Outside Cold:
        elif outsideTemp < desiredTemp:
    #         if Room 1 Window Close:
            # if not r1wState:
    #             Open
            r1wState = True
    #         if Middle Fan Open:
    #         if mfpState:
    # #             Close
    #             mfpState = False
    #             mfsState = False
    # else:
    # else:
    # #     if Middle Fan Open:
    #     if mfpState:
    # #         Close
    #         mfpState = False
    #         mfsState = False
    # #     if Room 1 Window Open:
    #     if r1wState:
    # #         Close
    #         r1wState = False
            
    # Goal: Get Room 2 Cold
    # if Room2temp > desiredTemp:
    if case == 2:
        # Turn on AC
        r2acState = True
        # Check Room 1
        # Check Outside
        # if Room1temp > desiredTemp and outsideTemp > desiredTemp:
        #     # if Room 2 Window Open:
        #     if r2wState:
        #         # Close
        #         r2wState = False
        #     # if Middle Fan Open:
        #     if mfpState:
        #         # Close
        #         mfpState = False
        #         mfsState = False
        # else if Room 1 Cold && Outside Warm:
        if Room1temp <= desiredTemp and outsideTemp > desiredTemp:
            # if Room 2 Window Open:
            # if r2wState:
            #     # Close
            #     r2wState = False
            # if Middle Fan Close:
            # if not mfpState:
            #     # Open
            mfsState = True
            mfpState = True
        # else if Outside Cold:
        # elif outsideTemp < desiredTemp:
        #     # if Room 2 Window Close:
        #     if r2wState:
        #         # Open
        #         r2wState = False
        #     # if Middle Fan Open:
        #     if mfpState:
        #         # Close
        #         mfpState = False
        #         mfsState = False
    # else:
    # else:
    #     # if Middle Fan Open:
    #     if mfpState:
    #         # Close
    #         mfpState = False
    #         mfsState = False
    #     # if Room 2 Window Open:
    #     if r2wState:
    #         # Close
    #         r2wState = False


    # Goal: Get Room 1 Warm
    # elif Room1temp < desiredTemp:
    if case == 3:
        # Check Room 2
        # Check Outside
        # Turn on heaters in room 1
        r1hState = True

        # If Sunlight and Room 1 Slightly Cold and Outside Warm
        if Room1Light > 600 and (Room1temp < desiredTemp - 2 and Room1temp > desiredTemp - 5) and outsideTemp > desiredTemp:
            # If Room 1 Window Close
            # if not r1wState:
            #     # Open
            r1wState = True
            # If Middle Fan Open
            # if mfpState:
            #     # Close
            #     mfpState = False
            #     mfsState = False
        else:
            # If Room 2 Cold and Outside Cold
            # if Room2temp <= desiredTemp and outsideTemp <= desiredTemp:
            #     # If Room 1 Window Open
            #     if r1wState:
            #         # Close
            #         r1wState = False
            #     # If Middle Fan Open
            #     if mfpState:
            #         # Close
            #         mfpState = False
            #         mfsState = False
            # Else if Room 2 Warm and Outside Cold
            if Room2temp > desiredTemp and outsideTemp <= desiredTemp:
                # # If Room 1 Window Open
                # if r1wState:
                #     # Close
                #     r1wState = False
                # # If Middle Fan Close
                # if not mfpState:
                #     # Open
                mfsState = True
                mfpState = True
            # Else if Outside Warm
            elif outsideTemp > desiredTemp:
                # If Room 1 Window Close
                # if not r1wState:
                    # Open
                r1wState = True
                # If Middle Fan Open
                # if mfpState:
                #     # Close
                #     mfpState = False
                #     mfsState = False
    # else:
    #     # If Middle Fan Open
    #     if mfpState:
    #         # Close
    #         mfpState = False
    #         mfsState = False
    #     # If Room 1 Window Open
    #     if r1wState:
    #         # Close
    #         r1wState = False

    # Goal: Get Room 2 Warm

    # If Room 2 is Cold:
    # elif Room2temp < desiredTemp:
    if case == 4:

        # Check Room 1 and Outside temperature
        # Check Room 1
        # Check Outside
        r2hState = True

        # If Sunlight is present and Room 2 is slightly cold and Outside is Warm
        if Room2Light > 600 and (Room2temp < desiredTemp - 2 and Room2temp > desiredTemp - 5) and outsideTemp > desiredTemp:

            # # If Room 2 window is open, close it
            # if r2wState:
            r2wState = True

            # # If Middle fan is open, close it
            # if mfpState:
            #     mfpState = False
            #     mfsState = False

        else:

            # # If Room 1 is Cold and Outside is Cold
            # if Room1temp < desiredTemp and outsideTemp < desiredTemp:

            #     # If Room 2 window is open, close it
            #     if r2wState:
            #         r2wState = False

            #     # If Middle fan is open, close it
            #     if mfpState:
            #         mfpState = False
            #         mfsState = False

            #     # Turn on Heaters in Room 2
            #     r2hState = True

            # If Room 1 is Warm and Outside is Cold
            if Room1temp >= desiredTemp and outsideTemp < desiredTemp:

                # # If Room 2 window is open, close it
                # if r2wState:
                #     r2wState = False

                # If Middle fan is closed, open it
                # if not mfpState:
                mfpState = True
                mfsState = True

            # If Outside is Warm
            elif outsideTemp >= desiredTemp:

                # If Room 2 window is closed, open it
                # if not r2wState:
                r2wState = True

                # # If Middle fan is open, close it
                # if mfpState:
                #     mfpState = False
                #     mfsState = False

        # If Room 2 is not Cold anymore, turn off Heaters in Room 2
        # r2hState = False

    if case == 7:
        #Cool down house at night by creating draft
        r1wState = True
        r2wState = True
        mfsState = True
        mfpState = True
        
    if case == 8:
        # Open the windows for a nice morning
        r1wState = True
        r2wState = True
        
    if case == 9:
        # Warm room 2, outside is cold and room 1 is warmer than room 2
        mfsState = True
        mfpState = True
        
    if case == 10:
        mfpState = True
        r2wState = True
        
        



    # Check for a key event to stop the loop
    if keyboard.is_pressed('q'):
        stop_loop = True
        
    
    # Servos
    if r1wState:
        set_servo_position(r1wpwm, 180)
    else:
        set_servo_position(r1wpwm, 0)
    if r2wState:
        set_servo_position(r2wpwm, 180)
    else:
        set_servo_position(r2wpwm, 0)
    if mfsState:
        set_servo_position(mfspwm, 0)
    else:
        set_servo_position(mfspwm, 180)
        
    # ON/OFF
    if r1acState:
        GPIO.output(r1ac, 1)
    else:
        GPIO.output(r1ac, 0)
    if mfpState:
        GPIO.output(mfp, 1)
    else:
        GPIO.output(mfp, 0)
    if r1hState:
        GPIO.output(r1h1, 1)
        GPIO.output(r1h2, 1)
    else:
        GPIO.output(r1h1, 0)
        GPIO.output(r1h2, 0)
    if r2hState:
        GPIO.output(r2h1, 1)
        GPIO.output(r2h2, 1)
    else:
        GPIO.output(r2h1, 0)
        GPIO.output(r2h2, 0)
    if r2acState:
        GPIO.output(r2ac, 1)
    else:
        GPIO.output(r2ac, 0)
        
    time.sleep(1)
        
    



# Cleanup the GPIO pins
r1wpwm.stop()
r2wpwm.stop()
mfspwm.stop()
GPIO.cleanup()
ser.close()