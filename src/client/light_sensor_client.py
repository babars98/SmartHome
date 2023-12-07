from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime
import config
import client_socket
import light_businesslogic

#global variable to keep track the fan and light status
is_light_on = False

#create the socket conection, read the temprature data and start sending to server
def start_client(config):
    try:
        light_id = config.get('common', 'lightsensoridentifier')
        delay = int(config.get('client', 'lightdelay'))
        sensor_pin = int(config.get('client', 'lightsensorpin'))
        global is_light_on
        
        #repeat the sensor read after a delay
        while True:      
            light_data = read_sensor_data(sensor_pin) 
            
            is_low_light = light_businesslogic.check_light_level(int(light_data))
            
            if is_low_light == True:
                time = str(datetime.now().time())
                data = ",".join([light_id, str(light_data), str(time)])

                res = client_socket.send_data(data)
                print('Light On', is_light_on)
                is_light_on = light_businesslogic.set_mode(res, is_light_on)
                
            elif is_light_on == True:
                is_light_on = light_businesslogic.set_mode(False, is_light_on)
                
            #wait for some time before sending next data
            sleep(delay)
            
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        sleep(delay)

#Read the data from sensor
def read_sensor_data(sensor_pin):
    # Set BCM mode for GPIO numbering
    GPIO.setmode(GPIO.BOARD)
    
    # Setup the GPIO pin for input
    GPIO.setup(sensor_pin, GPIO.IN)
    
    # Read the sensor value
    sensor_value = GPIO.input(sensor_pin) 
    
    return sensor_value 

if __name__ == "__main__":
    config = config.getconfig()
    start_client(config)