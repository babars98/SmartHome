import socket
import config
import light_sensor
import temp_sensor


#global variable to keep track the fan and light status
is_fan_on = False
is_light_on = False

#start the server connection and listen indefinitely in a loop
def start_server(config):

    host = config.get('common', 'serveraddress') #['common', 'serveraddress']   #Host IP or DNS
    port = config.getint('common', 'port')      # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(4)

    while True:
    
        conn, addr = s.accept()
        print('Connected by', addr)
        handle_client(conn)
    
#receive the clinet connection
def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client

            # Process and respond to the data as needed
            # For example, you can send a response back to the client
            result = identify_and_process_sensor(data)
            client_socket.sendall(result.to_bytes())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket when the connection is lost or an error occurs
        client_socket.close()

def identify_and_process_sensor(data):
    decoded_string = data.decode()
    sensor_with_data = decoded_string.split(':')
    
    if sensor_with_data[0] == config.get('common', 'tempsensoridentifier'):
        global is_fan_on
        is_fan_on = temp_sensor.process_temp_sensor(sensor_with_data[1], is_fan_on, config)
        return is_fan_on
    elif sensor_with_data[0] == config.get('common', 'lightsensoridentifier'):
        global is_light_on
        is_light_on = light_sensor.process_light_sensor(sensor_with_data[1], is_light_on, config)
        return is_light_on
    else:
        return False

if __name__ == "__main__":
    config = config.getconfig()
    start_server(config)