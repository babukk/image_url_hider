
import base64
import json

# ----------------------------------------------------------------------------------------------------------------------
def encode(key, clear):
    try:
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("" . join(enc))
    except:
        return None

# ----------------------------------------------------------------------------------------------------------------------
def decode(key, enc):
    try:
        dec = []
        enc = base64.urlsafe_b64decode(json.loads(json.dumps(enc)).encode('ascii'))
        #- enc = base64.urlsafe_b64decode(enc)     # doesn't work with JSON-encoded strings

        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "" . join(dec)

    except:
        return None


if __name__ == '__main__':

    key = 'top secret'
    # key = ''
    # xxx = 'http://i02.c.aliimg.com/img/ibank/2015/762/803/2116308267_1378471200.jpg'
    # xxx = encode(key, xxx)
    # print  xxx

    xxx = "vtXn6ZtPf96gnZfRTsLazYmw1ly50OCoyo23pNnNytyLkKCUUXieZYyTorGRU3-noZyfoVCZoJpXoqBhjZmnsJJSgKWe1dnV"
    print  decode(key, xxx)

