from time import sleep
from datetime import datetime
import config
from DHT20 import DHT20
import client_socket
import temp_businesslogic

#global variable to keep track the fan and light status
is_fan_on = False

#create the socket conection, read the temprature data and start sending to server
def start_client(config):
    try:
        dht20 = initialize()
        temp_id = config.get('common', 'tempsensoridentifier')
        delay = int(config.get('client', 'tempdelay'))
        global is_fan_on
        while True:      
            temprature = read_sensor_data(dht20) 
            is_temp_high = temp_businesslogic.check_temp_level(int(temprature))
            
            #if the temprature is hight then send request to server
            if is_temp_high == True:
                time = datetime.now().time
                data = ",".join([temp_id, str(temprature), str(time)])        
                res = client_socket.send_data(data)
                print('is_fan_on', is_fan_on)
                is_fan_on = temp_businesslogic.set_mode(res, is_fan_on)
            
            #wait for some time before sending next data
            elif is_fan_on == True:
                is_fan_on = temp_businesslogic.set_mode(False, is_fan_on)
                
            sleep(delay)
            
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        sleep(delay)
           
#Initialize the DHT20 Temprature sensor
def initialize():
    # The first  parameter is to select i2c0 or i2c1
    # The second parameter is the i2c device address
    I2C_BUS     = 0x01  # default use I2C1 bus
    I2C_ADDRESS = 0x38  # default I2C device address

    dht20 = DHT20(I2C_BUS ,I2C_ADDRESS)
    # Initialize sensor
    if not dht20.begin():
        print("DHT20 sensor initialization failed")
    
    return dht20

#Read the data from sensor
def read_sensor_data(dht20):
    
    temp_celcius, humidity, crc_error = dht20.get_temperature_and_humidity()
    
    if crc_error:
      print("CRC               : Error\n")
    
    print("Temperature       : %f\u00b0C " %(temp_celcius))
    
    return temp_celcius
    
    # Read ambient temperature and relative humidity and print them to terminal

if __name__ == "__main__":
    config = config.getconfig()
    start_client(config)