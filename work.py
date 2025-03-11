tatasks = []

while True:
    print("1- Lisa uus ülesanne")
    print("2- Eemalda ülesanne")
    print("3- Näita ülesannete nimekiri")
    print("4- Sorteeri ülesanded tähtede järgi")
    print("5- Lisa ülesanne konkreetsele positsioonile")
    print("6- Kuva ülesannete arv nimekirjas")
    print("7- Kustuta kõik ülesanded")
    print("8- Välju programmist")
    print("9- Kontrolli stringi omadusi (digit, alpha, alnum, jne.)")
    
    while True:
        try:
            valik = int(input("Vali tegevus (1-9): "))
            if 1 <= valik <= 9:
                break
            else:
                print("Palun vali number vahemikus 1-9.")
        except ValueError:
            print("Palun vali kehtiv number vahemikus 1-9.")
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
        if vastus in tasks:
            tasks.remove(vastus)
            print(f"Ülesanne '{vastus}' on eemaldatud nimekirjast.")
        else:
            print(f"Ülesannet '{vastus}' ei leitud nimekirjast.")
        print()

    elif valik == 3:
        if tasks:
            print(f"Sinu ülesannete nimekiri: {tasks}")
        else:
            print("Nimekiri on tühi.")
        print()

    elif valik == 4:
        tasks.sort()
        print(f"Ülesanded on sorteeritud: {tasks}")
        print()

    elif valik == 5:
        soov = input("Sisesta ülesanne: ")
        try:
            koht = int(input("Sisesta positsioon (1-põhineb 1-st): "))
            if 1 <= koht <= len(tasks) + 1:
                tasks.insert(koht - 1, soov)
                print(f"Ülesanne '{soov}' on lisatud positsioonile {koht}.")
            else:
                print(f"Kehtetu positsioon. Palun vali vahemikus 1-{len(tasks) + 1}.")
        except ValueError:
            print("Positsioon peab olema arv.")
        print()

    elif valik == 6:
        print(f"Nimekirjas on {len(tasks)} ülesannet.")
        print()

    elif valik == 7:
        tasks.clear()
        print("Kõik ülesanded on nimekirjast eemaldatud.")
        print()

    elif valik == 8:
        print("Head aega ja edu ülesannete täitmisel!")
        break

    elif valik == 9:
        string = input("Sisesta string, mida kontrollida: ").strip()
        if string.isdigit():
            print(f"String '{string}' koosneb ainult numbritest.")
        elif string.isalpha():
            print(f"String '{string}' koosneb ainult tähtedest.")
        elif string.isalnum():
            print(f"String '{string}' koosneb ainult tähtedest ja numbritest.")
        elif string.islower():
            print(f"String '{string}' koosneb ainult väikestest tähtedest.")
        elif string.isupper():
            print(f"String '{string}' koosneb ainult suurtest tähtedest.")
        elif string.isspace():
            print(f"String '{string}' koosneb ainult valgetest karakteritest (nt tühikutest).")
        elif string.istitle():
            print(f"String '{string}' koosneb sõnadest, mis algavad suure tähega.")
        elif string.isdecimal():
            print(f"String '{string}' koosneb ainult kümnenditest numbritest.")
        elif string.isnumeric():
            print(f"String '{string}' koosneb ainult numbrilistest väärtustest (nt rooma numbrid).")
        elif string.isidentifier():
            print(f"String '{string}' on kehtiv identifikaator (nt muutujanimi).")
        elif string.isprintable():
            print(f"String '{string}' sisaldab ainult kuvatavaid märke.")
        else:
            print(f"String '{string}' sisaldab erinevaid karakterite tüüpe.")
        print()
# # 1 
# print("reavahe")
# print("ül rea eraldamine tühikuga ")
# s = "Python is awesome"
# split_str = s.split()  
# #´2
# print("asendada kõik tühikud")
# replaced_str = s.replace(" ", "-")  
# # 3
# print("reavahe")
# s2 = "apple,banana,cherry"
# split_comma = s2.split(",")  
# print(split_str) 
# print(replaced_str) 
# print(split_comma) 

# s = "Python"
# slice_str = s[1:5]  # "ytho"

# padded_str = s.zfill(10)  # "00000Python"


# print(slice_str)  
# print(centered_str) 
# print(padded_str)  

# my_list = [5, 2, 9, 1, 7, 3]

# print("minimaalse ja maksimaalse elemendi leidmine")
# min_value = min(my_list)
# max_value = max(my_list)

# print(f"max value:  {min_value}")
# print(f"min value:  {max_value}")
