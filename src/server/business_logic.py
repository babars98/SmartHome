import config

config = config.getconfig()


def identify_and_process_sensor(data):
    decoded_string = data.decode()
    sensor_with_data = decoded_string.split(':')
    
    if sensor_with_data[0] == config.get('common', 'tempsensoridentifier'):
       return process_temp_sensor(sensor_with_data[1])
    else:
        return process_light_sensor(sensor_with_data[1])
        
def process_temp_sensor(temprature_data):
    
    is_fan_on = False
        
    temprature = float(temprature_data)
    temprature_limit = int(config.get('server', 'hightemp'))
    
    #if temprature is 25C or more turn on the fan and return the status True.
    if temprature > temprature_limit and is_fan_on == False:
        is_fan_on = True
        return True
    #else if temprature is less than 25C turn off the fan and return False.
    elif temprature < temprature_limit and is_fan_on == True:
        is_fan_on = False
        return False  
    
    
def process_light_sensor(lux_data):
    
    if not hasattr(process_temp_sensor, "is_light_on"):
        process_temp_sensor.is_light_on = False
    
    lux = int(lux_data)
    lux_limit = int(config.get('server', 'brightlux'))
    
    if lux < lux_limit and is_light_on == False:
        is_light_on = True
        return True
    
    elif lux > lux_limit and is_light_on == True:
        is_light_on = False
        return False
    
    
        
    