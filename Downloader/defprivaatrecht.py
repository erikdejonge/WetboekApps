from wetten import *

def structure():
    d = {}
    d["001. Burgerlijk wetboek"] = [BWBR0002656(), # Burgerlijk Wetboek Boek 1
                                    BWBR0003045(), # Burgerlijk Wetboek Boek 2
                                    BWBR0005291(), # Burgerlijk Wetboek Boek 3
                                    BWBR0002761(), # Burgerlijk Wetboek Boek 4
                                    BWBR0005288(), # Burgerlijk Wetboek Boek 5
                                    BWBR0005289(), # Burgerlijk Wetboek Boek 6
                                    BWBR0005290(), # Burgerlijk Wetboek Boek 7
                                    BWBR0006000(), # Burgerlijk Wetboek Boek 7A
                                    BWBR0005034(), # Burgerlijk Wetboek Boek 8
                                    BWBR0005048(), # Invoeringswet Boeken 3, 5 en 6 nieuw B.W.
                                    BWBR0002565()] # Overgangswet nieuw Burgerlijk Wetboek                                    
    d["002. Semi-burgerlijk recht en overige wetgeving"] = [BWBR0020417(), # Besluit marktmisbruik Wft
                                                            BWBR0020416(), # Besluit melding zeggenschap en kapitaalbelang in u
                                                            BWBR0022511(), # Besluit openbare biedingen Wft
                                                            BWBR0002014(), # Buitengewoon Besluit Arbeidsverhoudingen 1945
                                                            BWBR0002896(), # Colportagewet
                                                            BWBR0013797(), # Embryowet
                                                            BWBR0001860(), # Faillissementswet
                                                            BWBR0004541(), # Kadasterwet
                                                            BWBR0003403(), # Leegstandwet, Leegstandwet
                                                            BWBR0004045(), # Werkloosheidswet
                                                            BWBR0013642(), # Wet donorgegevens kunstmatige bevruchting
                                                            BWBR0003109(), # Wet giraal effectenverkeer
                                                            BWBR0003026(), # Wet melding collectief ontslag
                                                            BWBR0002524(), # Wet op de arbeidsongeschiktheidsverzekering
                                                            BWBR0001937(), # Wet op de collectieve arbeidsovereenkomst
                                                            BWBR0008508(), # Wet op de Europese ondernemingsraden
                                                            BWBR0002698(), # Wet op de loonvorming
                                                            BWBR0002747(), # Wet op de ondernemingsraden
                                                            BWBR0001987(), # Wet op het algemeen verbindend en het onverbindend
                                                            BWBR0020368()] # Wet op het financieel toezicht
    d["003. Wet op de rechterlijke organisatie e.a."] = [BWBR0001830(), # Wet op de rechterlijke organisatie
                                                         BWBR0002093(), # Advocatenwet
                                                         BWBR0013129(), # Besluit nevenvestigings- en nevenzittingsplaatsen
                                                         BWBR0012197(), # Gerechtsdeurwaarderswet
                                                         BWBR0003030(), # Reglement voor de bijzondere kamer bij het gerechtshof te Arnhem
                                                         BWBR0010388(), # Wet op het notarisambt
                                                         BWBR0008365()] # Wet rechtspositie rechterlijke ambtenaren
    d["004. Wetboek van burgerlijke rechtsvordering e.a."] = [BWBR0001827(), # Wetboek van burgerlijke rechtsvordering
                                                              BWBR0006368(), # Wet op de rechtsbijstand
                                                              BWBR0001852(), # Wet tarieven in burgerlijke zaken
                                                              BWBR0002430()] # Besluit tarieven in burgerlijke zaken
    d["005. Wetboek van koophandel e.a."]= [BWBR0001838(), # Wetboek van Koophandel
                                            BWBR0021777(), # Handelsregisterwet 2007
                                            BWBR0024067(), # Handelsregisterbesluit 2008
                                            BWBR0008691(), # Mededingingswet
                                            BWBR0002415()] # Wet aansprakelijkheidsverzekering motorrijtuigen
    d["006. Intellectueel eigendom"] = [BWBR0001886(), # Auteurswet
                                        BWBR0005921(), # Wet op de naburige rechten
                                        BWBR0001906(), # Handelsnaamwet
                                        BWBR0007118(), # Rijksoctrooiwet 1995
                                        BWBV0001716()] # Beneluxverdrag inzake de intellectuele eigendom (merken en tekeningen of modellen)
    return d
    
if __name__=="__main__":
    print structure()