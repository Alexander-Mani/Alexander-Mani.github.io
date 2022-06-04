#Alexander_Máni_Einarsson
#19/09/19
#aukaverkefni_(while)

print()
print("Vinsamlegast skráðu þig inn til að versla á netfatamarkaði Siggu og Grétars")
nafn = input("Sláðu inn nafn: ")
kt = input("Sláðu inn kennitölu: ")
print()
karfa = "Vörunar þínar: \n"
verð = 0

on = True
while on:
    print()
    print("Velkomin/nn á fatmarkað Siggu og Grétars")
    print("Vinsamlegast sláðu inn númer á þeiiri vöru sem þú vilt panta: ")
    print("-----------------------------")
    print("1. Herra skyrtur -6.000kr")
    print("2. Dömu skyrtur -6.000kr")
    print("3. Herra buxur -5.000kr")
    print("4. Dömu buxur -5.000kr")
    print("5. Herra sokkar -1.000kr")
    print("6. Dömu sokkar -1.000kr")
    print("7. Herra skór -8.000kr")
    print("8. Dömu skór -8.000kr")
    print("-----------------------------")
    print("9. Hætta")
    print("0. Skoða körfu")
    print()
    svar = int(input("Veldu möguleika"))


    if svar == 1:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Herra skyrta -6.000kr, \n"
        verð = verð + (6000 * magn_tala)
    elif svar == 2:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn + " x Dömu skyrta -6.000kr\n"
        verð = verð + (6000 * magn_tala)
    elif svar == 3:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Herra buxur -5.000kr,\n"
        verð = verð + (5000 * magn_tala)
    elif svar == 4:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Dömu buxur -5.000kr,\n"
        verð = verð + (5000 * magn_tala)
    elif svar == 5:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Herra sokkar -1.000kr,\n"
        verð = verð + (1000 * magn_tala)
    elif svar == 6:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Dömu sokkar -1.000kr,\n",
        verð = verð + (1000 * magn_tala)
    elif svar == 7:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Herra skór -8.000kr,\n"
        verð = verð + (8000 * magn_tala)
    elif svar == 8:
        magn = input("Sláðu inn magn: ")
        magn_tala = int(magn)
        karfa = karfa + magn +" x Dömu skór -8.000kr,\n"
        verð = verð + (8000 * magn_tala)
    elif svar == 0:
        print(karfa)
        print("þetta kosta þá",verð,"kr")
    elif svar == 9:
        print()
        print("************************")
        print("Fatamarkaður Siggu og Grétars")
        print("--------------------")
        print("reikningur")
        print(karfa)
        print("Verð: ",verð,"kr")
        print("viðskiptavinur")
        print(nafn)
        print(kt)
        print("--------------------")
        print("Þakkir fyrir að velja fatamarkað Siggu og Grétars")
        print("************************")
        quit()





