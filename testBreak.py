import keyboard

# Set up a flag to indicate when to stop the loop
stop_loop = False

# Loop until the flag is set to True
while not stop_loop:
    # Do something in the loop
    
    # Check for a key event to stop the loop
    if keyboard.is_pressed('q'):
        stop_loop = True
