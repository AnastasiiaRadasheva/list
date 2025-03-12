tasks = []
while True:
    print("1- Lisa uus ülesanne")
    print("2- Eemalda ülesanne")
    print("3- Sorteeri ülesanded tähtede järgi")
    print("4- Lisa ülesanne konkreetsele positsioonile")
    print("5- Kuva ülesannete arv nimekirjas")
    print("6- Kustuta kõik ülesanded")
    print("7- Kontrolli stringi omadusi (digit, alpha, alnum, jne.)")
    
    while True:
        try:
            valik = int(input("Vali tegevus (1-7): "))
            if valik < 1 or valik > 7:
                break
            else:
                print("Palun vali number vahemikus 1-7.")
        except ValueError:
            print("Palun vali kehtiv number vahemikus 1-7.")
            print()

    if valik == 1:
        while True:
            vastus = input("Sisesta ülesanne: ")
            tasks.append(vastus)
            print(f"Ülesanne '{vastus}' on lisatud nimekirja.")
            print()
            while True:
                soov = input("Kas tahad lisada veel ülesandeid? (jah/ei) ").strip().lower()
                if soov == "ei":
                    print()
                    break
                elif soov == "jah":
                    break
                else:
                    print("Palun vasta 'jah' või 'ei'.")
            if soov == "ei":
                break

    elif valik == 2:
        vastus = input("Sisesta ülesanne, mille tahad eemaldada: ")
        found = False
        for task in tasks:
            if task == vastus:
                tasks.remove(task)
                print(f"Ülesanne '{vastus}' on eemaldatud nimekirjast.")
                found = True
                break
        if not found:
            print(f"Ülesannet '{vastus}' ei leitud nimekirjast.")
        print()
    elif valik == 4:
        soov = input("Sisesta ülesanne: ")
        try:
            koht = int(input("Sisesta positsioon (1-põhineb 1-st): "))
            if 1 <= koht <= len(tasks) + 1:
                tasks.insert(koht - 1, soov)
                print(f"Ülesanne '{soov}' on lisatud positsioonile {koht}.")
            else:
                print(f"Kehtetu positsioon. Palun vali vahemikus {len(tasks) + 1}.")
        except ValueError:
            print("Positsioon peab olema arv.")
        print()

    elif valik == 5:
        print(f"Nimekirjas on {len(tasks)} ülesannet.")
        print()

    elif valik == 6:
        tasks.clear()
        print("Kõik ülesanded on nimekirjast eemaldatud.")
        print()
    elif valik == 7:
            print("Vali, mida kontrollida stringi omadustest:")
            print("1- Kas string on number?")
            print("2- Kas string sisaldab ainult tähti?")
            print("3- Kas string sisaldab ainult tähti ja numbreid?")
            print("4- Kas string on ainult väikestest tähtedest?")
            print("5- Kas string on ainult suurtest tähtedest?")
            while True:
                try:
                    kontrolli_valik = int(input("Vali tegevus (1-5): "))
                    if 1 <= kontrolli_valik <= 5:
                        break
                    else:
                        print("Palun vali number vahemikus 1-5.")
                except ValueError:
                    print("Palun vali kehtiv number vahemikus 1-5.")
        
            string = input("Sisesta string, mida kontrollida: ").strip()

            if kontrolli_valik == 1:
                if string.isdigit():
                    print(f"String '{string}' koosneb ainult numbritest.")
                else:
                    print(f"String '{string}' ei ole ainult numbritest.")
            elif kontrolli_valik == 2:
                if string.isalpha():
                    print(f"String '{string}' koosneb ainult tähtedest.")
                else:
                    print(f"String '{string}' ei ole ainult tähtedest.")
            elif kontrolli_valik == 3:
                if string.isalnum():
                    print(f"String '{string}' koosneb ainult tähtedest ja numbritest.")
                else:
                    print(f"String '{string}' ei ole ainult tähtedest ja numbritest.")
            elif kontrolli_valik == 4:
                if string.islower():
                    print(f"String '{string}' koosneb ainult väikestest tähtedest.")
                else:
                    print(f"String '{string}' ei ole ainult väikestest tähtedest.")
            elif kontrolli_valik == 5:
                if string.isupper():
                    print(f"String '{string}' koosneb ainult suurtest tähtedest.")
                else:
                    print(f"String '{string}' ei ole ainult suurtest tähtedest.")
