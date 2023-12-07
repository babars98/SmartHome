import socket
import config

#create socket connection
def create_connection():
    cofg = config.getconfig()
    host = cofg.get('common', 'serveraddress') #['common', 'serveraddress']   #Host IP or DNS
    port = cofg.getint('common', 'port')      # Arbitrary non-privileged port
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.connect((host, port))
    
    return sockt

#send data to the server
def send_data(data):
    
    try:    
        socket = create_connection()
        socket.sendall(data.encode())
        res = socket.recv(1024)
        res = bool.from_bytes(res)
        socket.close()
        return res
    
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        socket.close()