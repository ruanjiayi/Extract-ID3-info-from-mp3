# -*- coding: utf-8 -*-
from os import listdir
from eyed3.utils import art
import eyed3
path = "D:\course\dam\music\like\\"
fileList = listdir(path)

def getInfo(tag):
    info = "title:"+tag.title+"\n"
    info += "album:"+tag.album+"\n"
    info += "artist:"+tag.artist+"\n"
    return info
    
for file in fileList:
    mp3 = path + file
    t = eyed3.load(mp3)
    if not t:
        print("LoadError:"+file)
        continue
    t=t.tag
    
    artPic = art.getArtFromTag(t)
    fileName = file[:-4] #cut the extension
    text = open(fileName+".txt","w",encoding="utf-8")
    text.write(getInfo(t))
    text.close()
    
    if artPic:
       image = artPic[0]
    else:
     print("no image")
     continue
    picture = open(fileName+".png","wb")
    picture.write(image.image_data)
    picture.close()