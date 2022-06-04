#Alexander_Máni_Einarsson
#13/01/20
#Upprifjun 3

import datetime

on = True
while on:
    print()
    print("=-=-=-> Upprifjun 3 <-=-=-=")
    print()
    print("1. Uppröðun talna")
    print("2. Aldur um næstu aldamót")
    print("3. Talnaruna")
    print("4. Kúla")
    print("5. Lykilorð")
    print("6. Hástafir og Lágstafir")
    print("7. Hæsti samnefnari")
    print("8. Hætta ")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        talnalisti = []
        print("Foritið spyr um 3 tölur og raðar þeim upp")
        tala_1 = int(input("Sláðu inn fyrstu töluna: "))
        talnalisti.append(tala_1)
        tala_2 = int(input("Sláðu inn aðra töluna: "))
        talnalisti.append(tala_2)
        tala_3 = int(input("Sláðu inn þriðju töluna: "))
        talnalisti.append(tala_3)
        talnalisti.sort()
        print(talnalisti[0],talnalisti[1],talnalisti[2])
        if tala_1 == tala_2 == tala_3:
            print("allar tölunar eru eins")

    elif val == 2:
        print()
        nuna = datetime.datetime.now()
        nafn = input("Hvað heitir þú?: ")
        print(nafn, end="")
        aldur = int(input(" ,hve gamall/gömul ert þú"))

        afgangur = nuna.year % 100
        ar_i_aldamot = 100 - afgangur
        aldur_um_aldamot = aldur + ar_i_aldamot
        print(nafn,", um næstu aldamót verður þú",aldur_um_aldamot,"ára!")

    elif val == 3:
        tala = 1
        teljari = 0
        talnalisti = []
        while tala != 0:
            tala = int(input("Sláðu inn tölu"))
            talnalisti.append(tala)
            teljari = teljari + 1
        print("Summa talnana er: ",sum(talnalisti))
        medaltal = sum(talnalisti) / teljari
        print("Meðaltal talnana er",medaltal)
        print("Það voru, ",teljari,"tölur slegnar inn")

    elif val == 4:
        print()
        radius = input("Sláðu inn radius kúlu: ")
        pi = 3.14159
        flatarmal = 4 * pi * (radius *radius)
        rummal = (4.0 * (radius * radius * radius) * pi)/3
        print("Yfirborðsflatarmál kúlunar er", flatarmal)
        print("Rúmmál kúlunar er", rummal)

    elif val == 5:
        print()
        svar = "ja"
        teljari = 0
        tala = 0
        bokstafur = 0
        while svar != "Nei" or svar != "nei":
            lykilord = input("Sláðu inn lykilorð")
            for x in range(6):
                stafur = lykilord[teljari]
                teljari = teljari + 1
                if stafur.isalpha():
                    bokstafur = bokstafur +1
                if stafur.isdigit():
                    tala = tala +1
            print("Það eru",tala,"Tölustafir")
            print("Það eru",bokstafur,"Bókstafir")
            if bokstafur > 1 and tala > 1 and len(lykilord) >= 6:
                print("Þetta lykilorð er í lagi")
            else:
                print("Þetta lykilorð er ekki löglegt, ath lengd, bókstafi og tölustafi")

            svar = input("Viltu prófa aftur(Já/Nei): ")
    elif val == 6:
        print()
        texti = input("Sláðu inn texta")
        teljari= 0
        bokstafur = 0
        hastafur = 0
        for x in range(len(texti)):
            stafur =texti[teljari]
            teljari = teljari +1
            if stafur.isalpha():
                bokstafur = bokstafur + 1
            if stafur.isupper():
                hastafur = hastafur + 1
        lagstafur = bokstafur - hastafur
        print("Það er/eru ",lagstafur,"lágstafir")
        print("Það er/eru ",hastafur, "hástafir")


    elif val == 7:
        tala_1 = int(input("Sláðu inn tölu"))
        tala_2 =int(input("Sláðu inn tölu"))
        samnefnari = 0
        for x in range(1,100):
            if tala_1 % x == 0 and tala_2 % x == 0:
                samnefnari = x
        print("Hæsti samnefnarinn er: ",samnefnari)
        ""
    elif val == 8:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
