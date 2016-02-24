#!python3
#i_am_feeling_lucky.py - Takes Search Parameters from command line and gets first 5 search results and opens them in
# in a browser in seperate tabs.

import webbrowser,sys,requests,bs4

if len(sys.argv)>1:
    # Get search parameters from command line and join them to form a single parameter
    query=' '.join(sys.argv[1:])
    res=requests.get('https://www.google.co.in/search?q='+query)
    try:
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"html5lib")
        topresults=soup.select(".r a")
        
        numOpen = min(5, len(topresults))
        
        for i in range(numOpen):
            webbrowser.open('http://google.com'+topresults[i].get('href'))

           
            
        
        
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    
    

    
else :
    print('Please enter a search query')
