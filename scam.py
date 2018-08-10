import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://UrlToTheForm'
names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits) for i in range(4))

    username = name.lower() + name_extra + random.choice(name) + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(9))

    requests.post(url, allow_redirects=False, data={
        'user': username,
        'pass': password
    })

    print('sending', (username,password))
