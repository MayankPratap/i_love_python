#!python3
# downloadXkcd.py - Downloads evry single XKCD comic.

import requests,os,bs4

url='http://xkcd.com'  # starting url
os.makedirs('xkcd',exist_ok=True)# Store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res=requests.get(url)
    try:       
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('Could not find comic image.')
        else:
            comicUrl='http:'+comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...'%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()

        # Get the Prev button's url.
        prevLink=soup.select('a[rel="prev"]')[0]
        url='http://xkcd.com'+prevLink.get('href')

    except Exception as exc:        
        print('There was a problem: %s' % (exc))    

print('Done.')        
