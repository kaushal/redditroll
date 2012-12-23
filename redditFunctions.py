import json
import requests
from pprint import pprint as pp2

def login(username, password):
    print 'beginning login'
    UP = {'user':username, 'passwd':password, 'api_type': 'json',}
    headers = {'user-agent': 'asdf',}

    client = requests.session()
    
    r = client.post('http://www.reddit.com/api/login', data=UP)

    print r.text
    print r.cookies

    j = json.loads(r.text)

    client.modhash = j['json']['data']['modhash']
    print '{USER}\'s modhash is: {mh}'.format(USER=username, mh=client.modhash)
    client.user = username
    def name():
        return '{}\'s client'.format(username)
    return client

def subredditInfo(client, limit=25, sr='tankorsmash',sorting='', return_json=False, **kwargs):
    """retrieves X (max 100) amount of stories in a subreddit\n
    'sorting' is whether or not the sorting of the reddit should be customized or not,
    if it is: Allowed passing params/queries such as t=hour, week, month, year or all"""
 
    #query to send
    parameters = {'limit': limit,}
    #parameters= defaults.copy()
    parameters.update(kwargs)
 
    url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
    r = client.get(url,params=parameters)
    print 'sent URL is', r.url
    j = json.loads(r.text)
 
    #return raw json
    if return_json:
        return j
 
    #or list of stories
    else:
        stories = []
        for story in j['data']['children']:
            #print story['data']['title']
            stories.append(story)
 
        return stories
 
    client = login('USERNAME', 'PASSWORD')
 
    j = subredditInfo(client, limit=1)
 
    pp2(j)
