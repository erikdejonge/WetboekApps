
import os
import re
import sys
import cPickle
import copy
#import tidy
import pickle
import sqlite3
import time
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser    

global_wetboekhoofdstuk = 0
global_wetten = 0
global_hoofdstukken = 0
global_artikelen = 0
hoofdstuk_expressie = "  [A-Za-z0-9\xa7]"
start_boek = "-----------------------"
db_dir = "Apps/Politierecht/db/"
#db_dir = "db/"

def latin1_to_ascii(unicrap):
    xlate={0xc0:'A', 0xc1:'A', 0xc2:'A', 0xc3:'A', 0xc4:'A', 0xc5:'A',
        0xc6:'Ae', 0xc7:'C',
        0xc8:'E', 0xc9:'E', 0xca:'E', 0xcb:'E',
        0xcc:'I', 0xcd:'I', 0xce:'I', 0xcf:'I',
        0xd0:'Th', 0xd1:'N',
        0xd2:'O', 0xd3:'O', 0xd4:'O', 0xd5:'O', 0xd6:'O', 0xd8:'O',
        0xd9:'U', 0xda:'U', 0xdb:'U', 0xdc:'U',
        0xdd:'Y', 0xde:'th', 0xdf:'ss',
        0xe0:'a', 0xe1:'a', 0xe2:'a', 0xe3:'a', 0xe4:'a', 0xe5:'a',
        0xe6:'ae', 0xe7:'c',
        0xe8:'e', 0xe9:'e', 0xea:'e', 0xeb:'e',
        0xec:'i', 0xed:'i', 0xee:'i', 0xef:'i',
        0xf0:'th', 0xf1:'n',
        0xf2:'o', 0xf3:'o', 0xf4:'o', 0xf5:'o', 0xf6:'o', 0xf8:'o',
        0xf9:'u', 0xfa:'u', 0xfb:'u', 0xfc:'u',
        0xfd:'y', 0xfe:'th', 0xff:'y',
        0xa1:'!', 0xa2:'{cent}', 0xa3:'{pound}', 0xa4:'{currency}',
        0xa5:'{yen}', 0xa6:'|', 0xa7:'{section}', 0xa8:'{umlaut}',
        0xa9:'{C}', 0xaa:'{^a}', 0xab:'<<', 0xac:'{not}',
        0xad:'-', 0xae:'{R}', 0xaf:'_', 0xb0:'{degrees}',
        0xb1:'{+/-}', 0xb2:'{^2}', 0xb3:'{^3}', 0xb4:'"',
        0xb5:'{micro}', 0xb6:'{paragraph}', 0xb7:'*', 0xb8:'{cedilla}',
        0xb9:'{^1}', 0xba:'{^o}', 0xbb:'>>', 
        0xbc:'{1/4}', 0xbd:'{1/2}', 0xbe:'{3/4}', 0xbf:'?',
        0xd7:'*', 0xf7:'/'
        }

    r = ''
    for i in unicrap:
        if xlate.has_key(ord(i)):
            r += xlate[ord(i)]
        elif ord(i) >= 0x80:
            pass
        else:
            r += str(i)
    return r

def latin1_to_html(unicrap):
    return unicrap
    xlate={
        0xa1:'!', 0xa2:'&#162;', 0xa3:'&#163;', 0xa4:'&#164;',
        0xa5:'&#165;', 0xa6:'|', 0xa7:'&#167;', 0xa8:'&#168;',
        0xa9:'{C}', 0xaa:'{^a}', 0xab:'<<', 0xac:'&#172;',
        0xad:'-', 0xae:'{R}', 0xaf:'_', 0xb0:'',
        0xb1:'&#177;', 0xb2:'&#178;', 0xb3:' &#179;', 0xb4:'"',
        0xb5:'&#181;', 0xb6:' &#182;', 0xb7:'*', 0xb8:'&#184;',
        0xb9:'&#185;', 0xba:'{^o}', 0xbb:'>>', 
        0xbc:'&#188;', 0xbd:'&#189;', 0xbe:'{3/4}', 0xbf:'?',
        0xd7:'*', 0xf7:'/'
        }

    r = ''
    for i in unicrap:
        if xlate.has_key(ord(i)):
            r += xlate[ord(i)]
        elif ord(i) >= 0x80:
            pass
        else:
            r += str(i)
    return r
     
class RemoveLinks(HTMLParser):
    def __init__ (self, sloc):
        HTMLParser.__init__(self)
        self.html = ""
        self.sloc = sloc      

    def handle_data(self, data):
        self.html += data        

    def handle_starttag(self, tag, attrs):
        if tag=="a":
            self.html += "<i class='cur'>"
        else:
            if len(attrs)>0:
                self.html += "<"+tag+" class='"+attrs[0][1]+"'>"
            else:
                self.html += "<"+tag+">"
    def handle_endtag(self, tag):        
        if tag=="a":
            self.html += "</i>"  
        else:
            self.html += "</"+tag+">"
    
def executeQuery(cn, q):
    curs = cn.cursor()
    try:   
        curs.execute(q)
    except Exception, e:
        print {'x':q}
        raise e
    
def run_match(c, filebuffer, line, chapter):    
    buf = ''    
    while True:
        if chapter:
            if not re.match(hoofdstuk_expressie, line):
                break
        else:
            if re.match(hoofdstuk_expressie, line):
                c = c-1
                break            
        buf += line
        c = c + 1
        if c>=len(filebuffer):
            break                
        line=filebuffer[c]
    return c, buf

chap_indent = ""

def make_chap_clean(buf):
    buf = buf.replace("\n\r", " ").replace("\r\n", " ").strip()
    buf = buf.replace("\r", " ")
    buf = buf.replace(".", ". ")
    buf = buf.replace("\t", " ")
    for i in range(0,30):
        buf = buf.replace("   ", " ")    
    for i in range(0,30):
        buf = buf.replace("  ", " ")    
    if re.match("[Afdeling]", buf):
        buf = chap_indent+buf
    return buf

def make_content(buf):
    x = ''
    for i in buf.split("\r\n"):
        b = str(i).strip()
        if len(b)!=0:
            b = b.replace("\r\n", "")
        else:
            b += "\n\n"                
        x += " "+b
    x=x.replace("\n\n \n\n", "")
    y=''
    for i in x.split("\n"):
        y+=i.strip()+"\n"
    return y
     
def find_title(filebuffer):    
    titel = ''
    c=0
    while c<len(filebuffer):
        line=filebuffer[c]     
        if start_boek in line:
            if len(filebuffer[c+1].strip())==0:
                c += 1
            if len(filebuffer[c+1].strip())==0:
                c += 1                
            running = True
            while running:
                c += 1           
                line = filebuffer[c]
                if len(line.strip())==0:
                    running = False
                titel += line 
        #time.sleep(0.5)
        c += 1
    #print str({"x": make_chap_clean(titel).replace("  ", " ")})
    return make_chap_clean(titel).replace("  ", " ")

def find_title_html(html):    
    soup = BeautifulSoup(html)    
    s = soup.find("div", "intitule")
    if s:
        s = make_chap_clean(latin1_to_ascii(s.contents[0]))
    if s:
        return s
    else:
        return ""    

def insert_html_only(html):
    pass

def remove_html(s):
    class RemoveHTML(HTMLParser):
        def __init__ (self):
            HTMLParser.__init__(self)
            self.html = ""      
        def handle_data(self, data):
            if "CDATA" not in data:
                self.html += data        
        def handle_starttag(self, tag, attrs):
            pass
        def handle_endtag(self, tag):        
            pass  
    
    rh = RemoveHTML()
    rh.feed(s)            
    html = rh.html
    html = latin1_to_ascii(html)
    for i in range(0,20):
        html = html.replace("  ", " ")
    return html

def ParseWetHTML(cn, wettenfolder, wetbestand, wf):
    global global_wetten
    global global_hoofdstukken
    global global_artikelen
            
    if ".DS_Store" in wetbestand:
        return
    
    infile = open(os.path.join(wettenfolder, wetbestand),"r")  
    html = infile.read()
        
    options = dict( char_encoding='utf8',
                    output_xhtml=1, 
                    add_xml_decl=1, 
                    indent=1, 
                    tidy_mark=0)
        
    hoofdstukken = []
    artikelnummer=""
    wetbestand_longtitel = find_title_html(html)
    wetbestand_shorttitel = wetbestand.replace("-", " ").replace(".html", "") 
    if len(wetbestand_longtitel.strip())==0 or wetbestand_longtitel.strip()=="#":
        wetbestand_longtitel = wetbestand_shorttitel;
    
    d = pickle.loads(open("afk.pickle", "r").read())
    if d.has_key(wetbestand_shorttitel):
        afk = str(d[wetbestand_shorttitel]).strip().replace(" ", "")
    else:        
        afk = ""
    
    wetartdb = re.match("[a-z0-9]+", wetbestand.replace("-", "").replace(" ", "").lower()).group()+".db"    
    print wetartdb

    q="insert into wetboek values ('"+str(global_wetten)+"', '"+str(global_wetboekhoofdstuk)+"', '"+str(global_wetten)+"', '"+wetbestand_shorttitel.replace("'", "''")+"', '"+wetbestand_longtitel.replace("'", "''")
    if "artikel-kop" in html:    
        q +="', 'hoofdstukken', '"
    else:
        q +="', '"+wetartdb.replace(".db", "")+"', '"
    q += afk+"', 0, 0)"
    executeQuery(cn, q)            
        
    cnx = None
    if not os.path.exists(db_dir+wetartdb):        
        cnx = sqlite3.connect(db_dir+wetartdb)                    
        q = """CREATE TABLE artikel(id serial NOT NULL, 
                            hoofdstuk_id integer NOT NULL, 
                            sequence integer NOT NULL, 
                            titel character varying(255) NOT NULL, 
                            tekst text NOT NULL, 
                            teaser character varying(255) NOT NULL NOT NULL,
                            volgende character varying(255) NOT NULL, 
                            routing text,
                            first int NOT NULL,
                            last int NOT NULL,
                            CONSTRAINT artikel_pkey PRIMARY KEY (id), 
                            CONSTRAINT artikel_hoofdstuk_id_fkey 
                            FOREIGN KEY (hoofdstuk_id) REFERENCES hoofdstukken (id) MATCH SIMPLE)
            """
        executeQuery(cnx, q)
    else:
        print wetartdb, "bestaat"
        x
        
    if "artikel-kop" not in html:
        ts = str(html).split("</h3>")
        if len(ts)>0:
            ts = ts[1]
        else:
            ts = ts[0]
        teaser = remove_html(str(ts)).replace("\n", " ")    
        teaser = teaser.strip()
        teaser = teaser[0:250]
        teaser = make_chap_clean(teaser)
        style = open("style.txt", "r").read()        
        content='<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>'+style+'<body class="wettekst-inhoud">'+html+"</body></html>"           
        #content = tidy.parseString(str(content), **options)
        rh = RemoveLinks(None)    
        rh.feed(str(content))                
        content = rh.html        
        q="insert into artikel values ('"+str(global_artikelen)+"', '"+str(global_hoofdstukken)+"', '"+str(global_artikelen)+"', '"+wetbestand_shorttitel+"', '"+latin1_to_html(str(content)).replace("'", "''")+"', '"+latin1_to_html(str(teaser)).replace("'", "''")+"', 'artikeltekst', '', 0, 0)"                        
        executeQuery(cnx, q)
        cnx.commit()
        global_artikelen += 1        
        global_wetten+=1
        return
    
    found_chap = False
    soup = BeautifulSoup(html)       
    last_chapter = ''
    for i in soup.findAll("div"):
        chaps = i.findAll("h3")
        if len(chaps)>0:            
            #print "---------"
            #print chaps[0].contents[0]
            #print "---------"
            #print
            #print
            #try:
            #if "Koning" in chaps[0].contents[0]:
            #    print {'x':chaps[0].contents[0]}
            
            #print
            try:
                chap = chaps[len(chaps)-1].contents[0]
            except:
                chap = "chapter"
            chap = str(chap)
            
           #chap = chap.replace("0xa7", " ")
           # chap = chap.replace("\xa7", " ")
           # chap = chap.replace("\xc2", " ")
           # chap = chap.replace("\xa0", " ")
            #for i in range(0,10):
            #    chap = chap.replace("  ", " ")
            #print {'x':chap}
            #chap = chap.replace("\xab", "<<")
            #chap = chap.replace("\xbb", ">>")
            
            #print
            #print {'x':chap}
            chap = chap.encode("utf-8")
            #print {'x':chap}
            #chap = latin1_to_ascii(chap)
            chap = chap.strip()

            chap = make_chap_clean((chap))
            #if "Alleenstaande" in chap:
            #    print {'x':chap}
            #print "------------------------"
            
            #print chap, "Artikel" in chap or "Article" in chap
            if "Artikel" in chap or "Article" in chap:
                if not found_chap:
                    found_chap = True
                    global_hoofdstukken += 1                
                    q="insert into hoofdstukken values ('"+str(global_hoofdstukken)+"', '"+str(global_wetten)+"', '', '"+str(global_hoofdstukken)+"', '"+wetartdb.replace(".db", "")+"', 'Alle artikelen', '', 'artikel', 'YES')"
                    last_chapter = 'Alle artikelen'
                    executeQuery(cn, q)            
                artikelnummer = chap
            else:                 
                found_chap = True
                global_hoofdstukken += 1                
                q="insert into hoofdstukken values ('"+str(global_hoofdstukken)+"', '"+str(global_wetten)+"', '', '"+str(global_hoofdstukken)+"', '"+wetartdb.replace(".db", "")+"', '"+chap.replace("'", "''")+"', '', 'artikel', 'YES')"
                last_chapter = chap
                #print {'x':q}
                executeQuery(cn, q)            

            if "Artikel" in chap or "Article" in chap:
                ts = str(i).split("</h3>")
                if len(ts)>0:
                    ts = ts[1]
                else:
                    ts = ts[0]
                teaser = remove_html(str(ts)).replace("\n", " ")    
                teaser = teaser.strip()
                teaser = teaser[0:250]
                teaser = make_chap_clean(teaser)
                #print {'.':teaser}
                style = open("style.txt", "r").read()
                routing = wf + " / " + wetbestand_shorttitel.replace("'", "''")+" / "+last_chapter.replace("'", "''")+" / "+artikelnummer.replace(chap_indent, "").replace("'", "''")
                htmlrouting = "<div class='routing'>"+routing+"</div>"      
                content='<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>'+style+'<body class="wettekst-inhoud">'+str(i)+htmlrouting                
                #content = tidy.parseString(str(content), **options)
                rh = RemoveLinks(None)    
                rh.feed(str(content))                
                content = rh.html
                cnx = sqlite3.connect(db_dir+wetartdb)
                q="insert into artikel values ('"+str(global_artikelen)+"', '"+str(global_hoofdstukken)+"', '"+str(global_artikelen)+"', '"+artikelnummer.replace(chap_indent, "").replace("'", "''")+"', '"+latin1_to_html(str(content)).replace("'", "''")+"', '"+latin1_to_html(str(teaser)).replace("'", "''")+"', 'artikeltekst', '"+routing+"', 0, 0)"                
                executeQuery(cnx, q)
                cnx.commit()
                global_artikelen += 1   
            #except Exception, e:
            #    print e
            #    raise e
    global_wetten+=1
    
def parseWetten(cn, wettenfolder):
    global global_wetboekhoofdstuk    
    if os.path.isfile(wettenfolder):
        return
    #print wettenfolder
    wf = str(os.path.basename(wettenfolder))
    #print wf
    wf = wf[5:]
    #print wf
    q="insert into wetboekhoofdstuk values ('"+str(global_wetboekhoofdstuk)+"', '"+str(global_wetboekhoofdstuk)+"', '"+wf+"', 'wetboek', 0, 0)"
    executeQuery(cn, q)                
    for f in os.listdir(wettenfolder):
        if ".svn" not in f:    
            ParseWetHTML(cn, wettenfolder, f, wf)
    global_wetboekhoofdstuk+=1                    

def parseWettenFolder(wettenfolder, cn):
    for f in os.listdir(wettenfolder):
        if ".svn" not in f:
            parseWetten(cn, os.path.join(wettenfolder, f))
    
def updateHoofdstukken(cn):
    c = cn.cursor()
    c.execute('select id, artikelbestand from hoofdstukken')
    for row in c:
        x = db_dir+row[1]+".db"
        cnx = sqlite3.connect(x)         
        c2 = cnx.cursor()
        c2.execute("select id from artikel where hoofdstuk_id='"+str(row[0])+"'")
        ids = c2.fetchall()
        if len(ids)==0:
            executeQuery(cn, "update hoofdstukken set bevatartikelen='NO' where id='"+str(row[0])+"'")
            sys.stdout.write(".")
            sys.stdout.flush()
    print

def updateHoofdstukken2(cn):
    # Deze hoofdstukken hebben geen directe kinderen maar fungeren later als een section
    c = cn.cursor()
    c.execute('select * from hoofdstukken')
    l = []
    for row in c:
        l.append(row)
    c =0
    while c<len(l):
        if l[c][8]=="NO":
            assignid=l[c][0]
            c += 1 
            if c<len(l):
                while l[c][8]!="NO":
                    q = "update hoofdstukken set hoofdstuk_id='"+str(assignid)+"' where id='"+str(l[c][0])+"'"
                    #print q
                    executeQuery(cn, q)
                    c += 1
                    if len(l)<=c:
                        break
            c=c-1
        c += 1 
        sys.stdout.write(".")
        sys.stdout.flush()           
    cn.commit()           
    print 

def insert_article_chapters(maindatabase, mainquery):
    print "correcting", mainquery
    mc = sqlite3.connect(maindatabase).cursor()
    cn = sqlite3.connect(maindatabase)
    c = cn.cursor()
    mc.execute("SELECT max(id) FROM hoofdstukken");
    currentmax=mc.fetchall()[0][0]
    mc.execute(mainquery);
    for r in mc:
        r2 = copy.deepcopy(r)
        r2 = list(r2)
        currentmax += 1
        r2[0] = currentmax   
        r2[5] = "Alle artikelen"
        s = str(r2)
        s=s.replace("[", "(").replace("]", ")").replace(", u'",", '")
        q = "insert into hoofdstukken values "+s
        c.execute(q)
        q = "update hoofdstukken set bevatartikelen='NO', hoofdstuk_id='"+str(currentmax)+"' where id='"+str(r[0])+"'"
        c.execute(q)        
        cn2 = sqlite3.connect(db_dir+r[4]+".db")
        c2 = cn2.cursor()
        q = "update artikel set hoofdstuk_id='"+str(currentmax)+"' WHERE hoofdstuk_id =  '"+str(r[0])+"'"
        c2.execute(q)
        cn2.commit()
    cn.commit()
      
def get_hoofdstuk_subtitle(l):
    if len(l)==0:
        return "Geen artikelen"
    l2 = []
    for i in l:
        l2.append(i[0].replace("Artikel ", "").replace("Article ", ""))   
    if l2[0][0:15]==l2[len(l2)-1][0:15]:
        return "Artikel "+l2[0][0:15]
    return "Artikel "+l2[0][0:15]+" t/m "+l2[len(l2)-1][0:15]

def get_subtitels_hfst(maindatabase):
    q = "SELECT id, artikelbestand FROM hoofdstukken"
    c = sqlite3.connect(maindatabase)
    mc = c.cursor()    
    mc.execute(q)
    for r in mc:
        mc2 = sqlite3.connect(maindatabase.replace("wetten", r[1])).cursor()
        q = "select titel from artikel where hoofdstuk_id="+str(r[0])
        mc2.execute(q)
        l = []
        for r2 in mc2:
            l.append(r2)
        q = "update hoofdstukken set subtitel='"+get_hoofdstuk_subtitle(l)+"' where id="+str(r[0])
        sys.stdout.write(".")
        sys.stdout.flush()                   
        executeQuery(c, q)
    c.commit()
    print
    
def update_afkos(maindatabase):
    q = "SELECT * FROM wetboek WHERE afk=''"
    c = sqlite3.connect(maindatabase)
    mc = c.cursor()    
    mc2 = c.cursor()    
    mc.execute(q)
    for r in mc:
        s = r[3].split(" ")
        if len(s)==1:
            afk=r[3][0:4]
        elif len(s)>1:
            afk=''
            for i in s:
                if len(i)>0:
                    afk += i[0]
        q = "update wetboek set afk='"+afk+"' where id="+str(r[0])
        print q
        mc2.execute(q)
    c.commit()

def clip_empty_sections(maindatabase):         
    q = "SELECT id FROM wetboek"
    c = sqlite3.connect(maindatabase)
    mc = c.cursor()        
    mc.execute("DELETE FROM hoofdstukken WHERE hoofdstuk_id =  ''  and bevatartikelen='NO' and id not in (select hoofdstuk_id from hoofdstukken)")
    c.commit()
    
def set_first_last(maindatabase):
   db = sqlite3.connect(maindatabase)
   mc = db.cursor()
   q = "UPDATE wetboekhoofdstuk set last=0, first=1 where id=(select id from wetboekhoofdstuk order by sequence limit 1)"
   mc.execute(q)
   q = "UPDATE wetboekhoofdstuk set last=1, first=0 where id=(select id from wetboekhoofdstuk order by sequence desc limit 1)"
   mc.execute(q)
   db.commit()
   
   q = "UPDATE wetboek  set last=0, first=1 where id in (SELECT id FROM wetboek ORDER BY SEQUENCE limit 1)"       
   mc.execute(q)
   q = "UPDATE wetboek  set last=1, first=0 where id in (SELECT id FROM wetboek ORDER BY SEQUENCE DESC limit 1)"       
   mc.execute(q)
 
   db.commit()           
   q = "SELECT DISTINCT(artikelbestand) FROM hoofdstukken"   
   mc.execute(q)
   for r in mc:
       artdb = db_dir+r[0]+".db"
       artdb = sqlite3.connect(artdb)
       artdbc = artdb.cursor()
       artdbc.execute("update artikel set last=0, first=1 where id=(select id from artikel order by sequence limit 1)")       
       artdbc.execute("update artikel set last=1, first=0 where id=(select id from artikel order by sequence desc limit 1)")
       artdb.commit()
    

class RemoveHTML(HTMLParser):
    def __init__ (self):
        HTMLParser.__init__(self)
        self.html = ""      
    def handle_data(self, data):
        if "CDATA" not in data:
            self.html += data        
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):        
        pass  
    
def executeQuery(cn, q):
    curs = cn.cursor()
    try:   
        curs.execute(q)
    except Exception, e:
        print {'x':q}
        raise e

def capitalize_first_letter(steekwoord):
    steekwoord = steekwoord.lower()
    steekwoord2 = ""
    f = True
    if len(steekwoord)>1:
        for i in steekwoord:
            if f:
                steekwoord2 += i.upper()
                f = False
            else:
                steekwoord2 += i
    return steekwoord2
    
def make_cPickle_search():    
    maindatabase = db_dir+'wetten.db'
    artikelbestanden = []
    d = {}
    cn = sqlite3.connect(maindatabase)
    c = cn.cursor()
    c.execute("select distinct(artikelbestand) from hoofdstukken")
    cn.commit()
    htmlcontentfiles = []
    for i in c:
        artikelbestanden.append(i)        
    c.execute("select distinct(volgende), titel from wetboek where volgende!='hoofdstukken'")
    cn.commit()
    for i in c:
        htmlcontentfiles.append(i[0])        
        artikelbestanden.append(i)        
    cnt = 0        
    for i in artikelbestanden:
        qtitel = "SELECT distinct(wetboek.titel) FROM hoofdstukken, wetboek where wetboek_id=wetboek.id and artikelbestand='"+i[0]+"'"
        cntitel = sqlite3.connect(maindatabase).cursor().execute(qtitel)
        titel = tp = "Geen titel gevonden"
        for t in cntitel:
            titel = t[0]
        if titel==tp:
            if len(i)>1:
                titel = i[1]
        dbfile = db_dir+str(i[0])+'.db'
        cn = sqlite3.connect(dbfile)
        c2 = cn.cursor()
        c2.execute("select * from artikel")
        tempbuf = ''
        tempbuf2 = ''
        for j in c2:    
            rh = RemoveHTML()
            rh.feed(j[4])            
            html = rh.html
            tempbuf = html
            html = html.replace("\t", " ")
            html = html.replace("\n", " ")
            html = html.replace(".", " ")
            html = html.replace("-", " ")            
            for k in range(0,20):
                html = html.replace("  ", " ")
            subber = re.compile(r"[^A-Za-z0-9 ]").sub            
            html = subber("", html).strip()
            html = html.split(" ")      
            tempbuf2 = html
            for l in html:
                stripped = l.strip()
                stripped = capitalize_first_letter(stripped)                
                if len(stripped)!=0:         
                    #if stripped=="Aanartikel":
                    #    print tempbuf
                    #    print tempbuf2
                    #    x
                    if i[0] in htmlcontentfiles:                    
                        data = (dbfile, j[0], titel, "Tekst")
                    else:                    
                        data = (dbfile, j[0], titel, j[3])                        
                    try:
                        d[stripped].add(data)
                    except Exception, e:
                        d[stripped] = set()
                        d[stripped].add(data)            
            if cnt%100==0:
                sys.stdout.write(".")
                sys.stdout.flush()
            cnt += 1
    print
    open("datasearch.pickle", "w").write(cPickle.dumps(d))
    
def insert_items_search_tables():    
    maindatabase = db_dir+'wetten.db'
    cn = sqlite3.connect(maindatabase)
    try:
        executeQuery(cn, "DROP TABLE searchindex;")
    except:
        pass
    try:
        executeQuery(cn, "DROP TABLE herkomst;")
    except:
        pass    
    q = """
CREATE TABLE searchindex
(
  id SERIAL NOT NULL,
  steekwoord character varying(255) NOT NULL,
  CONSTRAINT pk_id PRIMARY KEY (id)
);
"""
    executeQuery(cn, q)
    q = """
    CREATE UNIQUE INDEX searchindex_steekwoord ON searchindex(steekwoord);
    """
    executeQuery(cn, q)
    q = """
CREATE TABLE herkomst
(
  id SERIAL NOT NULL,
  searchindex_id INTEGER NOT NULL,
  titel character varying(255),
  boek character varying(255),
  artikel integer,
  subtitel character varying(255),  
  CONSTRAINT pk_steekwoord PRIMARY KEY (id)
  CONSTRAINT fkey_searchindex FOREIGN KEY (searchindex_id) REFERENCES searchindex (id) MATCH SIMPLE
);
    """    
    executeQuery(cn, q)
    q = """
    CREATE INDEX searchindex_searchindex_id ON herkomst(searchindex_id);
    """    
    executeQuery(cn, q)    
    cn.commit()    
    d = cPickle.loads(open("datasearch.pickle", "r").read())    
    
    sic = 0
    hkc = 0
    for i in d:        
        l = list(d[i])
        steekwoord = str(i)
        q = "insert into searchindex values ('"+str(sic)+"', '"+steekwoord.replace("'", "''")+"');"
        executeQuery(cn, q)        
        for j in l:
            boek = os.path.basename(j[0].split(".")[0])
            q = "insert into herkomst values ('"+str(hkc)+"', '"+str(sic)+"', '"+str(j[2]).replace("'", "''")+"', '"+str(boek).replace("'", "''")+"', '"+str(j[1]).replace("'", "''")+"', '"+str(j[3]).replace("'", "''")+"');"
            #print j[3]
            executeQuery(cn, q)
            hkc += 1
        sic += 1
        if hkc%100==0:
            sys.stdout.write("*")
            sys.stdout.flush()
            
    cn.commit()
    print
    print len(d)

def check_sizes(wettenfolder):
    files = []
    for f in os.listdir(wettenfolder):
        if ".svn" not in f and ".DS_Store" not in f:    
            for f2 in os.listdir(wettenfolder+"/"+f):
                if ".svn" not in f2 and ".DS_Store" not in f2:
                    files.append( wettenfolder+"/"+f+"/"+f2)
    for f in files:        
        c = open(f, "r").read()
        if len(c)<14000:
            c = c.replace("artikel-kop", "artikel-kp")
            print "replacing:", f
        open(f, "w").write(c)

def main():    
    wettenfolder = "RawData/politiebundel"
    #wettenfolder = "WettenHTML2009"
    #wettenfolder = "WettenTest"
    
    maindatabase = db_dir+'wetten.db'
    bookmarkdb =  db_dir+'bookmarks.db'

    if os.path.exists(maindatabase):        
        os.system("rm "+db_dir+"*.db")
    
    check_sizes(wettenfolder)

    cn = sqlite3.connect(maindatabase)       

     
    q = """
CREATE TABLE wetboekhoofdstuk(id serial NOT NULL, 
                              sequence integer NOT NULL, 
                              titel character varying(255) NOT NULL, 
                              volgende character varying(255) NOT NULL, 
                              first int NOT NULL,
                              last int NOT NULL,                                                 
                              CONSTRAINT wetboekhoofdstuk_pkey PRIMARY KEY (id))
"""
    executeQuery(cn, q)    
    
    q = """
CREATE TABLE wetboek(id serial NOT NULL, 
                    wetboekhoofdstuk_id integer NOT NULL, 
                    sequence integer NOT NULL, 
                    titel character varying(1024) NOT NULL, 
                    longtitel character varying(1024) NOT NULL, 
                    volgende character varying(255) NOT NULL, 
                    afk character varying(255) NOT NULL,
                    first int NOT NULL,
                    last int NOT NULL,                    
                    CONSTRAINT wetboek_pkey PRIMARY KEY (id) 
                    FOREIGN KEY (wetboekhoofdstuk_id) REFERENCES wetboekhoofdstuk (id) MATCH SIMPLE)
"""
                                
    executeQuery(cn, q)
    q = "CREATE UNIQUE INDEX wetboektitel_index ON wetboek(titel);"
    executeQuery(cn, q)
    q = "CREATE UNIQUE INDEX wetboeklongtitel_index ON wetboek(longtitel);"
    executeQuery(cn, q)    
    q = "CREATE INDEX wetboekafk_index ON wetboek(afk);"
    executeQuery(cn, q)    

    q = """
CREATE TABLE hoofdstukken(id serial NOT NULL, 
                          wetboek_id integer, 
                          hoofdstuk_id integer, 
                          sequence integer NOT NULL, 
                          artikelbestand character varying(1024) NOT NULL, 
                          titel character varying(1024) NOT NULL, 
                          subtitel character varying(255), 
                          volgende character varying(255) NOT NULL, 
                          bevatartikelen character varying(3) NOT NULL, 
                          CONSTRAINT hoofdstukken_pkey PRIMARY KEY (id),
                          CONSTRAINT hoofdstukken_wetboek_id_fkey FOREIGN KEY (wetboek_id) REFERENCES wetboek (id) MATCH SIMPLE,
                          CONSTRAINT hoofdstukken_hoofdstuk_id_fkey FOREIGN KEY (hoofdstuk_id) REFERENCES hoofdstuk (id) MATCH SIMPLE)
"""
    executeQuery(cn, q)
    q = "CREATE INDEX hoofdstukkentitel_index ON hoofdstukken(titel);"
    executeQuery(cn, q) 
    q = "CREATE INDEX hoofdstukkensubtitel_index ON hoofdstukken(subtitel);"
    executeQuery(cn, q) 
        
    parseWettenFolder(wettenfolder, cn)
    
    print "done, committing to disk"
    cn.commit()
     
    print "updating tree"
    cn = sqlite3.connect(maindatabase)
    updateHoofdstukken(cn)
    cn.commit()

    print "updating tree again"
    cn = sqlite3.connect(maindatabase)
    executeQuery(cn, "update hoofdstukken set hoofdstuk_id=''")
    updateHoofdstukken2(cn)
    cn.commit()
        
    insert_article_chapters(maindatabase, "SELECT * FROM hoofdstukken WHERE titel LIKE  'Titel%' and bevatartikelen='YES'")
    insert_article_chapters(maindatabase, "SELECT * FROM hoofdstukken WHERE titel LIKE  'Hoofdstuk%' and bevatartikelen='YES'")
    insert_article_chapters(maindatabase, "SELECT * FROM hoofdstukken WHERE titel LIKE  'Lijst%' and bevatartikelen='YES'")
   
    get_subtitels_hfst(maindatabase)    
    update_afkos(maindatabase)
    clip_empty_sections(maindatabase)
    set_first_last(maindatabase)    

    make_cPickle_search()
    insert_items_search_tables()

    
if __name__=="__main__":
    main()

