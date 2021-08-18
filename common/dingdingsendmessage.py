
import requests
import json
import base64
import hashlib
import hmac
import urllib.request
import time

def sendmessage(text):
    ##钉钉sha256签名

    timestamp = round(time.time() * 1000)

    secret = 'SEC46598465c1f98d1c82866e153e493cc28dd94a69bd2cf1983f0420854c852539'

    secret_enc = bytes(secret, encoding='UTF-8')

    string_to_sign = '{}\n{}'.format(timestamp, secret)

    string_to_sign_enc = bytes(string_to_sign, encoding='utf-8')

    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()

    sign = urllib.request.quote(base64.b64encode(hmac_code))

    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=bea3ec47a670528ef91f10329209bd4e33b23c3df1a08397fefc4a8025c262cb&sign=%s&timestamp=%s" % \
              (sign, timestamp)


    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 构建请求数据
    message = {

        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {

            "isAtAll": False
        }

    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)

