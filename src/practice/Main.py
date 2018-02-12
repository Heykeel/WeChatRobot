import itchat
import requests
import configparser

def talkRobot(info):
    conf = configparser.ConfigParser()
    conf.read("apikey.ini")
    
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = conf.get('apikey','apikey')
    data = {'key': apikey,'info': info}
    req = requests.post(api_url, data=data).json()
    return req

@itchat.msg_register(itchat.content.TEXT)
def replyFriend(msg):
    replys = talkRobot(msg["Text"])["text"]+'--by Robot'
    return replys

itchat.auto_login()
# itchat.auto_login(enableCmdQR=True)
itchat.run()