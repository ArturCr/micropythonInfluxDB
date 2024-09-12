#Make a secrets.py file with the content below and leave this True
# or fill in the data in this file and set it to False
secret=True

###########################################################
#Network Data
ssid = ""
password = ""

#Database Data
CLUSTER_URL=""
ORGANIZATION_PROFILE_NAME=""
BUCKET=""
API_TOKEN=""
###########################################################

if secret:
    from secrets import *
    
### TODO: Fix while true loop
    
import network
import time
import requests
import random

def ConnectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#Connect to Network
ConnectWiFi()

#Build URL
url = f"{CLUSTER_URL}/api/v2/write?org={ORGANIZATION_PROFILE_NAME}&bucket={BUCKET}&precision=ns"

#Build message header
headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Content-Type": "text/plain; charset=utf-8",
        "Accept": "application/json"
}

# set debug True or False
debug = True

print('... Ready to go ....')
while True:
    temp = random.randint(20,40)
    data = f"thermometer,sensor_id=thermometer temp={temp}"
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 204:
        print("Data posted successfully")
    else:
        print("Failed to post data")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
    response.close()

    if debug:
        print(data)
        
    time.sleep(1)

            
