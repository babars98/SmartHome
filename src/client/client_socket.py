
def create_connection(socket, config):
    
    host = config.get('common', 'serveraddress') #['common', 'serveraddress']   #Host IP or DNS
    port = config.getint('common', 'port')      # Arbitrary non-privileged port
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    
    return socket