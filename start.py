import csv
import requests
import time
import re
import urllib.request
from datetime import datetime

reader = csv.reader(open("sample.csv"), delimiter=";")
picscsv = open('pics/piclinks.txt', mode='w')
nopic = open('pics/nopiclog.txt', mode='w')
print("START:")
print(datetime.now())
print("\n")
for row in reader:
    for attempt in range(5):
        try:
            time.sleep(0.2)
            requestlink = "https://www.bossard.com/eshop/global-en/search/?q="+row[1]
            htmlobject = requests.get(requestlink)
            htmltext = htmlobject.text
            hreflinks = re.findall("href=[\"\'](.*?)[\"\']", htmltext)
            srclinks = re.findall("src=[\"\'](.*?)[\"\']", htmltext)
            piclinks=[]
            for links in hreflinks:
                if "large" in links:
                    piclinks.append(links)
            for links in srclinks:
                if "large" in links:
                    piclinks.append(links)
            piclinks = list( dict.fromkeys(piclinks) )
            i=0
            if len(piclinks)==0:
                nopic.write(row[1]+"\n")
            for link in piclinks:
                i+=1
                urllib.request.urlretrieve("https://bossard.com"+link, "pics/"+row[1]+"_"+str(i))
                picscsv.write(row[1]+";"+link+"\n")
                print(row[1]+"->"+str(i))
                print(datetime.now())
        except:
            continue
        else:
            break
print("\n"+"END:")
print(datetime.now())