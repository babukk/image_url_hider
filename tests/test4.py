#! /usr/bin/env python


import requests

# url = 'http://127.0.0.1:5000/decrypt_url'
url = 'http://92.63.102.86/decrypt_url'
link = 'vtXn6ZtPf96gnZfRTsLazYmw1ly50OCoyo23pNnNytyLkKCUUXieZYyTorGRU3-noZyfoVCZoJpXoqBhjZmnsJJSgKWe1dnThw=='


response = requests.post(url, data={'xhash': link}).json()

print  response

