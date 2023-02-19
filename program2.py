#v.1.0 dzialajacej aplikacji
wiek = input("Podaj wiek uzytkownika: ")

plec = str(input("podaj swoja plec: "))

#sprawdzenie czy wiek jest liczba calkowita
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. zamykam apke")
wiek=int(wiek)

if wiek > 30 and plec == "kobieta" or "K" or "F" or "k" or "f":
    print(" +30 to aperol spritz pierwszy gratis!")
    print("mozesz kupowac alkohol")

elif wiek>=18 and wiek<=40:
    print("witamy w apce. mozesz kupowac u nas alko")
elif wiek>40:
    print("witamy w apce. mozesz kupowac u nas alkohol")
    print("korzystaj z produktow z umiarem")
else:
    exit("jestes za mlody wroc za jakis czas")