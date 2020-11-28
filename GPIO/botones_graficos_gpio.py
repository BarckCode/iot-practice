import tkinter
import RPi.GPIO as GPIO

# Tkinter start
w = tkinter.Tk()
fm = tkinter.Frame(w)
fm.grid(row=0, column=0)

# GPIO Conf
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)  # By default: off


# Commands
def off():
    print("Apagar")
    GPIO.output(2, GPIO.LOW)
    label.set("Apagado")


def on():
    print("Enceder")
    GPIO.output(2, GPIO.HIGH)
    label.set("Encendido")


# Buttons
button_1 = tkinter.Button(fm, text="Apagar", command=off)
button_1.grid(row=1, column=0, columnspan=2)
button_2 = tkinter.Button(fm, text="Encender", command=on)
button_2.grid(row=1, column=2, columnspan=2)


# Program Info
label = tkinter.StringVar()
label.set("Apagado")

lb = tkinter.Label(fm, textvariable=label)
lb.grid(row=2, column=0, columnspan=4)


w.mainloop()