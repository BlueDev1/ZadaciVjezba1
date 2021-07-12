broj1 = int(input('Unesite prvi broj bodova:'))
broj2 = int(input("Unesite drugi broj bodova:"))
broj3 = int(input("Unesite treći broj bodova:"))
rezultat1 = False
rezultat2 = False
rezultat3 = False

if broj1 == 200:
    rezultat1 = True

if broj2 == 200:
    rezultat2 = True

if broj3 == 200:
    rezultat3 = True

if rezultat1 or rezultat2 or rezultat3 == True:
    print("DA")

else:
    print("NE")
