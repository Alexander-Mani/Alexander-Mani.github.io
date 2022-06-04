#Alexander_Máni_Einarsson
#16/01/20
#Æfingaverkefni_4 upprifjun frh

import random

on = True
while on:
    print()
    print("=-=-=-> Upprifjun frh <-=-=-=")
    print()
    print("1. n/N fjöldi ")
    print("2. Tvö nöfn ")
    print("3. Samhverf nöfn ")
    print("4. Texti ")
    print("5. Listi ")
    print("6. Hætta ")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print("Þetta forrit tekur inn setningu og athugar hve mörg n eru í henni")
        texti = input("Sláðu inn setningu")
        teljari = 0
        n_fjoldi = 0
        for x in range(len(texti)):
            stafur = texti[teljari]
            teljari = teljari + 1
            if stafur == "n" or stafur == "N":
                n_fjoldi = n_fjoldi +1
        print("Það er",n_fjoldi,"n, bæði lítil sem stór í textanum")


    elif val == 2:
        print()
        print()
        print("Þetta forrit tekur inn nöfn og athugar með lengdina")
        texti = input("Sláðu fyrra nafnið")
        texti_2 = input("Sláðu inn seinna nafnið")
        teljari = 0
        magn = 0
        nafnalisti = []
        talnalisti = []
        lengd = len(texti)
        lengd_2 = len(texti_2)
        if lengd == lengd_2:
            print("Nöfnin eru jafn löng")
            minna = texti
        elif lengd < lengd_2:
            print("Seinna nafnið er stærra en hið fyrra")
            minna = texti
        elif lengd > lengd_2:
            print("Fyrra nafnið er stærra en hið seinna")
            minna = texti_2
        for x in range(len(minna)):
            stafur = texti[teljari]
            stafur_2 = texti_2[teljari]
            teljari = teljari + 1
            if stafur == stafur_2:
                nafnalisti.append(stafur)
                talnalisti.append(teljari)
                magn = magn +1
        teljari = 0
        for x in range(magn):
            print("Bókstafur nr.",talnalisti[teljari],nafnalisti[teljari],"er eins í báðum nöfnum")
            teljari = teljari + 1

    elif val == 3:
        print()
        print("Hér athugar forritið hvort nafn sé samhverft sjálfum sér")
        nafn = input("Sláðu inn nafn")
        aftur_nafn = nafn[::-1]
        if nafn == aftur_nafn:
            print("Þetta nafna er samhverft")
        else:
            print("Þetta nafn er ekki samhverft")
    elif val == 4:
        print()
        texti = input("Sláðu inn texta")
        on = True
        while on:
            print()
            print("=-=-=-> Texti <-=-=-=")
            print()
            print("1. Orðafjöldi ")
            print("2. Er orðið hestur í textanum")
            print("3. Lengd")
            print("4. Aftur á bak")
            print("5. Stór stafur")
            print("6. Er stafurinn þinn í textanum")
            print("7. A í stað a")
            print("0. Hætta")
            val = int(input("Veldu: "))
            if val == 1:
                print()
                teljari = 0
                ord = 1
                for x in range(len(texti)):
                    stafur = texti[teljari]
                    teljari = teljari +1
                    if stafur == " ":
                        ord = ord +1

                print("Það eru ",ord,"orð í textanum")

            elif val ==2:
                if "hestur" in texti:
                    print("hestur er í textanum ")
                else:
                    print("hestur er ekki í textanum")

            elif val ==3:
                print()
                lengd = len(texti)
                print("lengd textans er:",lengd,"stafir")

            elif val ==4:
                print()
                ofugt = texti[::-1]
                print("Svona er textinn öfugur:",ofugt)

            elif val ==5:
                print()
                hastafir = texti.uppercase
                print("Svona er textinn í hástöfum:",hastafir)

            elif val ==6:
                print()
                print("Sláðu inn staf forritið athugar svo hvort hann sé í textanum")
                stafur_not = input("Sláðu inn staf")
                teljari = 0
                fjoldi = 0
                for x in range(len(texti)):
                    stafur = texti[teljari]
                    teljari = teljari + 1
                    if stafur == stafur_not or stafur == stafur_not.uppercase:
                        fjoldi = fjoldi +1
                if fjoldi > 0:
                    print("Já og hann kemur fyrir",fjoldi,"Sinnum")
                else:
                    print("Nei")


            elif val ==7:
                teljari = 0
                texti_proxy = texti.replace("a","A")
                print(texti_proxy)

            elif val ==0:
                off = True
    elif val == 5:
        print()
        heild = 0
        talnalisti = []
        for x in range(100):
            tala = random.randint(250, 400)
            heild = heild + tala
            talnalisti.append(tala)
        medaltal = heild/100
        milli_fjoldi = 0
        minni_fjoldi = 0
        minnsta_tala = 0
        for x in range(100):
            tala_2 = talnalisti[x]
            print(tala_2)

            if tala_2 > 299 and tala_2 < 351:
                milli_fjoldi = 1 + milli_fjoldi
            if tala_2 > 268:
                minni_fjoldi = minni_fjoldi +1
            if tala_2 == min(talnalisti):
                minnsta_tala = minnsta_tala +1
        print("Meðaltal talnana er: ", medaltal)
        print("Fjöldi talna undir 267 er: ",minni_fjoldi)
        print("Minnsta talan er: ", min(talnalisti),"hún kemur fram", minnsta_tala,"sinnum")
        print("Fjöldi talna á milli 300-350 er: ", milli_fjoldi)



    elif val == 6:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
