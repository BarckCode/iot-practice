import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)

    validation = True
    while validation:
        data = input("Indica una orden de control: ")
        if data == "a":
            GPIO.output(2, GPIO.HIGH)
        elif data == "b":
            GPIO.output(2, GPIO.LOW)
        elif data == "z":
            validation = False


if __name__ == '__main__':
    print("Inicio del programa")
    main()
    GPIO.cleanup()
    print("Fin del programa")
