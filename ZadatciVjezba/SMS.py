import array

mapa_znakova = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1,
    "e": 2,
    "f": 3,
    "g": 1,
    "h": 2,
    "i": 3,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 1,
    "n": 2,
    "o": 3,
    "p": 1,
    "q": 2,
    "r": 3,
    "s": 4,
    "t": 1,
    "u": 2,
    "v": 3,
    "w": 1,
    "x": 2,
    "y": 3,
    "z": 4
}

broj = int(input("Upišite broj znakova u poruci:"))
znakovi = []
if broj < 16:
    for x in range(broj):
        znakovi.append(input("Unesite znak u poruci:"))


else:
    print("Broj znakova je prevelik.")

ukupno = 0

for znak in znakovi:
   broj_tipkanja = mapa_znakova.get(znak)
   ukupno = broj_tipkanja + ukupno

print("Ukupan zbroj pritisaka tipki je:", ukupno)
