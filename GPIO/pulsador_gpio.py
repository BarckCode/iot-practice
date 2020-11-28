import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(20, GPIO.IN)


''' Encender el LED mientras se mantenga pulsado el interruptor.
try:
    while True:
        if GPIO.input(20) == GPIO.HIGH:
            GPIO.output(2, GPIO.HIGH)
        else:
            GPIO.output(2, GPIO.LOW)
except:
    GPIO.cleanup()
    print("Fin de programa")
'''

# Lo mismo pero con menos codigo.
try:
    while True:
        GPIO.output(2, GPIO.input(20))
except:
    GPIO.cleanup()
    print("Fin de programa")
