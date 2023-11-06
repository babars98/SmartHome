import socket
import business_logic 
import config


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
    

def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client

            # Process and respond to the data as needed
            # For example, you can send a response back to the client
            result = business_logic.identify_and_process_sensor(data)
            client_socket.sendall(result.to_bytes())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket when the connection is lost or an error occurs
        client_socket.close()
      

if __name__ == "__main__":
    config = config.getconfig()
    start_server(config)