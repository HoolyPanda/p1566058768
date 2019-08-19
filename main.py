import os
import knocker
import time
import json

def main():
    credentials = json.load(open("credentials.json", 'r'))
    a = knocker.Knocker(login=credentials['login'], password=credentials['password'], token=credentials['token'], groupId=int(credentials['groupid']))
    targetFolder = credentials['targetfolder']
    uploadFlag = False
    while True:
        for osFile in os.listdir(targetFolder):
            # m = open('message', 'r', encoding='ansi').read()
            a.PostFile(dicId=a.UploadFile(file=targetFolder + "\\" + osFile), message=open('message.txt', 'r', encoding='ansi').read())
            os.remove(targetFolder + '\\' + osFile)
            time.sleep(int(credentials['timeout']))
            uploadFlag = True
        pass
        if not uploadFlag: 
            time.sleep(int(credentials['timeout']))
try:
    main()
except Exception as e:
    print(str(e))