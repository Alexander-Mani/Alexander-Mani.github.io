#Alexander_Máni_Einarsson
#09/01/20
#Æfingaverkefni_1_Upprifjun

on = True
while on:
    print()
    print("=-=-=-> Upprifjun <-=-=-=")
    print()
    print("1. Tvær tölur")
    print("2. Fullt nanfn")
    print("3. Km í m")
    print("4. Launareiknivél")
    print("5. Launareiknivél m/ skatt")
    print("6. Gráður")
    print("7. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print("Sláðu inn tvær tölur:")
        tala_1 = int(input("Sláðu inn Tölu 1: "))
        tala_2 = int(input("Sláðu inn Tölu 2: "))
        summa = tala_1 + tala_2
        margfeldi = tala_1 * tala_2
        print("Summan er", summa)
        print("Margfeldið er", margfeldi)

    elif val == 2:
        print()
        print("Góðan daginn, vinsamlegast:")
        fornafn = input("Sláðu inn fornafn: ")
        eftirnafn = input("Sláðu inn eftirnafn: ")
        print("Halló",fornafn, eftirnafn)

    elif val == 3:
        print()
        print("Forritið umbreytir Km(kílómetrum) í m(metrar) ")
        km = float(input("Sláðu inn kílómetrafjöld: "))
        m = km * 1000
        print("Það eru",m,"metrar")

    elif val == 4:
        print()
        print("Launareiknivél: ")
        laun = int(input("Laun á klst: "))
        timi = int(input("Námundaðar fjöldi klukkustunda"))
        heildarlaun = laun * timi
        print("Heildarlaunin þín eru þá", heildarlaun,"Krónur")
    elif val == 5:
        print()
        print("Launareiknivél: ")
        laun = int(input("Laun á klst: "))
        timi = int(input("Námundaðar fjöldi klukkustunda"))
        heildarlaun = laun * timi
        if heildarlaun < 30000:
            print("Heildarlaunin þín eru þá", heildarlaun,"Krónur")
        elif heildarlaun > 30000:
            heildarlaun_2 = heildarlaun - 30000
            skattur = heildarlaun_2 * 0.2
            print("Heildarlaunin þín eru þá", heildarlaun,"Krónur")
            print("Skattur er þá", skattur,"Krónur")
        else:
            print("Villa hefur komið upp!")

    elif val == 6:
        gradur = int(input("Sláðu inn gráður: "))
        hringur = gradur//360
        afgangur = gradur % 360
        if afgangur != 0:
            print("Þetta er þá",hringur,"Hringir og",afgangur,"gráður")
        elif afgangur == 0:
            print("Þetta er þá", hringur, "Hringir")

    elif val == 7:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
