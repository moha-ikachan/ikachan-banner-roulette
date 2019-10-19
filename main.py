import os
import json

from io import BytesIO
from PIL import Image
from base64 import b64encode
from requests_oauthlib import OAuth1Session

import banner


def to_base64(im):
    buffered = BytesIO()

    Image.fromarray(im).save(buffered, format='png')
    img_str = b64encode(buffered.getvalue()).decode('ascii')

    return img_str


def update_profile_banner(banner, config):
    CONSUMER_KEY = config['CONSUMER_KEY']
    CONSUMER_SECRET = config['CONSUMER_SECRET']
    ACCESS_TOKEN = config['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = config['ACCESS_TOKEN_SECRET']

    url = 'https://api.twitter.com/1.1/account/update_profile_banner.json'
    twitter = OAuth1Session(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )

    banner = to_base64(banner)
    data = {'banner': banner}

    res = twitter.post(url, data=data)

    print('status_code: %d' % res.status_code)
    print(res.text)


if __name__ == '__main__':
    conf_path = os.path.join(
      os.path.dirname(os.path.abspath(__file__)), 'account.json'
    )
    with open(conf_path) as fp:
        config = json.load(fp)
    banner_image = banner.make_banner()

    update_profile_banner(banner_image, config)
