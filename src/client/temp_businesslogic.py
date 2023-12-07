import gpio
import config

def set_mode(server_res, current_state):
    
    cnfg = config.getconfig()
    fan_GPIO_pin = int(cnfg.get('client', 'FanGPIOPin'))
    
    #if fan is already on and server response is false then turn in off
    if (current_state == True and server_res == False):
        gpio.turn_off(fan_GPIO_pin)
        print('Fan OFF')
        return False
    
    elif (current_state == False and server_res == True):
        gpio.turn_on(fan_GPIO_pin)
        print('Fan ON')
        return True
        
    return current_state

def check_temp_level(temprature):
    
    cnfg = config.getconfig()
    temprature_limit = int(cnfg.get('client', 'hightemp'))
    flag = False
    
    if temprature > temprature_limit:
        flag = True
        
    #else if temprature is less than 25C turn off the fan and return False.
    elif temprature < temprature_limit:
        flag = False  
    
    else:
        flag = False
        
    return flag