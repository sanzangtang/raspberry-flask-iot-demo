import RPi.GPIO as gpio

class Led():
    def __init__(self, pin):
        self.pin = pin
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)

    def turn_on(self):
        gpio.output(self.pin, gpio.HIGH)

    def turn_off(self):
        gpio.output(self.pin, gpio.LOW)
