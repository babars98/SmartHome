from time import sleep
import config
from DHT20 import DHT20
import socket
import client_socket
import fan_module

#global variable to keep track the fan and light status
is_fan_on = False

#create the socket conection, read the temprature data and start sending to server
def start_client(socket, config):
    dht20 = initialize()
    socket = client_socket.create_connection(socket, config)
    temp_id = config.get('common', 'tempsensoridentifier')
    delay = int(config.get('client', 'tempdelay'))
    while True:      
        temprature = read_sensor_data(dht20)
        global is_fan_on
        data = ":".join([temp_id, temprature, is_fan_on])
        socket.sendall(data.encode())
        res = socket.recv(1024)
        res = bool.from_bytes(res)
        
        print('is_fan_on', is_fan_on)
        is_fan_on = fan_module.set_mode(res, is_fan_on)
        
        #wait for some time before sending next data
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
    start_client(socket, config)