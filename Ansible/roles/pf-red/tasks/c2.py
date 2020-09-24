#!/bin/python3
import requests

def sendUpdate(ip, name="something"):
    host = "http://pwnboard.win/generic"
    data = {'ip': ip, 'type': name}
    try:
        getoutput = requests.get(str(ip+":8080"),timeout=3) 
        if getoutput:
            req = requests.post(host, json=data, timeout=3)
            print(req.text)
            return True
    except Exception as E:
        print(E)
        return False
sendUpdate("10.15.2.1")
