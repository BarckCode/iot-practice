import serial

s = serial.Serial("/dev/ttyACM0", 9600)

try:
    while True:
        dato = s.readline()
        print(type(dato), dato)
except:
    s.close()
    print("Fin del programa")