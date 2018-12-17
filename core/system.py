import json
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

with open (base_dir+"\db\\auth_info.json") as f:
    data=json.load(f)

class System:
    def __init__(self,username,password):
        if username in data and password==data[username]:
            print ("Login as " + username)
        else:
            print ("Login failed")
            return
