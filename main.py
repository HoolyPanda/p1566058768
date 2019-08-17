import os
import knocker
import time

def main():
    a = knocker.Knocker(login=open("login","r").read(), password=open("password",'r').read(), tokenPath='token', groupId=int(open('groupid', 'r').read()))
    targetFolder = open('folder','r').read() + '\\'
    while True:
        for osFile in os.listdir(targetFolder):
            a.PostFile(dicId=a.UploadFile(file=targetFolder + osFile), message=open('message', 'r').read())
            os.remove(targetFolder + osFile)
            time.sleep(900)
        pass
try:
    main()
except Exception as e:
    print(str(e))