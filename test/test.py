import requests
import os

with open(os.path.join( os.path.dirname(os.path.abspath(__file__)), "test.html")) as f:
    html = f.read()

# html = requests.get('https://google.com/').text.encode('utf-8')

headers = {'Content-type': 'text/html'}
url = 'http://127.0.0.1:80/image'

r = requests.post(url=url, headers=headers, data=html)
if r.status_code == 200:
    with open('test.png', 'wb') as out:
        out.write(r.content)
    del r