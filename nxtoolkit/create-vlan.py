import requests
import json

"""
Modify these please
"""
url='http://192.168.255.128//ins'
switchuser='admin'
switchpassword='cisco'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "config t ;vlan 998 ;name web2",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()