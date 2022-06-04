#Alexander_Máni_Einarsson
#06/11/19
#Timaprof 3

import random

on = True
while on:
    print()
    print("=-=-=-> Tímapróf 3 <-=-=-=")
    print()
    print("1. Oddatölur")
    print("2. Randomtölur")
    print("3. Texti")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        tala = 100
        for x in range(300):
            tala = tala + 1
            if tala % 2 != 0:
                print(tala," : ",end="")

    elif val == 2:
        listi_1 = []
        listi_2 = []
        listi_3 = []
        tveir_fimm_einn = 0
        for x in range(100):
            tala = random.randint(200, 300)
            listi_1.append(tala)
            if tala == 251:
                tveir_fimm_einn = tveir_fimm_einn +1
            if tala > 250:
                listi_2.append(tala)
            if tala % 5 == 0:
                listi_3.append(tala)
        summa = sum(listi_1)
        print()
        print("Hér er summa lista 1 með tveimur aukastöfum",format(summa, ".2f"))
        print()
        print("Talan 251 kemur fyrir",tveir_fimm_einn,"sinni/sinnum")
        print()
        print("Allar tölur yfir 250 eru í lista tvö, þær eru:",listi_2)
        print()
        print("Tölunar sem ganga í 5 eru: ")
        teljari = 0
        for x in range(len(listi_3)):
            tala = listi_3[teljari]
            teljari = teljari +1
            if teljari > 1:
                print(", ",end="")
            print(tala, end="")

    elif val == 3:
        texti = input("Sláðu inn texta")
        texti_2 = texti
        teljari = 0
        ord = 1
        n = 0
        bil = 0
        for x in range(len(texti)):
            stafur = texti[teljari]
            if stafur == " ":
                ord = ord + 1
            if stafur == "n" or stafur == "N":
                n = n + 1
            elif stafur == " ":
                bil = bil + 1
            else:
                texti = texti.replace(stafur, "#")

            teljari = teljari + 1
        print()
        print("það eru ",ord,"orð í þessum texta")
        print()
        print("stafurinn N/n kemur",n,"sinnum fyrir")
        print()
        print(texti_2,"verður þá",texti)

        ""
    elif val == 4:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
