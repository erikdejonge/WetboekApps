from wetten import *

def structure():
    d = {}
    d["001. Besluiten"] = [BWBR0020421(), # Besluit Gedragstoezicht financiele ondernemingen W
                           BWBR0002459(), # Besluit kennisgevingen aansprakelijkheidsverzekeri
                           BWBR0020420(), # Besluit prudentiele regels Wft
                           BWBR0002601(), # Besluit uitvoering afwikkeling liquidatieuitkering
                           BWBR0020536()] # Vrijstellingsregeling Wft
                           
    d["002. Wetten"] = [BWBR0005290(), # Burgerlijk Wetboek Boek 7
                        BWBR0020809(), # Pensioenwet
                        BWBR0006622(), # Wegenverkeerswet 1994
                        BWBR0002976(), # Wet aansprakelijkheid olietankschepen
                        BWBR0002415(), # Wet aansprakelijkheidsverzekering motorrijtuigen
                        BWBR0002524(), # Wet op de arbeidsongeschiktheidsverzekering
                        BWBR0001827(), # Wetboek van Burgerlijke Rechtsvordering
                        BWBR0020368(), # Wet op het financieel toezicht
                        BWBR0006509(), # Wet toezicht verzekeringsbedrijf 1993
                        BWBR0019057(), # Wet werk en inkomen naar arbeidsvermogen
                        BWBR0018450()] # Zorgverzekeringswet
    return d
    
if __name__=="__main__":
    print structure()