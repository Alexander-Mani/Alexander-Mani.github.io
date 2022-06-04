#Alexander_Máni_Einarsson
#12/11/19
#timaverkefni_2

on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni <-=-=-=")
    print()
    print("1. Sentimetrum breytt í, m, dm og cm")
    print("2. Veldi ")
    print("3. Sláðu inn tölu á bilinu 1 - 9 ")
    print("4. Hætta ")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        svar = "j"
        while svar == "j" or svar == "J":
            cm = int(input("Sláðu inn lengd í sentimetrum: "))
            m = cm // 100
            afgangur = cm % 100
            dm = afgangur // 10
            afgangur = cm % 10
            cm = afgangur
            print(m, "metrar")
            print(dm, "desimetrar")
            print(cm, "sentimetrar")
            svar = input("Viltu halda áfram j/n?: ")

    elif val == 2:
        svar = "j"
        while svar == "j" or svar == "J":
            tala = int(input("Sláðu inn tölu: "))
            veldi = int(input("Sláðu inn veldisvísir fyrir töluna: "))
            utkoma = 1
            for x in range(veldi):
                utkoma = tala * utkoma
            print(utkoma)
            svar = input("Viltu halda áfram j/n?: ")


    elif val == 3:
        print()
        tala = 5
        while tala > 0 and tala < 10:
            tala = int(input("Sláðu inn heiltölu á bilinu 1 - 9: "))
            tala1 = tala
            tala = tala + 1
            for y in range(tala):
                tala = tala - 1
                if tala > 0:
                    print("*" * tala)
            for x in range(tala1):
                x = x + 1
                print("*" * x)
    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")