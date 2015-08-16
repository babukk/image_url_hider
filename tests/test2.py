#! /usr/bin/env python


import requests

# url = 'http://127.0.0.1:5000/encrypt_url'
url = 'http://92.63.102.86/encrypt_url'
# link = 'http://i02.c.aliimg.com/img/ibank/2015/762/803/2116308267_1378471200.jpeg'

link = 'http://i03.c.aliimg.com/img/ibank/2015/316/716/2154617613_1665186263.jpg'

response = requests.post(url, data={'url': link}).json()
print  requests.post(url, data={'url': link}).json()['xhash']


#xlink = 'http://92.63.102.86/image/cache/' + requests.post(url, data={'url': link}).json()['xhash']

#print  xlink
