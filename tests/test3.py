#! /usr/bin/env python

# import  json
from requests import post, put, get

response = post('http://localhost:5000/kuku', data={'data': 'Remember the milk'}).json()


print  response


