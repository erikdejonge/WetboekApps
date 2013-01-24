from wetten import *

def structure():
    d = {}
    d["001. Besluiten"] = [BWBR0002838(), # Besluit aanvulling omschrijving slijtersbedrijf
                           BWBR0017606(), # Besluit bestuurlijke boete Drank- en Horecawet
                           BWBR0014964(), # Besluit BIBOB
                           BWBR0011700(), # Besluit eisen inrichtingen Drank- en Horecawet
                           BWBR0010673(), # Besluit eisen zedelijk gedrag Drank- en Horecawet
                           BWBR0007689(), # Besluit kennis en inzicht sociale hygiene Drank- e
                           BWBR0023770(), # Besluit uitvoering rookvrije werkplek, horeca en a
                           BWBR0011373(), # Speelautomatenbesluit 2000
                           BWBR0007953()] # Vrijstellingenbesluit Winkeltijdenwet      
    d["002. Regelingen"] = [BWBR0007743(), # Regeling aanvraaggegevens en formulieren Drank- en
                            BWBR0007742()] # Regeling bewijsstukken sociale hygiene Drank- en H
    d["003. Wetten"] = [BWBR0002458(), # Drank- en Horecawet
                        BWBR0004302(), # Tabakswet
                        BWBR0003245(), # Wet milieubeheer
                        BWBR0002063(), # Wet op de economische delicten
                        BWBR0002469(), # Wet op de kansspelen
                        BWBR0007636(), # Wijzigingswet Drank- en Horecawet, enz.
                        BWBR0007952(), # Winkeltijdenwet
                        BWBR0005181()] # Woningwet
    return d
    
if __name__=="__main__":
    print structure()