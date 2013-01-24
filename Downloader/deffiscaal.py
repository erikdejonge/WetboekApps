from wetten import *

def structure():
    d = {}

    d["001. Algemeen"] = [BWBR0002448(), # Algemene termijnenwet
                          BWBR0005537(), # Algemene wet bestuursrecht
                          BWBR0002320(), # Algemene wet inzake rijksbelastingen
                          BWBR0006358()] # Besluit proceskosten bestuursrecht
    d["002. Dividendbelasting"] = [BWBR0002517(), # Uitvoeringsbeschikking dividendbelasting 1965
                                   BWBR0002515()] # Wet op de dividendbelasting 1965
    d["003. Douane"] = [BWBR0023746()] # Algemene douanewet
    d["004. Inkomstenbelasting"] = [BWBR0012066(), # Uitvoeringsbesluit inkomstenbelasting 2001
                                    BWBR0012031(), # Uitvoeringsregeling inkomstenbelasting 2001
                                    BWBR0018053(), # Wet aanpassing fiscale behandeling VUT/prepensioen
                                    BWBR0011353(), # Wet inkomstenbelasting 2001
                                    BWBR0004537(), # Wet invoering en aanvulling van de vereenvoudiging
                                    BWBR0003600(), # Wet tijdelijke maatregelen inzake aftrekbaarheid v
                                    BWBR0004536()] # Wet vereenvoudiging tariefstructuur en aftrekposte
    d["005. Invordering"] = [BWBR0004770(), # Invorderingswet 1990
                             BWBR0002645(), # Kostenwet invordering rijksbelastingen
                             BWBR0004772(), # Uitvoeringsbesluit Invorderingswet 199
                             BWBR0004766()] # Uitvoeringsregeling Invorderingswet 1990
    d["006. Kansspelbelasting"] = [BWBR0002363(), # Uitvoeringsbeschikking kansspelbelasting
                                   BWBR0002359()] # Wet op de kansspelbelasting   
    d["007. Loonbelasting"] = [BWBR0002489(), # Uitvoeringsbesluit loonbelasting 1965
                               BWBR0007780(), # Uitvoeringsregeling afdrachtvermindering
                               BWBR0012059(), # Uitvoeringsregeling loonbelasting 2001
                               BWBR0006305(), # Uitvoeringsregeling werknemersspaarregelingen en w
                               BWBR0002471(), # Wet op de loonbelasting 1964
                               BWBR0007892(), # Wet uitbreiding loondoorbetalingsplicht bij ziekte
                               BWBR0017839(), # Wet uitbreiding rechtsgevolgen VAR
                               BWBR0007746()] # Wet vermindering afdracht loonbelasting en premie
    d["008. Millieubelasting"] = [BWBR0007159(), # Uitvoeringsregeling belastingen op milieugrondslag
                                  BWBR0007168(), # Wet belastingen op milieugrondslag
                                  BWBR0005564()] # Wet verbruiksbelastingen van brandstoffen, geheven 
    d["009. Motorrijtuigenbelasting"] = [BWBR0004912(), # Besluit gemeentelijke parkeerbelastingen
                                         BWBR0007310(), # Invoeringswet Wet op de motorrijtuigenbelasting 19
                                         BWBR0005807(), # Uitvoeringsbesluit belasting van personenauto's en
                                         BWBR0007679(), # Uitvoeringsbesluit belasting zware motorrijtuigen
                                         BWBR0007311(), # Uitvoeringsbesluit motorrijtuigenbelasting 1994
                                         BWBR0005813(), # Uitvoeringsregeling belasting van personenauto's e
                                         BWBR0007308(), # Uitvoeringsregeling motorrijtuigenbelasting 1994
                                         BWBR0007678(), # Wet belasting zware motorrijtuigen
                                         BWBR0005806(), # Wet op de belasting van personenauto's en motorrij
                                         BWBR0006324()] # Wet op de motorrijtuigenbelasting 1994
    d["010. Omzetbelasting"] = [BWBR0002636(), # Besluit uitsluiting aftrek omzetbelasting 1968
                                BWBR0002634(), # Uitvoeringsbeschikking omzetbelasting 1968
                                BWBR0002633(), # Uitvoeringsbesluit omzetbelasting 1968
                                BWBR0002629(), # Wet op de omzetbelasting 1968
                                BWBR0013817()] # Wet op het BTW-compensatiefonds
    d["011. Onroerende goederen"] = [BWBR0007142(), # Uitvoeringsregeling uitgezonderde objecten Wet waa
                                     BWBR0007119()] # Wet waardering onroerende zaken
    d["012. Rechtsverkeer"] = [BWBR0002739(), # Registratiewet 1970
                               BWBR0002770(), # Uitvoeringsbesluit belastingen van rechtsverkeer
                               BWBR0002740()] # Wet op belastingen van rechtsverkeer
    d["013. Successiewet"] = [BWBR0001939(), # Natuurschoonwet 1928
                              BWBR0002226(), # Successiewet 1956
                              BWBR0002227(), # Uitvoeringsbesluit Successiewet 1956
                              BWBR0003746()] # Uitvoeringsregeling Successiewet 1956
    d["014. Venootschapsbelasting"] = [BWBR0014483(), # Besluit fiscale eenheid 2003
                                       BWBR0002784(), # Uitvoeringsbeschikking vennootschapsbelasting 1971
                                       BWBR0002786(), # Uitvoeringsbesluit vennootschapsbelasting 1971
                                       BWBR0002782(), # Vrijstellingsbesluit vennootschapsbelasting
                                       BWBR0002672(), # Wet op de vennootschapsbelasting 1969
                                       BWBR0004412()] # Wet tot verlaging tarief en op nihil stellen vermo
    return d
    
if __name__=="__main__":
    print structure()