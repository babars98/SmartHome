import config
import api_handler

def process_light_sensor(light_data, time):
    
    cnfg = config.getconfig()
    #construct api url with query string parameters
    url = construct_api_url(cnfg, time, light_data)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url)  
    
    #if Current Time is between the set schedule/Interval, return True.
    if result == True:
        return True
    
    #else if Current Time is not between the set schedule/Interval, return False.
    elif result == False:
        return False
    
    #else return the current state
    else:
        return False

def construct_api_url(config, time, data):
    apir_url = config.get("server", "api_url")
    sensor_id = config.get("server", "light_sensor_id")
    
    url = "".join([apir_url, sensor_id, '/', time, '/', str(data)])
    
    return url