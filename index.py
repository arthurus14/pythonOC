# coding: utf8
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
	quote = my_list[0]
	return quote

print(show_citation(quotes))
