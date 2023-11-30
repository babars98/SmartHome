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

