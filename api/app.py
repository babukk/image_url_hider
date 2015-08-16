
from flask import Flask, request, send_file, abort
from flask_restful import Resource, Api
import urllib2
from BeautifulSoup import BeautifulSoup

import EasyCrypto


app = Flask(__name__)
api = Api(app)


KEY = 'Vasya Pupkin and Co.'
HOST = '92.63.102.86'
IMG_PATH = '/image/cache/'


# ----------------------------------------------------------------------------------------------------------------------
class ReplaceImgSrc(Resource):

    def post(self):
        html = request.form['html']

        soup = BeautifulSoup(html)
        for img in soup.findAll('img'):
            img['src'] = 'http://' + HOST + IMG_PATH + EasyCrypto.encode(KEY, img['src'])
            # img['rel'] = 'nofollow'

        return {'html': str(soup)}


# ----------------------------------------------------------------------------------------------------------------------
class EncryptURL(Resource):

    def post(self):
        url = request.form['url']
        hash_str = EasyCrypto.encode(KEY, url)

        return {'xhash': hash_str}


# ----------------------------------------------------------------------------------------------------------------------
class DecryptURL(Resource):

    def post(self):
        xhash = request.form['xhash']
        url = EasyCrypto.decode(KEY, xhash)

        return {'url': url}


api.add_resource(EncryptURL, '/encrypt_url')
api.add_resource(DecryptURL, '/decrypt_url')
api.add_resource(ReplaceImgSrc, '/replace_img_src')


# ----------------------------------------------------------------------------------------------------------------------

@app.route('/image/cache/<string:xhash>', methods=['GET'])
@app.route('/image/cache/<string:xhash>/photo.jpg', methods=['GET'])
@app.route('/image/cache/<string:xhash>/photo.gif', methods=['GET'])
@app.route('/image/cache/<string:xhash>/photo.png', methods=['GET'])
def GetImageByHash(xhash):

    url = EasyCrypto.decode(KEY, xhash)
    f_ext = '.'
    mimetype = ''

    try:
        img = urllib2.urlopen(url)
        mime = img.info()['Content-type']

        if mime.endswith("png"):
            f_ext = '.png'
        elif mime.endswith("jpeg"):
            f_ext = '.jpg'
        elif mime.endswith("gif"):
            f_ext = '.gif'

        return send_file(
            img,
            attachment_filename='xhash' + f_ext,
            mimetype=mime
        )
    except:
        abort(404)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

