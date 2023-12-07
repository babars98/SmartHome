import config
import gpio

def set_mode(server_res, current_state):
    
    cnfg = config.getconfig()
    light_GPIO_pin = int(cnfg.get('client', 'LightGPIOPin'))
    
    #if fan is already on and server response is false then turn in off
    if (current_state == True and server_res == False):
        gpio.turn_off(light_GPIO_pin)
        print('Light OFF')
        return False
    
    elif (current_state == False and server_res == True):
        gpio.turn_on(light_GPIO_pin)
        print('Light ON')
        return True
        
    return current_state

def check_light_level(lightdata):
    cnfg = config.getconfig()
    bright_light = int(cnfg.get('client', 'brightLight'))
    low_light = int(cnfg.get('client', 'lowLight'))

    #if it is dark then return status True.
    if lightdata == low_light:
        return True
    
    #else if it is clear return false
    elif lightdata == bright_light:
        return False
    
    #else return the current state
    else:
        return False
