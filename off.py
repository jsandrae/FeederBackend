import serial

def turn_off():
    port = "/dev/ttyACM0"
    Arduino = serial.Serial(port,9600)
    Arduino.flushInput()
    str = "f"
    print str
    Arduino.write(str)
