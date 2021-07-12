cijena = int(input("Cijena:"))
sat = int(input("Sati:"))
min = int(input("Minute:"))


zbroj = (cijena-(sat+min))
if zbroj < 0:
    zbroj = 0

print("Cijena s popustom je", zbroj, "kuna.")
