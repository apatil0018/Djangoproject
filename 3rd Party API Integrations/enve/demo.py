import requests
import pandas as pd

def API_Connection():
    BASE_URL =""
    #ENDPOINT = "api/unknown/"

    resp = requests.get(BASE_URL)
    
    #print(resp.text)
    #print(resp.json())

    obj = resp.json()
    print(obj)
    #data = obj.get("data")
    #df = pd.DataFrame(data)
    #print(df)
    

API_Connection()
