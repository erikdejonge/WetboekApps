from wetten import *

def structure():
    d = {}
    d["001. Grondwet"] = [BWBR0001840()] # Grondwet
    d["002. Verdragen"] = [BWBV0001507(), # Verdrag betreffende de Europese Unie, Maastricht
                           BWBV0001506()] # Verdrag tot oprichting van de Europese Gemeenschap
    d["003. Wetten"] = [BWBR0006502(), # Algemene wet gelijke behandeling
                        BWBR0002320(), # Algemene wet inzake rijksbelastingen
                        BWBR0001886(), # Auteurswet 1912, Aut 
                        BWBR0002656(), # Burgerlijk Wetboek Boek 1
                        BWBR0002761(), # Burgerlijk Wetboek Boek 4
                        BWBR0005290(), # Burgerlijk Wetboek Boek 7
                        BWBR0005416(), # Gemeentewet, Gemeentewet,
                        BWBR0003738(), # Rijkswet op het Nederlanderschap
                        BWBR0011823(), # Vreemdelingenwet 2000
                        BWBR0006622(), # Wegenverkeerswet 1994          
                        BWBR0001854(), # Wetboek van Strafrecht
                        BWBR0005252()] # Wet openbaarheid van bestuur
    return d
    
if __name__=="__main__":
    print structure()