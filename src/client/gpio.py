import RPi.GPIO as GPIO

def turn_on(GPIO_pin):
    
    set_GPIO(GPIO_pin) 
    GPIO.output(GPIO_pin, GPIO.HIGH)


def turn_off(GPIO_pin):

    set_GPIO(GPIO_pin)
    GPIO.output(GPIO_pin, GPIO.LOW)

def set_GPIO(pin_no):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_no, GPIO.OUT)