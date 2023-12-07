import config
import api_handler

def process_light_sensor(light_data, time):
    
    cnfg = config.getconfig()
    #construct api url with query string parameters
    url = construct_api_url(cnfg, time)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url)  
    
    #if it is dark and light is off then return status True.
    if result == True:
        return True
    
    #else if it is clear or out of schedule return false to turn off the light
    elif result == False:
        return False
    
    #else return the current state
    else:
        return False

def construct_api_url(config, time):
    apir_url = config.get("server", "api_url")
    sensor_id = config.get("server", "light_sensor_id")
    
    url = "".join([apir_url, sensor_id, '/', time])
    
    return url