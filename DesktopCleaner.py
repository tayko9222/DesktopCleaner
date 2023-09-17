import os

try:
    import os; import shutil ; from colorama import *; import time; import pystyle; from pystyle import *; import platform; import subprocess; import colorama; from colorama import Fore, Style
except:
    os.system("pip install time random colorama string pystyle platform subprocess colorama")

# CLEAR

def clear():
    os.system("cls")


# ASCII

def ascii():
    print(Fore.LIGHTBLUE_EX, """

·▄▄▄▄  ▄▄▄ ..▄▄ · ▄ •▄ ▄▄▄▄▄       ▄▄▄·     ▄▄· ▄▄▌  ▄▄▄ . ▄▄▄·  ▐ ▄ ▄▄▄ .▄▄▄  
██▪ ██ ▀▄.▀·▐█ ▀. █▌▄▌▪•██  ▪     ▐█ ▄█    ▐█ ▌▪██•  ▀▄.▀·▐█ ▀█ •█▌▐█▀▄.▀·▀▄ █·
▐█· ▐█▌▐▀▀▪▄▄▀▀▀█▄▐▀▀▄· ▐█.▪ ▄█▀▄  ██▀·    ██ ▄▄██▪  ▐▀▀▪▄▄█▀▀█ ▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▄▄▌▐█▄▪▐█▐█.█▌ ▐█▌·▐█▌.▐▌▐█▪·•    ▐███▌▐█▌▐▌▐█▄▄▌▐█ ▪▐▌██▐█▌▐█▄▄▌▐█•█▌
▀▀▀▀▀•  ▀▀▀  ▀▀▀▀ ·▀  ▀ ▀▀▀  ▀█▄▀▪.▀       ·▀▀▀ .▀▀▀  ▀▀▀  ▀  ▀ ▀▀ █▪ ▀▀▀ .▀  ▀

    """)
    print("")

# 1

clear()
ascii()


# DOSSIER OU IL Y A LES FICHIERS A COPIER

print(Colors.light_gray, "[", end=""), print(Fore.LIGHTBLUE_EX, "#", end=""), print(Colors.light_gray, "]", end=""), print(Colors.light_gray, " Chemin vers le dossier ou il y a les fichiers à copier")
print("")
repertoire_source = r'' + input(" > ")

clear()
ascii()
print(Colors.light_gray, "[", end=""), print(Fore.LIGHTBLUE_EX, "#", end=""), print(Colors.light_gray, "]", end=""), print(Colors.light_gray, " Le chemin de dossier est " + repertoire_source)
time.sleep(2)


# 2

clear()
ascii()

# LE NOM DU DOSSIER QUI VAS ETRE CREER ET OU LES FICHIERS VONT ETRE COPIER
print(Colors.light_gray, "[", end=""), print(Fore.LIGHTBLUE_EX, "#", end=""), print(Colors.light_gray, "]", end=""), print(Colors.light_gray, " Nom de l'extension de dossier")
print("")
extension = input(" > ")

# PRINT LA RESPONSE
clear()
ascii()
print(Colors.light_gray, "[", end=""), print(Fore.LIGHTBLUE_EX, "#", end=""), print(Colors.light_gray, "]", end=""), print(Colors.light_gray, " Le dossier qui vas être créer est " + repertoire_source + '\\' + extension)
time.sleep(2)

# NOUVEAU DOSSIER A CREER
g = repertoire_source + '\ ' + extension


# CREATION DU DOSSIER
if not os.path.exists(g):
    os.makedirs(g)
rm_g = g

extensions_a_deplacer = ['.' + extension]
clear()
ascii()
print(Colors.light_gray, "[", end=""), print(Fore.LIGHTBLUE_EX, "#", end=""), print(Colors.light_gray, "]", end=""), print(Colors.light_gray, " Rangement du bureau en cours (" + extensions_a_deplacer + ")")
time.sleep(3)

for nom_fichier in os.listdir(repertoire_source):

    if any(nom_fichier.endswith(extension) for extension in extensions_a_deplacer):

        chemin_source = os.path.join(repertoire_source, nom_fichier)

        chemin_destination = os.path.join(rm_g, nom_fichier)

        shutil.move(chemin_source, chemin_destination)
        print(f'Fichier déplacé : {nom_fichier}')
