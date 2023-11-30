from time import sleep
import RPi.GPIO as GPIO
import config
import client_socket
import light_module

#global variable to keep track the fan and light status
is_light_on = False

#create the socket conection, read the temprature data and start sending to server
def start_client(config):
    try:
        light_id = config.get('common', 'lightsensoridentifier')
        delay = int(config.get('client', 'lightdelay'))
        sensor_pin = int(config.get('client', 'lightsensorpin'))
        global is_light_on
        while True:      
            light_data = read_sensor_data(sensor_pin) 
            data = ":".join([light_id, str(light_data), str(is_light_on)])

            res = send_data(data)
            print('Light On', is_light_on)
            is_light_on = light_module.set_mode(res, is_light_on)
            
            #wait for some time before sending next data
            sleep(delay)
            
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        sleep(delay)
        
def send_data(data):
    try:    
        sockt = client_socket.create_connection(config)
        sockt.sendall(data.encode())
        res = sockt.recv(1024)
        res = bool.from_bytes(res)
        sockt.close()
        return res
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        sockt.close()   

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