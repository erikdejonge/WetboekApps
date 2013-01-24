
import os
import sys
import marshal

d = marshal.load(open("wetten.marshal", "r"))

def latin1_to_ascii (unicrap):
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
        0xb1:'{+/-}', 0xb2:'{^2}', 0xb3:'{^3}', 0xb4:"'",
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

def convert():
    c = open("wetten.txt", "r").read()
    d = eval(c)
    marshal.dump(d, open("wetten.marshal", "w"))
    
def printoutput2(i, afk):
    if type(i["CiteertitelLijst"]["Citeertitel"])==type([]):
        titels = ""
        for k in i["CiteertitelLijst"]["Citeertitel"]:
            titels += k["titel"]["value"]
            break
        #print i["BWBId"]["value"],"|", afk,"|", titels
        print
        print "def", str(i["BWBId"]["value"]+"():").replace(".", ""), "#", latin1_to_ascii(titels)[0:50]
        print '\treturn make_dict("'+afk+'", "'+i["BWBId"]["value"]+'", "'+latin1_to_ascii(titels).replace('"', "'")+'")'
    else:
        #print i["BWBId"]["value"],"|", afk,"|", i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"]
        print
        print "def", str(i["BWBId"]["value"]+"():").replace(".", ""), "#", latin1_to_ascii(i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"])[0:50]
        print '\treturn make_dict("'+afk+'", "'+i["BWBId"]["value"]+'", "'+latin1_to_ascii(i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"]).replace('"', "'")+'")'

def printoutput(i, afk):
    if type(i["CiteertitelLijst"]["Citeertitel"])==type([]):
        titels = ""
        for k in i["CiteertitelLijst"]["Citeertitel"]:
            titels += k["titel"]["value"]+", "
        #print i["BWBId"]["value"],"|", afk,"|", titels
        print str(i["BWBId"]["value"]+"()").replace(".", "")+",", "#", latin1_to_ascii(titels)[0:50]
    else:
        #print i["BWBId"]["value"],"|", afk,"|", i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"]
        print str(i["BWBId"]["value"]+"()").replace(".", "")+",", "#", latin1_to_ascii(i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"])[0:50]
                      
def getafkorting(i):
    afk = ''
    if i.has_key("AfkortingLijst"):
        #print "----", i["AfkortingLijst"]
        if i["AfkortingLijst"].has_key("Afkorting"):
            if type(i["AfkortingLijst"]["Afkorting"])==type([]):
                for k in i["AfkortingLijst"]["Afkorting"]:
                    afk += k["value"]+" "
            else:
                afk += i["AfkortingLijst"]["Afkorting"]["value"]
    if afk.strip()=="":
        afk = "afk."
    return afk
        
             
def search(query):
    d2 = d['BWBIdServiceResultaat']
    d3 = d2["RegelingInfoLijst"]
    wettenlijst = d3["RegelingInfo"]
    l = wettenlijst
    notfound = True

    print "afkortingen doorzoeken"
    for i in l:
        if i.has_key("OfficieleTitel"):
            if i["OfficieleTitel"].has_key("value"):
                afk = getafkorting(i)
                if query.lower() in afk.lower():
                    notfound = False
                    printoutput(i, afk)                        

    if notfound:
        print "citeertitels doorzoeken"        
        for i in l:
            titels = []
            if type(i["CiteertitelLijst"]["Citeertitel"])==type([]):
                tit = ""
                for t in i["CiteertitelLijst"]["Citeertitel"]:
                    tit += t["titel"]["value"]
                titels.append(tit)
            else:
                titels.append(i["CiteertitelLijst"]["Citeertitel"]["titel"]["value"])
            for t in titels:            
                if query.lower() in t.lower():
                    notfound = False
                    afk = getafkorting(i)                            
                    printoutput(i, afk)
                                  
    if notfound:
        print "volledige titels doorzoeken"            
        for i in l:     
            if i.has_key("OfficieleTitel"):
                if i["OfficieleTitel"].has_key("value"):
                    if query.lower() in i["OfficieleTitel"]["value"].lower():
                        afk = getafkorting(i)
                        if afk.strip()=="":
                            afk = "afk."
                        printoutput(i, afk) 
    if notfound:
        print "zoeken op code"
        for i in l:             
            if query.lower()==i["BWBId"]["value"].lower():
                afk = getafkorting(i)
                printoutput(i, afk)
            
def main2():
    d2 = d['BWBIdServiceResultaat']
    d3 = d2["RegelingInfoLijst"]
    wettenlijst = d3["RegelingInfo"]
    l = wettenlijst
    
    for i in l:
       afk = getafkorting(i)
       printoutput(i, afk)
        
def main():
    x="n"
    while True: 
        sys.stdout.write ("> ")
        x = raw_input()
        if x!='q' and x!='exit' and x!='quit':
            if x.strip()!='':
                search(x)
        else:
            break

if __name__=="__main__":
    main()