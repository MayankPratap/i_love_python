#!python3
# ScrapeJames.py - Downloads every James Altucher's Post

import requests,os,bs4,urllib.request


url='http://jamesaltucher.com/page/'
os.makedirs('jamesaltucher',exist_ok=True)# Store all posts of james in this folder

page=1

while 1==1:
    
   loadurl=url+str(page)
   page+=1
   res=requests.get(loadurl)
   try:  
       res.raise_for_status()
       soup=bs4.BeautifulSoup(res.text,"html5lib")
       posts=soup.select('.post-title a')
       i=0
       
       while i<len(posts):
           goto=posts[i].get('href')
           page=urllib.request.urlopen(goto)
           page_content=page.read()
           page_content=page_content.decode('utf-8')   # Converting byte type to str type for python3
           goto=goto[:-1]
           # Remove last '/' from address so that we can take basename
           # and then add a '.html' to filename
           filename=os.path.basename(goto)+'.html'
           print(filename)
           filename=os.path.join('jamesaltucher',filename)
           with open(filename,'w') as fid:
               fid.write(page_content)

           i+=1    
               
   except Exception as exc:
       print('There was a problem: %s' % (exc))
       break
       
print('Done.')       
   
                    
       
          
            
        
    
       



    
    
