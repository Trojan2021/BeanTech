import serial
import keyboard

ser = serial.Serial('/dev/ttyACM0', 9600)

count = 0

while True:
    if keyboard.is_pressed('space'):
        print('Spacebar pressed!')
        # Do something after the keypress, like break out of a loop
        break
    data = ser.readline().decode('utf-8').rstrip()
    print(data)
    count += 1   
ser.close()


