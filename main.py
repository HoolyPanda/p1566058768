import os
import knocker
import time
import json

def main():
    credentials = json.load(open("credentials.json", 'r', encoding = 'utf-8-sig'))
    a = knocker.Knocker(login=credentials['login'], password=credentials['password'], token=credentials['token'], groupId=int(credentials['groupid']))
    targetFolder = credentials['targetfolder']
    uploadFlag = False
    while True:
        for osFile in os.listdir(targetFolder):
            # m = open('message', 'r', encoding='ansi').read()
            print('Found new file')
            a.PostFile(dicId=a.UploadFile(file=targetFolder + "\\" + osFile), message=open('message.txt', 'r', encoding = 'utf-8-sig').read())
            os.remove(targetFolder + '\\' + osFile)
            time.sleep(int(credentials['timeout']))
            uploadFlag = True
        pass
        if not uploadFlag: 
            # print('Folder is empty')
            time.sleep(int(credentials['timeout']))
main()
# try:
#     pass
# except Exception as e:
#     print(str(e))