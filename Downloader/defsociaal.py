from wetten import *

def structure():
    d = {}
    d["001. Algemene wetgeving"] = [BWBR0007795(), # Algemene nabestaandenwet
                                    BWBR0002221(), # Algemene Ouderdomswet
                                    BWBR0005537(), # Algemene wet bestuursrecht
                                    BWBR0002170(), # Beroepswet
                                    BWBR0004090(), # Besluit aanwijzing gevallen waarin arbeidsverhoudi
                                    BWBR0005199(), # Besluit gelijkstelling loondagen Werkloosheidswet,
                                    BWBR0020483(), # Besluit ontheffing verplichtingen WW en Wet WIA, B
                                    BWBR0011708(), # Boetebesluit socialezekerheidswetten
                                    BWBR0017747(), # Invoeringswet Wet financiering sociale verzekering
                                    BWBR0013061(), # Invoeringswet Wet structuur uitvoeringsorganisatie
                                    BWBR0017084(), # Maatregelenbesluit UWV
                                    BWBR0004043(), # Toeslagenwet
                                    BWBR0017745(), # Wet financiering sociale verzekeringen
                                    BWBR0002255(), # Wet gedeeltelijke compensatie voor ingevolge Algem
                                    BWBR0013060(), # Wet structuur uitvoeringsorganisatie werk en inkom
                                    BWBR0004157()] # Wet verhoging daglonen WAO, WWV en WW
    d["002. Arbeidsmarkt"] = [BWBR0024591(), # Beleidsregels boeteoplegging Wet arbeid vreemdelin
                              BWBR0007523(), # Besluit uitvoering Wet arbeid vreemdelingen
                              BWBR0007514(), # Delegatie- en uitvoeringsbesluit Wet arbeid vreemd
                              BWBR0009616(), # Wet allocatie arbeidskrachten door intermediairs
                              BWBR0007149(), # Wet arbeid vreemdelingen
                              BWBR0017614(), # Wet bestuurlijke boete arbeid vreemdelingen
                              BWBR0018268()] # Wijziging beleidsregels CWI inzake uitvoering Wet
    d["003. Arbeidsomstandigheden"] = [BWBR0014681(), # Aanpassingswet Tabakswet aan EU-richtlijn betreffe
                                       BWBR0021173(), # Aanwijzing handhaving Arbeidsomstandighedenwet
                                       BWBR0021139(), # Aanwijzing handhaving Arbeidstijdenwet
                                       BWBR0008587(), # Arbeidsomstandighedenregeling
                                       BWBR0010346(), # Arbeidsomstandighedenwet 1998, Arbeidsomstandighed
                                       BWBR0007671(), # Arbeidstijdenwet
                                       BWBR0026469(), # Beleidsregel boeteoplegging Arbeidstijdenwet en Ar
                                       BWBR0021624(), # Beleidsregels inzake ontheffing verbod van kindera
                                       BWBR0017461(), # Beleidsregels kwaliteit kinderopvang
                                       BWBR0023770(), # Besluit uitvoering rookvrije werkplek, horeca en a
                                       BWBR0017686(), # Intrekkingsregeling Regeling kinderopvang en buite
                                       BWBR0013009(), # Invoeringswet arbeid en zorg
                                       BWBR0011369(), # Praktische consequenties Wet aanpassing arbeidsduu
                                       BWBR0005528(), # Regeling toezicht naleving Tabakswet
                                       BWBR0017252(), # Regeling Wet kinderopvang
                                       BWBR0021537(), # Richtlijn voor strafvordering Arbeidsomstandighede
                                       BWBR0021508(), # Richtlijn voor strafvordering arbeidstijdenwet
                                       BWBR0004302(), # Tabakswet
                                       BWBR0011173(), # Wet aanpassing arbeidsduur
                                       BWBR0013008(), # Wet arbeid en zorg
                                       BWBR0016941(), # Wet bestuurlijke boete Arbeidstijdenwet
                                       BWBR0017017(), # Wet kinderopvang
                                       BWBR0023926(), # Wet zwangerschaps- en bevallingsuitkering zelfstan
                                       BWBR0010792(), # Wijziging Arbeidsomstandighedenregeling
                                       BWBR0026135(), # Wijzigingsregeling Subsidieregeling kinderopvang (
                                       BWBR0020772(), # Wijzigingswet Arbeidsomstandighedenwet 1998, enz.
                                       BWBR0020644(), # Wijzigingswet Arbeidstijdenwet (vereenvoudiging we
                                       BWBR0011404(), # Wijzigingswet Mediawet en Tabakswet (implementatie
                                       BWBR0018262()] # Wijzigingswet Wet arbeid en zorg, enz. (recht op l
    d["004. Arbeidsongeschiktheidsrecht"] = [BWBR0017240(), # Besluit uitvoering sociale werkvoorziening en bege
                                             BWBR0022309(), # Regeling procesgang eerste en tweede ziektejaar vo
                                             BWBR0019152(), # Reintegratiebesluit
                                             BWBR0011478(), # Schattingsbesluit arbeidsongeschiktheidswetten
                                             BWBR0026062(), # Tijdelijke wet compensatieregeling loonkosten bij
                                             BWBR0008656(), # Wet arbeidsongeschiktheidsverzekering zelfstandige
                                             BWBR0002524(), # Wet op de arbeidsongeschiktheidsverzekering
                                             BWBR0002551(), # Wet overgangsregeling arbeidsongeschiktheidsverzek
                                             BWBR0002552(), # Wet overgangsregeling Ziektewet
                                             BWBR0008903(), # Wet sociale werkvoorziening
                                             BWBR0006355(), # Wet terugdringing ziekteverzuim
                                             BWBR0023310(), # Wet verhoging uitkeringshoogte arbeidsongeschikthe
                                             BWBR0019057(), # Wet werk en inkomen naar arbeidsvermogen
                                             BWBR0016942(), # Wijzigingswet Wet sociale werkvoorziening en Wet s
                                             BWBR0001888()] # Ziektewet
    d["005. Burgerlijk wetboek boek 2"] = [BWBR0003045()] # Burgerlijk Wetboek Boek 2
    d["006. Burgerlijk wetboek boek 7"] = [BWBR0005290()] # Burgerlijk Wetboek Boek 7                                      
    d["007. CAO"] = [BWBR0001937(), # Wet op de collectieve arbeidsovereenkomst
                     BWBR0002698(), # Wet op de loonvorming
                     BWBR0001987()] # Wet op het algemeen verbindend en het onverbindend
    d["008. Faillissementswet"] = [BWBR0001860()] # Faillissementswet
    d["009. Gelijke behandeling"] = [BWBR0006502(), # Algemene wet gelijke behandeling
                                     BWBR0011468(), # Wet bescherming persoonsgegevens
                                     BWBR0014915(), # Wet gelijke behandeling op grond van handicap of c
                                     BWBR0016185(), # Wet gelijke behandeling op grond van leeftijd bij
                                     BWBR0003299(), # Wet gelijke behandeling van mannen en vrouwen
                                     BWBR0008819()] # Wet op de medische keuringen                    
    d["010. Medezeggenschapsrecht"] = [BWBR0003773(), # Besluit verstrekking financiele informatie aan ond
                                       BWBR0002058(), # Wet op de bedrijfsorganisatie
                                       BWBR0008508(), # Wet op de Europese ondernemingsraden
                                       BWBR0002747(), # Wet op de ondernemingsraden
                                       BWBR0018115(), # Wet rol werknemers bij de Europese vennootschap, W
                                       BWBR0010389(), # Wijzigingswet Wet op de bedrijfsorganisatie en eni
                                       BWBR0009392()] # Wijzigingswet Wet op de ondernemingsraden en titel
    d["011. Minimumloon"] = [BWBR0021782(), # Beleidsregels bestuurlijke handhaving Wet minimuml
                             BWBR0008222(), # Besluit aanwijzing aantal arbeidsverhoudingen die
                             BWBR0003599(), # Besluit minimumjeugdloonregeling
                             BWBR0002638()] # Wet minimumloon en minimumvakantiebijslag
    d["012. Ontslagrecht"] = [BWBR0002014(), # Buitengewoon Besluit Arbeidsverhoudingen 1945
                              BWBR0010062(), # Ontslagbesluit
                              BWBR0003026()] # Wet melding collectief ontslag
    d["013. Verdragen"] = [BWBV0001800(), # Europees Sociaal Handvest (herzien), Straatsburg,
                           BWBV0001017(), # Internationaal Verdrag inzake burgerrechten en po
                           BWBV0001016(), # Internationaal Verdrag inzake economische, sociale
                           BWBV0001000()] # Verdrag tot bescherming van de rechten van de mens
    d["014. Werkloosheidsrecht"] = [BWBR0020335(), # Beleidsregels toepassing artikelen 24 en 27 WW 200
                                    BWBR0026096(), # Besluit nadere regeling eindiging recht op uitkeri                  
                                    BWBR0026326(), # Besluit sollicitatieplicht werknemers WW 2009
                                    BWBR0026038(), # Inkomstenbesluit Werkloosheidswet
                                    BWBR0010338(), # Richtlijn passende arbeid 1999
                                    BWBR0017139(), # Scholingsregeling WW
                                    BWBR0004045(), # Werkloosheidswet
                                    BWBR0004044(), # Wet inkomensvoorziening oudere en gedeeltelijk arb
                                    BWBR0020031(), # Wet maatschappelijke ondersteuning
                                    BWBR0015703(), # Wet werk en bijstand
                                    BWBR0005735(), # Wijzigingswet Werkloosheidswet, enz. (vrijwillige
                                    BWBR0007156()]# Wijzigingswet Werkloosheidswet, enz. (aanscherping
    d["015. Wetboek van burgelijke rechtsvordering"] = [BWBR0001827()] # Wetboek van Burgerlijke Rechtsvordering
    return d
    
if __name__=="__main__":
    print structure()
    
    
    
    
    
    
    
    