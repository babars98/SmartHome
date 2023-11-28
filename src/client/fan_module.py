import RPi.GPIO as GPIO
import config

def set_mode(server_res, current_state):
    
    #if fan is already on and server response is false then turn in off
    if (current_state == True and server_res == False):
        turn_off_fan()
        return False
    
    elif (current_state == False and server_res == True):
        turn_fan_on()
        return True
        
    return current_state

def turn_fan_on():
    
    cnfg = config.getconfig()
    fan_GPIO_pin = cnfg.get('client', 'FanGPIOPin')
    set_GPIO(fan_GPIO_pin)
    
    GPIO.output(fan_GPIO_pin, GPIO.HIGH)
    print("Fan on")

def turn_off_fan():
    fan_GPIO_pin = config.getconfig()
    set_GPIO(fan_GPIO_pin)
    GPIO.output(12,GPIO.LOW)
    print("Fan off")

def set_GPIO(pin_no):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_no, GPIO.OUT)
    