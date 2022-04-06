from lib2to3.pgen2 import token
import requests
import json

url = "https://chandratech.atlassian.net/rest/api/3/issue/Ap-17"
token = 'w4OvBrzLVEICBAhhAMlM163C'
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

r = requests.get(url, headers=headers, auth=('surisetty.chandrakiran@gmail.com', token))

#print(r.text)
#print(type(r))


print(json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",", ": ")))
