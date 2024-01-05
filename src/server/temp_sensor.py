import config
import api_handler

def process_temp_sensor(temprature_data, time):
    
    temprature = float(temprature_data)
    #construct api url with query string parameters
    url = construct_api_url(time)
    #get the result from api either as true or false
    #depending on schedule
    result = api_handler.get_api_data(url, temprature)   
    
    #if temprature is 25C or more turn on the fan and return the status True.
    if result == True:
        return True
    #else if temprature is less than 25C turn off the fan and return False.
    elif result == False:
        return False  
    
    #else return the current state
    else:
        return False
    
    
def construct_api_url(time, data):
    cnfg = config.getconfig()
    apir_url = cnfg.get("server", "api_url")
    sensor_id = cnfg.get("server", "temp_sensor_id")
    
    url = "".join([apir_url, sensor_id, '/', time, '/', data])
    
    return url
