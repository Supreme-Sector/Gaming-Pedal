import serial, pyautogui, time

#throw() launches throwable and quickly switches back to gun
def throw():
    pyautogui.mouseUp() #Release the mouse in case it is being held down

    #Press 4 for 0.01 seconds
    pyautogui.keyDown('4')
    time.sleep(0.01)
    pyautogui.keyUp('4')

    pyautogui.mouseDown() #Use throwable without launching yet
    while True:
        data = ser.read(1)
        if data == b'R':
            pyautogui.mouseUp() #Launch throwable when pedal is released
            break

    #Switch back to gun in the first slot
    pyautogui.keyDown('1')
    time.sleep(0.01)
    pyautogui.keyUp('1')


#Serial object listening on arduino COM port; baud rate set to 9600
ser = serial.Serial('COM3',9600)

#Wait for 5 seconds to open game
time.sleep(5)

while ser.isOpen():
    data=ser.read(1) #Read a byte
    if data == b'P':
        throw() #If pedal is pressed, throw() is called
