lkz = int(input("Unesite količinu lkz-a."))

if lkz < 51:
    print("Dobra kvaliteta zraka.")

if lkz > 50 and lkz < 101:
    print("Umjerena kvaliteta zraka.")

if lkz > 100 and lkz < 151:
    print("Zrak nezdrav za osjetljive grupe.")
    
if lkz > 150 and lkz < 201:
    print("Nezdrav zrak.")

if lkz > 200 and lkz < 301:
    print("Vrlo nezdrav zrak.")

if lkz > 300 and lkz < 501:
    print("Opasan zrak")
