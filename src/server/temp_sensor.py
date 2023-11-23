from datetime import datetime
import api_handler

def process_temp_sensor(temprature_data, is_fan_on, config):
    #construct api url with query string parameters
    url = construct_api_url(config)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url)   
         
    temprature = float(temprature_data)
    temprature_limit = int(config.get('server', 'hightemp'))
    
    #if temprature is 25C or more turn on the fan and return the status True.
    if temprature > temprature_limit and is_fan_on == False and result == True:
        return True
    #else if temprature is less than 25C turn off the fan and return False.
    elif (temprature < temprature_limit and is_fan_on == True) or result == False:
        return False  
    
    #else return the current state
    else:
        return is_fan_on
    
    
def construct_api_url(config):
    apir_url = config.get("server", "api_url")
    sensor_id = config.get("server", "temp_sensor_id")
    time = datetime.now().time()
    
    url = "".join([apir_url, sensor_id, '/', str(time)])
    
    return url
