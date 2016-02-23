#!python3
#socialsites.py  Launches Several Sites simultaneously in seperate tabs simultaneously 
# Names of sites to be entered in command line seperated by spaces


import webbrowser,sys

if len(sys.argv)>1:
    # Get name of social network sites from command line
    i=1
    while i<len(sys.argv):
        webbrowser.open_new_tab('https://www.'+sys.argv[i]+'.com')
        i=i+1
        

        





        
        
        
        
        


