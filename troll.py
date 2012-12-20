import requests
import json
from pprint import pprint

username = 'not_a_trollbot'
password = 'trollbot'

user_pass_dict = {'user': username, 
                  'passwd': password, 
                  'api_type': 'json' }

headers = {'user-agent': '/u/TankorSmash\'s API python tutorial bot', }
client = requests.session(headers=headers)
r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)
j = json.loads(r.text)
print j
client.modhash = j['json']['data']['modhash']

print '{USER}\'s modhash is: {mh}'.format(USER=username, mh=client.modhash)

