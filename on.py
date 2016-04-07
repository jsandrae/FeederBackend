import serial

def turn_on():
    port = "/dev/ttyACM0"
    Arduino = serial.Serial(port,9600)
    Arduino.flushInput()
    str = "n"
    print str
    Arduino.write(str)
