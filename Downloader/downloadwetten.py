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

def print_command(command):
    print "==", command, "=="
    os.system(command)

def downloadfile(fname, url):
    try:
        print_command("fetch -vamT 6000 "+url)
        print_command("mv opslaan_in_html temp.zip")
        print_command("unzip temp.zip")
        newfname = fname[0:140]
        newfname = newfname.replace(" ", "-").replace("'", "").replace(".", "").replace("/", "-").replace("\\", "-")+".html"
        newfname = newfname.replace("-.", ".").replace(",", "").replace("(", "").replace(")", "").replace("--", "-")
        print newfname
        os.rename(glob.glob('*.html')[0], newfname)
        return newfname
    except:
        return ''

def download(module):
    bookdir = "downloads/"+module.__name__.replace("def", "")
    if os.path.exists(bookdir):
        print_command("rm -Rf "+bookdir)
    print_command("mkdir "+bookdir)
    d = module.structure()
    for i in d:
        wetdir = "downloads/"+module.__name__.replace("def", "")+"/'"+i+"'"
        if not os.path.exists(wetdir):
            print_command("mkdir "+wetdir)
        for j in d[i]:
            newfname = ''
            ln = len(newfname)
            while ln==0:
                newfname = downloadfile(j["title"], "http://wetten.overheid.nl/"+j["id"]+"/opslaan_in_html")
                ln = len(newfname)
                print ln
                if ln==0:
                    print "== sleeping =="
                    time.sleep(60)
            time.sleep(5)
            print_command("mv "+newfname+" "+wetdir)
            print_command("rm *.zip")
            print_command("rm -Rf css")
            print "== sleeping =="
            time.sleep(6)

def checkfordoubles(module):
    l = []
    d = module.structure()
    for i in d:
        for j in d[i]:
            l.append(j["id"])
    for i in l:
        d = 0
        for j in l:
            if i==j:
                d += 1
            if d==2:
                print "dubbele gevonden", str(module), i
                raise

def main():
    print_command("date")
    print_command("rm *.zip")
    print_command("rm -Rf css")
    print_command("rm -Rf downloads/")
    print_command("mkdir downloads")

    #defstrafrecht.structure()
    #defbestuursrecht.structure()
    #deffiscaal.structure()
    #defhorecarecht.structure()
    defpolitiebundel.structure()
    #defprivaatrecht.structure()
    #defrechtlite.structure()
    #defrecht.structure()
    #defstudiebundel.structure()
    #defsociaal.structure()
    #defverzekeringsrecht.structure()

    #checkfordoubles(defstrafrecht)
    #checkfordoubles(defbestuursrecht)
    #checkfordoubles(deffiscaal)
    #checkfordoubles(defhorecarecht)
    checkfordoubles(defpolitiebundel)
    #checkfordoubles(defprivaatrecht)
    #checkfordoubles(defrechtlite)
    #checkfordoubles(defrecht)
    #checkfordoubles(defstudiebundel)
    #checkfordoubles(defsociaal)
    #checkfordoubles(defverzekeringsrecht)


    #download(deffiscaal)
    #download(defstrafrecht)
    #download(defbestuursrecht)
    #download(deffiscaal)
    #download(defhorecarecht)
    download(defpolitiebundel)
    #download(defprivaatrecht)
    #download(defrechtlite)
    #download(defrecht)
    #download(defstudiebundel)
    #download(defsociaal)
    #download(defverzekeringsrecht)

    print_command("rm -Rf ../2012/RawData/*")
    print_command("cp -r downloads/* ../2012/RawData/")

    #print_command("./bestuursrechtdbcreate.sh")
    #print_command("./horecarechtdbcreate.sh")
    #print_command("./fiscaalrechtdbcreate.sh")
    #print_command("./fiscaalrechtdbcreate.sh")
    print_command("./politierechtdbcreate.sh")
    #print_command("./privaatrechtdbcreate.sh")
    #print_command("./rechtdbcreate.sh")
    #print_command("./rechtlitedbcreate.sh")
    #print_command("./sociaalrechtdbcreate.sh")
    #print_command("./strafrechtdbcreate.sh")
    #print_command("./studiebundeldbcreate.sh")
    #print_command("./verzekeringsrechtdbcreate.sh")

    print_command("date")

if __name__=="__main__":
    main()
