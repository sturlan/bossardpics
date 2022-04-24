import csv
import requests
import time
import re
import urllib.request

reader = csv.reader(
    open("bossard.csv"), delimiter=";")
picscsv = open('piclinks.txt', mode='w')
nopic = open('nopic.txt', mode='w')
for row in reader:
    time.sleep(1)
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
        i=i+1
        urllib.request.urlretrieve("https://bossard.com"+link, "/media/darko/STORE/BoossardPics/"+row[1]+"_"+str(i))
    for link in piclinks:
        #fieldnames = ['ARTNMR','piclinks']
        line = row[1]+";"+link+"\n"
        picscsv.write(line)