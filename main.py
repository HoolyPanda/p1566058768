import os
import knocker
import time

def main(folder=""):
    a = knocker.Knocker(login=open("./login","r").read(), password=open("./password",'r').read(), tokenPath='./token', groupId=int(open('./groupid', 'r').read()))
    targetFolder = folder+ '\\'
    while True:
        for osFile in os.listdir(targetFolder):
            a.PostFile(dicId=a.UploadFile(file=targetFolder + osFile), message="test1")
            os.remove(targetFolder + osFile)
            time.sleep(900)
        pass
try:
    main('folder')
except Exception as e:
    print(str(e))