print ("Witaj w naszym sklepie. Podaj potrzebne dane, aby moc korzystac ze sklepu.")

region = input("Podaj region (EUR/USA)")

region = str(region.upper())

if region == "EUR":
    wiek = input ("Podaj wiek uzytkownika: ")
    if wiek.isdigit() == False:
        exit("Wiek musi byc liczba calkowita. Zamykam aplikacje")

    wiek=int(wiek)

    if  wiek >= 18 and wiek <= 40:
        print ("Witamy w apce. Mozesz kupic u nas alkohol")
    elif wiek > 40 and wiek < 120:
        print ("Witamy w apce. Mozesz kupic u nas alkohol")
        print ("Prosze korzystaj z produktow z umiarem")
    else:
        exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
elif region == "USA":
    wiek = input ("Podaj wiek uzytkownika: ")
    if wiek.isdigit() == False:
        exit("Wiek musi byc liczba calkowita. Zamykam aplikacje")

    wiek=int(wiek)

    if  wiek >= 21 and wiek <= 40:
        print ("Witamy w apce. Mozesz kupic u nas alkohol")
    elif wiek >40 and wiek < 120:
        print ("Witamy w apce. Mozesz kupic u nas alkohol")
        print ("Prosze korzystaj z produktow z umiarem")
    else:
        exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
else: 
    exit ("Nie sprzedajemy w innych regionach")

# 
