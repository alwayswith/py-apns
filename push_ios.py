#coding=utf-8
import sys
import apns

def push(msg):
    #推送需要用到的证书
    pem = 'apns-dev-cert.pem'
    token = msg['udid']
    data = msg['data']
    sandbox = True

    payload = apns.Payload(msg['content'], msg['count'], data)
    return apns.APN(token, payload, pem, sandbox)

if __name__ == '__main__':
    msg = {
        'data':{},
        #'data': {'type':1, 'skiplink': 'yymobile://Web/Features/7/Url/http%3a%2f%2fm.yy.com', 'skiptype':1},
        'count': 8,
        'udid': 'de2f1721 13849c54 ee60809f d278dd97 fca503c7 276b0182 2ebfe67b 875e4d35',
        'content': '推送测试'
    }
    print push(msg)