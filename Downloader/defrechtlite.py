from wetten import *

def structure():
    d = {}
    #d["test"] = [BWBR0018053()] # Wet aanpassing fiscale behandeling VUT/prepensioen]
    d["001. Grondwet"] = [BWBR0001840()] # Grondwet
    d["002. Wetten"] = [BWBR0001886(), # Auteurswet 1912, Aut 
                        BWBR0005290() ,# Burgerlijk Wetboek Boek 7
                        BWBR0001854() ]# Wetboek van Strafrecht
    return d
    
if __name__=="__main__":
    print structure()