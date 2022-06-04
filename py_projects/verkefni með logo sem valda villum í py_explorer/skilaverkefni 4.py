#Alexander_Máni_Einarsson
#19/11/19
#Lokaverkefni

import random

on = True
while on:
    print()
    print("=-=-=-> Lokaverkefni <-=-=-=")
    print()
    print("1. Fótboltalið ")
    print("2. Þversumma ")
    print("3. Skæri, blað, steinn")
    print("4. Texti")
    print("5. Heiltölur")
    print("6. Teningapilið: Craps")
    print("7. Hangman")
    print("8. Hætta ")
    val = int(input("Veldu töluna hjá liðnum sem þú villt opna : "))
    if val == 1:
        print()
        print("Vinsamlegast sláðu inn: ")
        heild = int(input("Fjöldi þátttakend: "))
        heild_lid = int(input("Fjöldi í hverju liði: "))
        if heild_lid > heild:
            print("Ekki næst í lið með þennan fjölda þátttakend")
        elif heild_lid <= heild:
           lid = heild // heild_lid
           varamenn = heild % heild_lid
           print("Liðafjöldi: ", lid)
           print("Varmenn: ", varamenn)

        else:
            print("Villa hefur komið upp")

    elif val == 2:
        tala = 1
        tala_2 = 0
        while tala != 0:
            tala = int(input("sláðu inn heiltölu: "))
            summa = 0
            if tala >0:
                for x in range(1,tala+1):
                    summa = tala + summa
                    if x == tala:
                        print(x, end =" = ")
                    else:
                        print(x, end = " + ")
                print(summa)
            elif tala <0:
                for x in range(tala, 0):
                    summa = summa + tala
                    if x == -1:
                        print("(",x,")", end = " = ")
                    else:
                        print("(",x,")", end ="+")
                print(summa)

    elif val == 3:
        print()
        nafn = input("Hvað heitir þú fullu nafni?: ")
        aldur = input("Hve gamall ertu þú?: ")
        tol_sigur = 0
        tol_tap = 0
        not_sigur = 0
        not_tap = 0
        jafntefli = 0
        leikur = 0
        not_svar = 0
        while not_svar != 4:
            print()
            print("=-=-=-> Skæri, blað, steinn <-=-=-=")
            print()
            print("1. Skæri")
            print("2. Blað")
            print("3. Steinn")
            print("4. Hætta")
            not_svar = int(input("Veldu þann lið sem þér líkar með tölustaf: "))
            for x in range(1, 6):
                tol_svar = random.randint(1, 3)

            if not_svar == 1:
                not_val = "Skæri"
            elif not_svar == 2:
                not_val = "Blað"
            elif not_svar == 3:
                not_val = "Stein"
            else:
                print("Villa hefur komið upp")
            if tol_svar == 1:
                tol_val = "Skæri"
            elif tol_svar == 2:
                tol_val = "Blað"
            elif tol_svar == 3:
                tol_val = "Stein"
            else:
                print("Villa hefur komið upp")

            if (not_svar == 1 and tol_svar == 2) or (not_svar == 2 and tol_svar == 3) or (not_svar == 3 and tol_svar == 1):
               print()
               print("Tölvan valdi",tol_val)
               print("Þú valdir",not_val)
               print("Sem þýðir að...")
               print()
               print("Þú vannst!")
               not_sigur = not_sigur +1
               tol_tap = tol_tap +1
               leikur = leikur + 1
            elif (not_svar == 2 and tol_svar == 1) or (not_svar == 3 and tol_svar == 2) or (not_svar == 1 and tol_svar == 3):
                print()
                print("Tölvan valdi", tol_val)
                print("Þú valdir", not_val)
                print("Sem þýðir að...")
                print()
                print("Tölvan hefur unnið")
                tol_sigur = tol_sigur +1
                leikur = leikur + 1
                not_tap = not_tap +1
            elif not_svar == tol_svar:
                print()
                print("Tölvan valdi", tol_val)
                print("Þú valdir", not_val)
                print("Sem þýðir að...")
                print()
                print("Það hefur komið upp jafntefli")
                jafntefli = jafntefli + 1
                leikur = leikur + 1
            elif not_svar == 4:
                print()
                print("<>==-<>-=-<>-=Stigatafla=-<>-=-<>-=-==<>")
                print()
                print("-Spilari: ", nafn,".",aldur,"ára gamall.-")
                print()
                print("-----Þú vannst í",not_sigur,"skipti-----")
                print("------Þú tapaðir í",not_tap,"skipti------")
                print("----Tölvan vann í", tol_sigur, "skipti---")
                print("----Tölvan tapað í", tol_tap, "skipti----")
                print("---Jafntelfi var í",jafntefli,"skipti----")
                print("--------í gegnum", leikur,"leiki---------")
                print()
                print("Takk fyrir að spila, skæri blað steinn.")
            else:
                print("villa hefur komið upp")
    elif val == 4:
        texti = input("Sláðu inn texta")
        texti_2 = texti
        teljari = 0
        for x in range(len(texti)):
            stafur = texti[teljari]
            if  stafur == "J"  or stafur == "j" or stafur == "b" or stafur == "l" or stafur == "n" or stafur == "_":
                ""
            else:
                if stafur == " ":
                   texti = texti.replace(stafur, "_")
                else:
                    texti = texti.replace(stafur, "*")
            teljari = teljari + 1
        print()
        print(texti_2, ",verður þá: ", texti)

    elif val == 5:
        print()
        print("Foritið biður um 12 heiltölur og raðar þeim síðan upp")
        talnalisti = []
        tala = 0
        for x in range(12):
            tala = int(input("Sláðu inn heiltölu: "))
            talnalisti.append(tala)
        print("Minnsta talan er: ",min(talnalisti))
        print("Stærsta talan er: ",max(talnalisti))
        print("Summa allra talnana er: ",sum(talnalisti))
        medaltal = sum(talnalisti) // 12
        print("Meðaltal talnana er: ",medaltal)

    elif val == 6:
        print()
        teningur_1 = random.randint(1, 6)
        teningur_2 = random.randint(1, 6)
        summa = teningur_1 + teningur_2
        kasta = input("Ýttu á hvað hnapp sem er til þess að kasta")
        print("Þú fékkst", summa)
        if summa == 7 or summa == 11:
            print()
            print("Til hamingu þú vannst!")
        elif summa == 2 or summa == 3 or summa ==12:
            print()
            print("Þú tapaðir, craps")
        else:
            summa_2 = 0
            svar = "j"
            while svar == "j":
                teningur_1 = random.randint(1, 6)
                teningur_2 = random.randint(1, 6)
                summa_2 = teningur_1 + teningur_2
                print()
                print("Kastaðu aftur ef þú færð", summa," Vinnur þú, en þú tapar ef þú færð 7: ")
                kasta = input("Ýttu á hvað hnapp sem er til þess að kasta")
                print("Þú fékkst", summa_2)
                if summa == summa_2:
                    print()
                    print("Til hamingu þú vannst!")
                    svar == "n"
                    break
                elif summa_2 == 7:
                    print()
                    print("Þú tapaðir")
                    svar == "n"
                    break


        ""
    elif val == 7:
        ord = 0
        rett = []
        rangt = []
        ord = random.randint(0, 4)
        ordalisti = ["amma", "traktor", "hilla", "banani", "epli"]
        ord = ordalisti[ord]
        svar = 1
        ord_2 = ord
        while svar != ord:
            ord_2 = ord
            ord = ord_2
            gisk = input("Giskaðu á staf: ")
            teljari = 0
            for x in range(len(ord)):

                stafur = ord[teljari]
                if stafur == gisk:
                    ""
                else:
                    ord = ord.replace(stafur, "_")
                teljari = teljari + 1
            print(ord)
            print()




        ""
    elif val == 8:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
