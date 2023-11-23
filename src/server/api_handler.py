import requests

def get_api_data(url):
    
    try:
        
        response = requests.get(url)
        
        if(response.status_code == 200):
            return response.json()
            
        else:
            return False
    except:
        return False

