import socket

def create_connection(config):
    
    host = config.get('common', 'serveraddress') #['common', 'serveraddress']   #Host IP or DNS
    port = config.getint('common', 'port')      # Arbitrary non-privileged port
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt.connect((host, port))
    
    return sockt