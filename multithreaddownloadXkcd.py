#!python3

# multidonwloadXkcd.py - Downloads XKCD comics using multiple threads

import requests,os,bs4,threading

os.makedirs('xkcdnew',exist_ok=True)  # Store comics in ./xkcd

def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        # Download the page.
        print("Downloading page http://xkcd.com/%s.."%(urlNumber))
        res=requests.get("http://xkcd.com/%s"%(urlNumber))
        res.raise_for_status()
        
        soup=bs4.BeautifulSoup(res.text)
        
        # Find the URL of comic image.
        
        comicElem=soup.select("#comic img")
        
        if comicElem==[]:
            print("Could not find comic image.")
        else:
            comicUrl=comicElem[0].get('src')
            # Download the image.
            print("Downloading image %s..."%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()
            
            # Save the image to ./xkcdnew
            imageFile=open(os.path.join('xkcdnew',os.path.basename(comicUrl)),"wb")
            
            for chunk in res.iter_content(100000):
                 imageFile.write(chunk)
            imageFile.close()


downloadThreads=[]     # A list of all thread objects
for i in range(0,1400,100):          # Loops 14 times,creates 14 threads
    downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print("Done.")
