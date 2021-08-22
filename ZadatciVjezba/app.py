import array

oznake = []
broj = int(input('Unesite broj koji je lansiran u svemir:'))
asteroid = int(input('Unesite broj asteroida koji su pogodili broj:'))
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
b2 = 0
c2 = 0
d2 = 0

if 999 < broj < 10000 and 1 < asteroid < 11:
    for i in range(asteroid):
        oznake.append(int(input('Unesite oznaku koja je udarila broj:')))

        for oznaka in oznake:

            if -5 < oznaka < 5:
                print("Sve oznake su validne.")

            else:
                print("Neka od oznaka nije validna.")

for oznaka in oznake:
    if oznaka == -1:
        counter1 = counter1 + 1

for oznaka in oznake:
    if oznaka == -2:
        counter2 = counter2 + 1

for oznaka in oznake:
    if oznaka == -3:
        counter3 = counter3 + 1

for oznaka in oznake:
    if oznaka == -3:
        counter3 = counter3 + 1

for oznaka in oznake:
    if oznaka == -4:
        counter4 = counter4 + 1


def jedinice(a):
    for x in range(counter1):
        b1 = a % 10
        c1 = b1 - counter1
        d1 = a - b1

    print(b1)
    print(c1)
    print(d1)


def desetice(a):
    for x in range(counter2):
        b2 = a % 100 // 10
        c2 = b2 - counter2
        d2 = a - b2 * 10
        d2 = d2 + c2 * 10

    print(b2)
    print(c2)
    print(d2)


jedinice(broj)
desetice(broj)
