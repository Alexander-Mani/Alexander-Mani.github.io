#Alexander_Máni_Einarsson
#09/01/20
#Æfingaverkefni_2_Upprifjun

on = True
while on:
    print()
    print("=-=-=-> Upprifjun <-=-=-=")
    print()
    print("1. Hæð og nöfn")
    print("2. Ekrur")
    print("3. Ekru í töflu")
    print("4. Áfangaheiti")
    print("5. Prósentureikningur")
    print("6. Hætta")

    val = int(input("Veldu: "))
    if val == 1:
        print()
        print("Sláðu inn nöfn tveggja einstaklinga og hæð þeirra: ")
        nafn_1 = input("Sláðu inn fyrra nafnið: ")
        haed_1 = input("Sláðu inn hæð fyrri einstaklingsins í cm: ")
        nafn_2 = input("Sláðu inn seinna nafnið: ")
        haed_2 = input("Sláðu inn hæð seinni einstaklingsins í cm: ")
        print("Fyrra nafn: ",nafn_1)
        print("Hæð í cm: ", haed_1)
        print("Seinna nafn: ", nafn_2)
        print("Hæð í cm: ", haed_2)
        if haed_1 == haed_2:
            print(nafn_1," og ",nafn_2," eru jafn há")
        elif haed_1 < haed_2:
            print(nafn_2, " er stærri en ", nafn_1,)
        elif haed_1 > haed_2:
            print(nafn_1, " er stærri en ", nafn_2,)

    elif val == 2:
        print()
        print("Forritið gefur upp stærð flets í ekrum: ")
        l = int(input("Sláðu inn lengd í metrum"))
        b = int(input("Sláðu inn breidd í metrum"))
        staerd = (l*b)/4046
        print("Þetta eru þá", staerd,"ekrur")
    elif val == 3:
        x = 0
        b = int(input("Sláðu inn breidd í metrum"))
        print("Þetta eru þá stærðin í ekrum")
        print("Stærð          Lengd í ekrum")
        while x < 100:
            x = x + 10
            staerd = (x * b) / 4046
            print(" ",x,"        ",staerd,)

    elif val == 4:
        print()
        afangi = input("Sláðu inn afangaheiti")
        teljari = 0
        if len(afangi) != 7:
            print("þetta er ekki gilt áfangaheiti(Ath lengd)")
            break
        for x in range(len(afangi)):
            stafur = afangi[teljari]
            if teljari < 3:
                if stafur.isalpha() and stafur.isupper:
                    ""
            elif teljari > 3:
                if stafur.isdigit():
                    ""
            else:
                print("þetta er ekki gilt áfangaheiti")
                print()
            teljari = teljari + 1
        print("þetta er rétt áfanga heiti")


    elif val == 5:
        heild = int(input("Heildin:"))
        hluti = int(input("Hver er %?"))
        reikningur = heild//hluti
        print("Niðurstaðan er",reikningur)
    elif val == 6:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
