#Alexander_Máni_Einarsson
#12/11/19
#Skilaverkefni 6

import random

on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni 6<-=-=-=")
    print()
    print("1. Random tölur")
    print("2. Talnabil")
    print("3. Strengjalisti")
    print("4. Samanburður")
    print("5. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print("Hér tekur foritið inn 50 tölur á bilini 5-70 að handahófi")
        print("og prentar síðan út ýmsar staðreyndir")
        talnalisti = []
        #50 random tölur á milli 5 og 70 fengnar
        for x in range(50):
            tala = random.randint(5,70)
            talnalisti.append(tala)
        teljari = 0
        margfeldi = 1
        #Allar tölur margfaldaðar
        for x in range(len(talnalisti)):
            margfeldi = margfeldi * talnalisti[teljari]
            teljari = teljari + 1
        #Ýmsar upplýsingar um listann, talnsalisti fenginn, útskýringar í græna letrinu
        print("Hér er margfeldi allra staka listans", margfeldi)
        print("Hæsta stak listans er : ", max(talnalisti))
        print("Minnsta stak listans er: ", min(talnalisti))
        print("Hér er talnalistinn útprentaður: ",talnalisti)
        talnalisti.sort()
        print("Hér er talnalistinn raðaður og útprentaður: ",talnalisti)

    elif val == 2:
        print()
        tala = 2000
        talnalisti = []
        #Tölunar eiga að ver frá 2000-32000. það eru 1200 þar á milli svo það er range-ið svo fer það í if klausu sem finnur út hvort það gengur upp í 7 en ekki 5
        for x in range(1200):
            tala = tala + 1
            if tala % 7 == 0 and tala % 5 != 0:
                talnalisti.append(tala)
        teljari = 0
        #Foritið leggur saman allar tölunar í listanum í þessari slaufu
        for x in range(len(talnalisti)):
            print(" Allar tölur listans í beinni línu með kommur á milli: ",talnalisti[teljari],",", end=" ")
            teljari = teljari + 1
        print("\n","Summa allra a talna listans: ",sum(talnalisti))

    elif val == 3:
        print()
        teljari = 0
        ordalisti = []
        #Whie lykkja sem keyrir 10 sinnum
        while teljari < 10:
            ordin = input("Sláðu inn orð til að bæta í lista: ")
            ordalisti.append(ordin)
            teljari = teljari + 1
        teljari = 0
        print()
        print("Hér er annaðhvert orð í listanum skrifað út öfugt")
        for x in range(len(ordalisti)):
            stak = ordalisti[teljari]
            if teljari % 2 == 0:
                print(stak[::-1])
            teljari = teljari + 1
        print()
        #Listinn aðeins raðaur í prentun svo hann helst óbreyttur í raun
        print("Hér er listinn raðaður: ", sorted(ordalisti))
        print()
        stafur = input("Sláðu inn þann staf sem á að eyða orðum með sama upphafsstaf: ")
        teljari = 0
        staf_teljari = 0
        nyr_listi = []
        print()
        #Nýr listi búinn með þeim orðum sem haf ekki sama upphafstaf og notandi gefur sem lætur það lýta út eins og eytt hefur verið þeim orðum sem byrja á þeim staf.
        for x in range(len(ordalisti)):
            stak = ordalisti[teljari]
            if stafur != stak[0]:
                nyr_listi.append(stak)
            else:
                staf_teljari = staf_teljari +1
            teljari = teljari + 1
        print()
        print(staf_teljari, "Staf/Stöfum var eytt")
        print()
        print("Hér er listinn út prentaður með eyddu orðunum: ",nyr_listi)

    elif val == 4:
        print()
        ordalisti = []
        teljari = 0
        #While lykkja sem keyrir 7 sinnum
        while teljari < 7:
            ordin = input("Sláðu inn orð til að bæta í lista: ")
            ordalisti.append(ordin)
            teljari = teljari + 1
        teljari = 0
        ordalisti_2 = []
        # While lykkja sem keyrir 6 sinnum
        while teljari < 6:
            ordin = input("Sláðu inn orð til að bæta í lista 2: ")
            ordalisti_2.append(ordin)
            teljari = teljari + 1
        nyr_listi = []
        teljari_1 = 0
        # While lykkja sem keyrir 7 sinnum
        #Með for lykkjunni fyrir neðan lætur þetta hvert einasta orð í báðum listum bers gi saman við hvort annað.
        while teljari_1 < 7:
            teljari = 0
            #Þetta keyrir sex sinnum
            for x in range(len(ordalisti_2)):
                stak = ordalisti[teljari_1]
                stafur = ordalisti_2[teljari]
                #Þau orð sem eru eins í báðum listum eru færð yfir í nýjan lista til að safna þeim sem eru eins
                if stafur == stak:
                    nyr_listi.append(stak)
                teljari = teljari + 1
            teljari_1 = teljari_1 + 1
        print("Eftirfarandi orð eru eins í báðum listum", nyr_listi)

    elif val == 5:
        print("Nú verður foritinu hætt")
        quit()

    else:
        print("Villa hefur komið upp")
