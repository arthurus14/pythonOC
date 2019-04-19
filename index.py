# coding: utf8
import random
print("Welcome on Python bro :)")

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]


reponse = input("A pour rester, B pour quitter le programme.")

if reponse == "A":
    print("Vous avez choisi de rester dans le programme")
else:
    print("Au revoir")

def show_citation(my_list):
  rand = random.randint(0, len(my_list) - 1)
  quote = my_list[rand]
  return quote

print(show_citation(quotes))

mess = "{perso} a dit : {message}".format(perso="Babar", message="On mange quoi ce soir ?")
print(mess)
