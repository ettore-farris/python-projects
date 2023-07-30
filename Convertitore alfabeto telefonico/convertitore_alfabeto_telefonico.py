import pandas as pd

alfabeto_telefonico = {
    "lettere": [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "nomi": ["Spazio", "Ancona", "Bari", "Como", "Domodossola", "Empoli", "Firenze", "Genova", "Hotel", "Imola", "I lunga", "Cappa", "Livorno", "Milano", "Napoli", "Otranto", "Palermo", "Quadro", "Roma", "Savona", "Torino", "Udine", "Venezia", "Vu doppia", "Ics", "Ipsilon", "Zeta"]
}

df = pd.DataFrame(alfabeto_telefonico)
result = []

while True:
    name = input("Scrivi il tuo nome: ").lower()
    nospacename = name.replace(' ', '')
    if nospacename.isalpha() == False:
        print("Digita solo lettere!")
    else:
        result = [row.nomi for l in name for (index,row) in df.iterrows if l == row.letters]
        print(result)
        break



