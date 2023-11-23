from datetime import datetime
import api_handler

def process_light_sensor(lux_data, is_light_on, config):
    
    #construct api url with query string parameters
    url = construct_api_url(config)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url)  
    
    lux = int(lux_data)
    lux_limit = int(config.get('server', 'brightlux'))
    
    #if it is dark and light is off then return status True.
    if lux < lux_limit and is_light_on == False and result == True:
        return True
    
    #else if it is clear or out of schedule return false to turn off the light
    elif (lux > lux_limit and is_light_on == True) or result == False:
        return False
    
    #else return the current state
    else:
        return is_light_on

def construct_api_url(config):
    apir_url = config.get("server", "api_url")
    sensor_id = config.get("server", "light_sensor_id")
    time = datetime.now().time()
    
    url = "".join([apir_url, sensor_id, '/', str(time)])
    
    return url