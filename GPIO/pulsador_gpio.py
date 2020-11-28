import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

try:
    while True:
        if GPIO.input(20) == GPIO.HIGH:
            GPIO.output(2, GPIO.HIGH)
        else:
            GPIO.output(20, GPIO.LOW)
except:
    GPIO.cleanup()
    print("Fin de programa")
