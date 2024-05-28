                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################
"""

Ce projet est un jeux qui permet de trouver un mot cache selectionne dans un dictionnaire. Il est dynamique en ce sens qu'il vous guide

a chaque fois pour vous rappocher du mot cache. Le score et le nombre de tentative du joueur 

lui sont donnes a la fin.

"""

def generate_mystery_word(dictionnaire):
    
    import random
    
    # index = random.randint(0, len(dictionnaire)-1)
    # mot = dictionnaire[index]
    # print(mot)
    
    mot = random.choice (dictionnaire)
    # print(mot)   
    mot = dictionnaire[3]
    mot_len = len(mot)
    essaie = 1
    score = 100
    mystere = ""

    
    for i in range(mot_len):
    
        if i%2 ==0:
        
            mystere += mot[i]
        
        else:
        
            mystere += "*"
    
    return mot, mystere

def check_it(mystere, mot, user_try):  #user_try=mot_utilisateur
    status = False
    msg = None
    essaie = 1
    score = 100
    
    if not len(user_try) == len(mot):
        
        msg = f"Desole vous devez entrer un mot contenant {len(mot)} caracteres"
        essaie +=1
        score -=10
        
    if user_try != mot:
        
        mystere_backup = mystere
        mystere = ""
                
        for i in range(len(mot)):
                    
            if user_try[i] == mot[i]:
                if i > 0:
                    if mot[i-1] == user_try[i-1]:
                        mystere += mot[i]
                    else:
                        mystere += mystere_backup[i]      
                else:
                    mystere += mystere_backup[i]
                            
            else:
                        
                mystere += mystere_backup[i]
        msg = f"Desolé!!!! vous avez manque le mot caché. Essayez a nouveau"
        essaie +=1
        score -=10
        return status, msg, mystere

    msg = f"Felicitation!!! Vous avez trouve le mot cache : {mot}"
    status = True
    essaie +=1
    score -=10
    return status, msg, mystere

    


mot, mystere =generate_mystery_word([
    "test",
    "vie",
    "aimer",
    "secret",
    "mysterieux",
    "cacher"
])

print(mystere)

mot_ = input(f"entrez les caracteres manquant afin de trouver le mot caché de {len(mot)} caracteres")
print(check_it(mystere, mot, mot_))