import serial
import string
import time




ser = serial.Serial('COM30', 9600, timeout=1)


def set_temp(temp):
    # sets the temperature as temp
    ser.close()
    ser.open()
    nominal_temp_string = "$00E " + str(temp)+ " 0000.0 "+ "0000.0 "+ "0000.0 "+ "0000.0 "+ "0101010100000101"+ "\r\n"
    print (nominal_temp_string)
    ser.write(str.encode(nominal_temp_string))

    ser.close()


def stop_temp():
    ser.close()
    ser.open()
    nominal_temp_string = "$00E" +"\r\n"
    #print nominal_temp_string
    ser.write(nominal_temp_string)


def read_temp():
    ser.close()
    ser.open()
    ser.write("$00I\r\n")
    line = ser.readline()
    value = string.split(line, ' ')
    ser.close()
    return value[1]


set_temp('-027')
'''
while True:
    x = read_temp()
    print x
    if x >= '0026.9':
        stop_temp()
        break
'''