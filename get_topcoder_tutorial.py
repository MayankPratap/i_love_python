import requests
import pdfcrowd
import urllib2
import os

from bs4 import BeautifulSoup,SoupStrainer

url="https://www.topcoder.com/community/data-science/data-science-tutorials/"

def save_as_pdf(link,filename):

    try:

        client=pdfcrowd.Client("MayankPratap", "28d53cddfd1b63f50748fd6c58ad0646")
        output_file=open(filename,'wb')
        page=requests.get(link)
        soup=BeautifulSoup(page.text)
        html=soup.find_all('div',{'class':'container'})
        
        client.convertHtml(''.join(map(str,html)),output_file)
        output_file.close()
        print filename," saved"
    except pdfcrowd.Error,why:

        print "Failed:",why

page=requests.get(url)
page_bs=BeautifulSoup(page.text)

tutorial_links=[]

for link_detail in page_bs.select('a[href]'):

        link=link_detail.get('href')
        if link.startswith(url):
            tutorial_links.append(link)

for link in tutorial_links:
    link=link[:-1]
    #print link
    fileName=os.path.basename(link)+'.pdf'
    #print fileName
    save_as_pdf(link,fileName)

