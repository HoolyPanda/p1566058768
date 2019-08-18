import vk_api
import random
import requests
import os

class Knocker:
    def __init__(self, login, password, token, groupId):
        self.client = vk_api.VkApi(login, password)
        if self.client.auth(token_only=True):
            print("succ")
        self.userId = int(self.client.token['user_id'])

        self.bot = vk_api.VkApi(token=token)
        self.bot._auth_token()
        self.gId = groupId
        
    def SendMsg(self, messageText : str, peerId):
        self.bot.method("messages.send",{"peer_id": self.userId, "random_id" : random.randint(1, 1000),"message": messageText})

    def UploadFile(self, file):
        fileToUpload = open(file, 'rb')
        uploadUrl = self.client.method("docs.getWallUploadServer", {"group_id": self.gId})['upload_url']
        request = requests.post(uploadUrl, files = {'file':fileToUpload})
        fileToUpload.close()
        a = request.json()['file']
        return self.client.method('docs.save', {'file': a, 'v':5.101})['doc']['id']

    def PostFile(self, dicId, message, fromGroup = True, signed = '0'):
        a = (str('doc' + str(0 - self.gId) + '_' + str(dicId)))
        self.client.method('wall.post', {'owner_id': 0 - self.gId, 'message': message, 'attachments':a, 'signed': signed, "from_group":fromGroup })
        pass
