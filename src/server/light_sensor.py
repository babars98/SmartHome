from datetime import datetime
import api_handler

def process_light_sensor(light_data, is_on, config):
    
    #construct api url with query string parameters
    url = construct_api_url(config)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url)  
    
    is_light = int(light_data)
    current_state = bool(is_on)
    print('is_light', is_light)
    print('current_state', current_state)
    bright_light = int(config.get('server', 'brightLight'))
    low_light = int(config.get('server', 'lowLight'))
    print('bright_light', bright_light)
    print('low_light', low_light)
    
    #if it is dark and light is off then return status True.
    if is_light == low_light and result == True:
        return True
    
    #else if it is clear or out of schedule return false to turn off the light
    elif is_light == bright_light or result == False:
        return False
    
    #else return the current state
    else:
        return current_state

def construct_api_url(config):
    apir_url = config.get("server", "api_url")
    sensor_id = config.get("server", "light_sensor_id")
    time = datetime.now().time()
    
    url = "".join([apir_url, sensor_id, '/', str(time)])
    
    return url