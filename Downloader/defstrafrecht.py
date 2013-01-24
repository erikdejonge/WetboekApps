from wetten import *

def structure():
    d = {}
    d["001. Strafrecht"] = [BWBR0001855(), # Invoeringswet Wetboek van Strafrecht
                               BWBR0001854(), # Wetboek van Strafrecht 
                               BWBR0015252(), # Wet internationale misdrijven
                               BWBR0002063(), # Wet op de economische delicten
                               BWBR0008804(), # Wet wapens en munitie
                               BWBR0001941()] # Opiumwet
    d["002. Bijzonder strafrecht"] = [BWBR0009640(), # Flora- en faunawet
                                      BWBR0005662(), # Gezondheids- en welzijnswet voor dieren
                                      BWBR0002320()] # Algemene wet inzake rijksbelastingen    
    d["003. Strafvordering"] = [BWBR0006763(), # Algemene wet op het binnentreden
                                   BWBR0010975(), # Besluit bewaren en vernietigen niet-gevoegde stukken
                                   BWBR0019359(), # Besluit getuigenbescherming
                                   BWBR0006664(), # Transactiebesluit 1994
                                   BWBR0026117(), # Besluit politiegegevens bijzondere opsporingsdiens
                                   BWBR0016664(), # Overleveringswet
                                   BWBR0025038(), # Regeling periodieke audit politiegegevens
                                   BWBR0002559(), # Uitleveringswet
                                   BWBR0017212(), # Wet DNA-onderzoek bij veroordeelden, Wet DNA-onder
                                   BWBR0014194(), # Wet justitiele en strafvorderlijke gegevens, Wet j
                                   BWBR0004244(), # Wet op de inlichtingen- en veiligheidsdiensten
                                   BWBR0004028(), # Wet overdracht tenuitvoerlegging strafvonnissen
                                   BWBR0024282(), # Wet ter voorkoming van witwassen en financieren va
                                   BWBR0001903()] # Wetboek van Strafvordering
    d["004. Penitentiair"] = [BWBR0008765(), # Beginselenwet verpleging ter beschikking gestelden
                              BWBR0008690(), # Reglement verpleging ter beschikking gestelden
                              BWBR0012110(), # Geweldsinstructie inrichtingen voor TBS-gestelden
                              BWBR0009709(), # Penitentiaire beginselenwet
                              BWBR0009398()] # Penitentiaire maatregel
    d["005. Verkeer"] = [BWBR0004826(), # Besluit administratieve bepalingen inzake het wegv
                         BWBR0008805(), # Besluit alcoholonderzoeken
                         BWBR0025554(), # Besluit voertuigen,
                         BWBR0008799(), # Regeling ademanalyse
                         BWBR0018724(), # Regeling bloed- en urineonderzoek
                         BWBR0025798(), # Regeling voertuigen
                         BWBR0008803(), # Regeling voorlopig ademonderzoek
                         BWBR0008074(), # Reglement rijbewijzen
                         BWBR0004825(), # Reglement verkeersregels en verkeerstekens 1990 (R
                         BWBR0006951(), # Kentekenreglement
                         BWBR0006622(), # Wegenverkeerswet 1994
                         BWBR0004581(), # Wet administratiefrechtelijke handhaving verkeersv
                         BWBR0002415(), # Wet aansprakelijkheidsverzekering motorrijtuigen
                         BWBR0025776(), # Aanwijzing inbeslagneming bij verkeersdelicten
                         BWBR0007127()] # Uitvoeringsbesluit ex artikel 4 Wegenverkeerswet 1994 inzake verkeersvoorschriften voor het militaire verkeer
    d["006. Politie"] = [BWBR0022463(), # Wet politiegegevens
                          BWBR0006589(), # Ambtsinstructie voor de politie, de Koninklijke ma
                          BWBR0006299()] # Politiewet 1993
    d["008. Jeugdstrafrecht"] = [BWBR0011756(), # Beginselenwet justitiele jeugdinrichtingen
                                 BWBR0012647(), # Reglement justitiele jeugdinrichtingen
                                 BWBR0023386(), # Besluit gedragsbeinvloeding jeugdigen
                                 BWBR0016637(), # Wet op de jeugdzorg
                                 BWBR0017751(), # Uitvoeringsbesluit Wet op de jeugdzorg
                                 BWBR0021142(), # Aanwijzing 12-minners incl. stopreactie
                                 BWBR0025771(), # Aanwijzing effectieve afdoening strafzaken jeugdigen
                                 BWBR0026005()] # Richtlijn voor strafvordering jeugd
    d["007. Overige"] = [BWBR0005537(), # Algemene wet bestuursrecht
                         BWBR0002448(), # Algemene termijnenwet
                         BWBR0002461(), # Besluit ex artikel 7, tweede lid, Algemene termijn
                         BWBR0011468(), # Wet bescherming persoonsgegevens
                         BWBR0016544(), # Besluit justitiele gegevens
                         BWBR0005700(), # Wet bijzondere opnemingen in psychiatrische zieken
                         BWBR0006297(), # Wet op de identificatieplicht
                         BWBR0011823(), # Vreemdelingenwet
                         BWBR0011825(), # Vreemdelingenbesluit
                         BWBR0012289(), # Vreemdelingencirculaire 2000 (B) 
                         BWBR0012002(), # Voorschrift vreemdelingen 2000
                         BWBR0002406(), # Wet tarieven in strafzaken
                         BWBR0012410(), # Wet toetsing levensbeeindiging op verzoek en hulp
                         BWBR0013177(), # Wijzigingswet Wet melding ongebruikelijke transacties
                         BWBR0001830()] # Wet op de rechterlijke organisatie
    d["009. Beleidsregels OM"] = [BWBR0021114(), # Aanwijzing aangiften van in het buitenland gepleeg
                                  BWBR0026744(), # Aanwijzing administratiefrechtelijke handhaving ve
                                  BWBR0021116(), # Aanwijzing afdoening van aangiften op basis van de
                                  BWBR0023567(), # Aanwijzing afloopberichten aan de verantwoordelijk
                                  BWBR0022926(), # Beleidsregel aanwijzing telecommunicatiewet
                                  BWBR0011161(), # Beleidsregels aanwijzing beschermde monumenten op
                                  BWBR0026461(), # Aanwijzing bemonstering en analyse milieudelicten
                                  BWBR0021256(), # Aanwijzing bestrijding van voetbalvandalisme en ge
                                  BWBR0026745(), # Aanwijzing bestuurlijke strafbeschikking overlastf
                                  BWBR0021149(), # Aanwijzing bestuurlijke transactie milieudelicten
                                  BWBR0024647(), # Aanwijzing beveiliging van personen, objecten en d
                                  BWBR0024007(), # Aanwijzing bijstand van tolken en vertalers in het
                                  BWBR0022927(), # Aanwijzing discriminatie
                                  BWBR0025208(), # Aanwijzing (doen) besturen tijdens ontzegging e.d.
                                  BWBR0021163(), # Aanwijzing elektronisch toezicht
                                  BWBR0021602(), # Aanwijzing executie, (vervangende) vrijheidsstraff
                                  BWBR0024039(), # Aanwijzing executie (vervangende) vrijheidsstraffe
                                  BWBR0024031(), # Aanwijzing formulier risicoprofiel en executie-ind
                                  BWBR0026284(), # Aanwijzing gebruik sepotgronden
                                  BWBR0026847(), # Aanwijzing Halt-Afdoening
                                  BWBR0021176(), # Aanwijzing handelwijze geweldsaanwending (politie)
                                  BWBR0021173(), # Aanwijzing handhaving Arbeidsomstandighedenwet
                                  BWBR0021148(), # Aanwijzing handhaving milieurecht
                                  BWBR0021587(), # Aanwijzing handhaving vuurwerkregelgeving                       
                                  BWBR0021172(), # Aanwijzing handhaving Winkeltijdenwet
                                  BWBR0024648(), # Aanwijzing hoge transacties en bijzondere transact
                                  BWBR0025087(), # Aanwijzing huiselijk
                                  BWBR0026850(), # Aanwijzing informatieverstrekking verkeersongevall
                                  BWBR0021180(), # Aanwijzing intellectuele-eigendomsfraude
                                  BWBR0023574(), # Aanwijzing internationale gemeenschappelijke onder
                                  BWBR0025898(), # Aanwijzing inverzekeringstelling
                                  BWBR0023380(), # Aanwijzing invordering bewijzen van bevoegdheid in
                                  BWBR0024759(), # Aanwijzing inzake de informatie-uitwisseling in he
                                  BWBR0024092(), # Aanwijzing inzake de invordering rijbewijzen
                                  BWBR0023576(), # Richtlijn inzake toepassing artikel 552i WvSv door
                                  BWBR0023377(), # Aanwijzing kader voor strafvordering
                                  BWBR0022422(), # Aanwijzing kinderpornografie (artikel 240b WvSr)
                                  BWBR0022058(), # Richtlijn kinderpornografie
                                  BWBR0026861(), # Aanwijzing lichten van gedetineerden, TBS-gestelde
                                  BWBR0025772(), # Aanwijzing maximumconstructiesnelheid brom- en sno
                                  BWBR0025105(), # Aanwijzing mensenhandel
                                  BWBR0021289(), # Aanwijzing onderzoek rijden onder invloed
                                  BWBR0022100(), # Aanwijzing onmiddellijke invrijheidsstelling
                                  BWBR0025359(), # Aanwijzing Ontneming
                                  BWBR0021625(), # Aanwijzing Opiumwet
                                  BWBR0021241(), # Aanwijzing opmaken proces-verbaal tegen onbekende
                                  BWBR0023203(), # Aanwijzing opsporing en behandeling van militaire
                                  BWBR0022168(), # Aanwijzing opsporing en vervolging ambtelijke corr
                                  BWBR0025375(), # Aanwijzing opsporing en vervolging faillissementsf
                                  BWBR0026007(), # Aanwijzing opsporing en vervolging inzake kindermi
                                  BWBR0021581(), # Aanwijzing opsporingsbevoegdheden
                                  BWBR0021175(), # Aanwijzing orgaandonatie bij niet-natuurlijke dood
                                  BWBR0021471(), # Aanwijzing paspoortsignalering
                                  BWBR0025787(), # Aanwijzing plaatsing in een psychiatrisch ziekenhu                                  
                                  BWBR0026000(), # Aanwijzing politietransactie inzake eenvoudige die
                                  BWBR0024535(), # Aanwijzing prioritering DNA-onderzoeken
                                  BWBR0021185(), # Aanwijzing rechtshulpverzoeken voor grensoverschri
                                  BWBR0024293(), # Aanwijzing Schade Niet-Voegen
                                  BWBR0021178(), # Aanwijzing slachtofferzorg
                                  BWBR0025778(), # Aanwijzing snelheidsoverschrijdingen en snelheidsb
                                  BWBR0024967(), # Aanwijzing Sociale Zekerheidsfraude
                                  BWBR0021138(), # Aanwijzing spreekrecht en schriftelijke slachtoffe
                                  BWBR0021583(), # Aanwijzing strafrechtelijk onderzoek bij zware ong
                                  BWBR0022337(), # Aanwijzing strafrechtelijke aanpak schoolverzuim
                                  BWBR0025104(), # Aanwijzing taakstraffen 2009
                                  BWBR0021226(), # Aanwijzing taken en inzet rijksrecherche                                  
                                  BWBR0021513(), # Aanwijzing TBS bij vreemdelingen
                                  BWBR0021482(), # Aanwijzing TBS met voorwaarden
                                  BWBR0021474(), # Aanwijzing toepassing opsporingsbevoegdheden en dw
                                  BWBR0021203(), # Aanwijzing toezeggingen aan getuigen in strafzaken
                                  BWBR0021520(), # Aanwijzing tweede beoordeling ('second opinion')
                                  BWBR0026854(), # Aanwijzing uitbreiding identificatieplicht
                                  BWBR0021156(), # Aanwijzing varen onder invloed
                                  BWBR0026862(), # Aanwijzing verkeersongevallen
                                  BWBR0023571(), # Aanwijzing verlaten plaats ongeval (art. 7 WVW 199
                                  BWBR0021593(), # Aanwijzing verplichtingen in het kader van Wbp en
                                  BWBR0022023(), # Aanwijzing vervolgingsbeslissing inzake levensbeei
                                  BWBR0021955(), # Aanwijzing vervolgingsbeslissing levensbeeindiging
                                  BWBR0026865(), # Aanwijzing vliegen onder invloed
                                  BWBR0025779(), # Aanwijzing Voertuigafmetingen, Aanwijzing Voertuig
                                  BWBR0021499(), # Aanwijzing voor de opsporing en vervolging van ove
                                  BWBR0021537(), # Richtlijn voor strafvordering Arbeidsomstandighede
                                  BWBR0021508(), # Richtlijn voor strafvordering arbeidstijdenwet
                                  BWBR0025777(), # Richtlijn voor strafvordering belading van voertui
                                  BWBR0026747(), # Richtlijn voor strafvordering bestuurlijke strafbe
                                  BWBR0026103(), # Richtlijn voor strafvordering bij meerderjarige ve
                                  BWBR0021523(), # Richtlijn voor strafvordering Drank- en horecawet
                                  BWBR0021394(), # Richtlijn voor strafvordering grondstromen
                                  BWBR0021450(), # Richtlijn voor strafvordering intellectuele-eigend
                                  BWBR0025755(), # Richtlijn voor strafvordering maximumconstructiesn
                                  BWBR0022043(), # Richtlijn voor Strafvordering Regelgeving Minister                                  
                                  BWBR0021425(), # Richtlijn voor strafvordering sociale zekerheidsfr
                                  BWBR0021238(), # Richtlijn voor strafvordering strafrechtelijke aan
                                  BWBR0026034(), # Richtlijn voor strafvordering tarieflijst waterzak
                                  BWBR0023700(), # Richtlijn voor strafvordering verkeersongevallen
                                  BWBR0026010(), # Richtlijn voor strafvordering wet vervoer gevaarli
                                  BWBR0025775(), # Richtlijn voor strafvordering Wet wegvervoer goede
                                  BWBR0022656(), # Aanwijzing voorlichting opsporing en vervolging
                                  BWBR0008150(), # Voorschrift inzake de samenwerking van de Belastin
                                  BWBR0024026(), # Aanwijzing Voorwaardelijke Invrijheidstelling
                                  BWBR0024276(), # Aanwijzing Wet Politiegegevens
                                  BWBR0025780(), # Aanwijzing Wet wegvervoer goederen
                                  BWBR0023568()] # Aanwijzing witwassen      
    d["010. Verdragen"] = [BWBV0002508(), # Verdrag inzake de rechten van het kind, New York,
                           BWBV0001000()] # Verdrag tot bescherming van de rechten van de mens
    return d
    
if __name__=="__main__":
    print structure().keys()
    
    
    
    
    
    
    
    
    
    
    
    
    