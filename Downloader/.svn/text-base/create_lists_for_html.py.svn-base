import os
import time
import glob
import urllib2
import defbestuursrecht
import deffiscaal
import defhorecarecht
import defpolitiebundel
import defprivaatrecht
import defrecht
import defrechtlite
import defsociaal
import defstrafrecht
import defstudiebundel
import defverzekeringsrecht

def makehtml(module):
    d = module.structure()
    print str(module)
    l= d.keys()
    l.sort()
    print "<p>"
    c = 1
    for i in l:
        print "<h2><b>",i,"</b></h2>"        
        print "<ul>"
        for j in d[i]:
            print "<li>",j["title"],"</li>"
        print "</ul>"
    print "</p>"
    
def main():

    defbestuursrecht.structure()
    deffiscaal.structure()
    defhorecarecht.structure()
    defpolitiebundel.structure()
    defprivaatrecht.structure()
    defrechtlite.structure()
    defrecht.structure()
    defstrafrecht.structure()
    defstudiebundel.structure()
    defsociaal.structure()
    defverzekeringsrecht.structure()

    makehtml(defverzekeringsrecht)
    #makehtml(defbestuursrecht)
    #makehtml(deffiscaal)
    #makehtml(defhorecarecht)
    #makehtml(defpolitiebundel)
    #makehtml(defprivaatrecht)
    #makehtml(defrechtlite)
    #makehtml(defrecht)
    #makehtml(defstrafrecht)
    #makehtml(defstudiebundel)
    #makehtml(defsociaal)

if __name__=="__main__":
    main()