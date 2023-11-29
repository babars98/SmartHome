import RPi.GPIO as GPIO
import config

def set_mode(server_res, current_state):
    
    cnfg = config.getconfig()
    fan_GPIO_pin = int(cnfg.get('client', 'FanGPIOPin'))
    
    #if fan is already on and server response is false then turn in off
    if (current_state == True and server_res == False):
        turn_off_fan(fan_GPIO_pin)
        return False
    
    elif (current_state == False and server_res == True):
        turn_fan_on(fan_GPIO_pin)
        return True
        
    return current_state

def turn_fan_on(GPIO_pin):
    
    set_GPIO(GPIO_pin)
    
    GPIO.output(GPIO_pin, GPIO.HIGH)
    print("Fan on")

def turn_off_fan(GPIO_pin):

    set_GPIO(GPIO_pin)
    GPIO.output(GPIO_pin, GPIO.LOW)
    print("Fan off")

def set_GPIO(pin_no):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_no, GPIO.OUT)
    