#Alexander_Máni_Einarsson
#01/23/20
#Skilaverkefni_1
import random

on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni 1 <-=-=-=")
    print()
    print("1. Strengjalisti ")
    print("2. Random-tölur")
    print("3. Skráning í áfanga ")
    print("4. Listi fyrir tölur")
    print("5. Teningakast")
    print("6. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        #listi til að geyma fimm nöfnin
        nafnalisti = []
        print("Sláðu inn 5 nöfn")
        #for lykkja sem safnar 5 nöfnum
        for x in range (5):
            nafn = input("Sláðu inn nafn:")
            nafnalisti.append(nafn)
        svar = 0
        #valmynd fyrir strengjalista
        while svar != 5:
            print()
            print("=-=-=-> Strengjalisti <-=-=-=")
            print()
            print("1. Birta nöfnin óraðað")
            print("2. Raða nöfnunum í stafrófsröð og birta")
            print("3. Raða nöfnunum í öfuga stafrófsröð og birta")
            print("4. Birta eitt nafn eftir því hvaða númer 1-5 var valið")
            print("5. Hætta í verkefni 3")
            svar = int(input("Veldu: "))
            if svar == 1:
                print()
                #For lykkja til að prenta nöfnin snyrtilega
                for x in range(5):
                    print(nafnalisti[x])

            elif svar ==2:
                print()
                #Nýr listi búinn til til að skemma ekki þann upprunulega
                stafrof_nafnalisti = nafnalisti
                #Nýji listinn raðaður í stafrófsröð
                stafrof_nafnalisti.sort()
                # For lykkja til að prenta nöfnin snyrtilega í stafrófsröð
                for x in range(5):
                    print(stafrof_nafnalisti[x])

            elif svar == 3:
                print()
                # Nýr listi búinn til til að skemma ekki þann upprunulega
                ofug_stafrof_nafnalisti = stafrof_nafnalisti
                # Nýji listinn raðaður í öfuga stafrófsröð
                ofug_stafrof_nafnalisti.reverse()
                # For lykkja til að prenta nöfnin snyrtilega í stafrófsröð
                for x in range(5):
                    print(ofug_stafrof_nafnalisti[x])
            elif svar == 4:
                print()
                #Prenta listan við númeri til hliðar
                for x in range(5):
                    y = x+1
                    print(y,". ", stafrof_nafnalisti[x])
                print()
                #Lætur notenda velja númerið á því nafni sem hann vill prenta
                tala = int(input("veldu númerið á því nafni sem þú vilt prenta: "))
                tala = tala - 1
                print()
                print(stafrof_nafnalisti[tala])

            #Hætti sjálfkrafa því fimm lætur while lykjuna hætta
            elif svar == 5:
                ""

    elif val == 2:
        print()
        talnalisti = []
        tverifimmeinn = 0
        nulll = 0
        #for lykkja sem velur 70 tölur á milli 1-1500
        for x in range(70):
            tala = random.randint(1, 1500)
            talnalisti.append(tala)
            #if skipun sem telur tölur ef þær eru hææri en 0 og minni en 251
            if tala > 0 and tala < 251:
                nulll = nulll +1
            #if skipun sem telur tölur ef þær eru hææri en 250 og minni en 501
            if tala > 250 and tala < 501:
                tverifimmeinn = tverifimmeinn +1
        teljari = 0
        print("Listinn eins og hann varð til með 4 tölum í dálk")
        #Tvöföld for slaufa til að keyra listann af tölunum í 4 dálkum (17*4=68)(68+2=70)
        #4 dálkanir eru keyrði 17 sinnum og svo tvisvar í viðbót til að ná yfir allar tölur listans
        for x in range(17):
            for x in range(4):
                print(talnalisti[teljari],end=", ")
                teljari = teljari + 1
            print("\n")
        for x in range(2):
            print(talnalisti[teljari], end=", ")
            teljari = teljari + 1
        print("\n")
        print()
        #minnsta talan prentuð(min) og stærsta (max)
        print("Stærsta talan er: ",max(talnalisti)," & minnsta talan er: ", min(talnalisti))
        print()
        print("Tölur 6 saman í dálk í öfugri röð:")
        #Öfugur listi af tölunum búinn til
        ofugur_talnalisti = talnalisti
        ofugur_talnalisti.reverse()
        teljari = 0
        print()
        # Tvöföld for slaufa til að keyra listann af tölunum í 6 dálkum (11*6=66)(66+4=70)
        # 6 dálkanir eru keyrðir 11 sinnum og svo 4 sinnum í viðbót til að ná yfir allar tölur listans og tölunar eru síðan prentaðar öfugt með nýja listanum
        for x in range(11):
            for x in range(6):
                print(ofugur_talnalisti[teljari],end=", ")
                teljari = teljari + 1
            print("\n")
        for x in range(4):
            print(ofugur_talnalisti[teljari], end=", ")
            teljari = teljari + 1
        print("\n")
        print()
        #Fjöldi talnana á áður skilgreindum og bilum birtur
        print("Tölur á bilinu 1-250 voru: ", nulll,". Tölur á bilinu 251-500 voru: ", tverifimmeinn)



    elif val == 3:
        print()
        nafnalisti = []
        #SPyr notenda hve margir eru skráðir í áfanga
        fjoldi = int(input("Hve margir eru skráðir í hópinn FOR1TÖ05BU?"))
        #For slaufa búinn til með lengd notenda
        #Notendi er síðan biðinn um að fylla í pláss áfangans með nöfnum
        for x in range(fjoldi):
            nafn = input("Sláðu inn nafna þáttakanda")
            nafnalisti.append(nafn)
        svar = 0
        #While lykkja fyrirr valmynd áfanga
        while svar != 5:
            print()
            print("=-=-=-> FOR1TÖ05BU <-=-=-=")
            print()
            print("1. Stafrófsraðaður listi")
            print("2. Eyða")
            print("3. Bæta við")
            print("4. Prenta")
            print("5. Hætta")
            svar = int(input("Veldu: "))
            if svar == 1:
                print()
                # Nýr listi búinn til til að skemma ekki þann upprunulega
                # Nýji listinn raðaður í stafrófsröð með sort()
                #veit ég hefði get notað print(... .sorted()) en ákvað að gera þetta svona
                stafrofs_nafnalisti = nafnalisti
                stafrofs_nafnalisti.sort()
                #for slaufa sem prentar út listann snyrtilega 1 nafn í dálki
                for x in range(fjoldi):
                    print(stafrofs_nafnalisti[x])

            elif svar == 2:
                print()
                # for slaufa sem prentar út listann snyrtilega 1 nafn í dálki
                for x in range(fjoldi):
                    print(nafnalisti[x])
                print()
                #notandi slær inn nafna sem hann vill eyða
                nafn = input("Sláðu inn nafnið á þeim sem þú villt eyða úr hópnum: ")
                #forritið athugar hvort nafnið sé í áfanganum(nafnalistanum)
                if nafn in nafnalisti:
                    nafnalisti.remove(nafn)
                    #Ef þessi slaufa keyrist eyðist eytt nafn og því þarf að breyta fjolda
                    fjoldi = fjoldi -1
                    print("Listinn hefur verið uppfærður")
                else:
                    print("Þú hefur ekki slegið inn rétt nafn")

            elif svar == 3:
                print()
                # notandi slær inn nafna sem hann vill bæta
                nafn = input("Sláðu inn nafnið á þeim sem þú villt bæta í hópinn: ")
                nafnalisti.append(nafn)
                #Sama hvað noteandi slær breytist það í listann því við erum ekki með neina nafna fordóma og því bætist við einn í hópinn
                fjoldi = fjoldi +1
                print("Listinn hefur verið uppfærður")
                #prentar út listann til að sýna breytingar
                for x in range(fjoldi):
                    print(nafnalisti[x])

            elif svar == 4:
                print()
                #prentar ú tlistann snyritlega
                for x in range(fjoldi):
                    print(nafnalisti[x])

            elif svar == 5:
                print()
                #Þegar valið er "5" hætti valmyndinn út af skylirðinu í while
                print("Nú verður valmyndinni hætt")
            else:
                print("Villa hefur komið upp")



    elif val == 4:
        print()
        talnalisti = []
        print("Sláðu inn sjö tölur")
        summa = 0
        fimmtiukommafimm = 0
        #For slaufa sem setur 7 nöfn frá notenda inn í lista
        for x in range(7):
            tala = int(input("Sláðu inn tölu: "))
            talnalisti.append(tala)
            #Ef skylirði sem telur hvort talan 50.5 eð eh minni tala komi upp og hve oft
            if tala <= 50.5:
                fimmtiukommafimm = fimmtiukommafimm +1
            summa = tala + summa
        #Útskýris sig sjálft hvað gengur á hér
        medaltal = summa/ 7
        print()
        print("Hæsta talan er: ",max(talnalisti))
        print("Lægsta talan er: ", min(talnalisti))
        print("Meðaltal talnana er: ",medaltal)
        print("Summa talnana er", summa)
        print()
        radadur_talnalisti = talnalisti
        radadur_talnalisti.sort()
        #for slaufa sem prentar allan listan snyrtilegan(raðaða útgáfu
        for x in range(7):
            print(radadur_talnalisti[x])
        print()
        #for slaufa sem raðar upp talnalistanum í beina línu með ; á milli
        for x in range(7):
            print(talnalisti[x], end="; ")
        print()
        #Loks er prentað skylirðið sem áðan var talið
        if fimmtiukommafimm > 1:
            print("Það eru tölur sem jafngilda eða eru jafnar og 50,5 þær eru: ", fimmtiukommafimm)


    elif val == 5:
        print()
        oftlisti = []
        #Fáum frá notend hve oft hann vill kast tveimur teningum
        oft = int(input("Hve oft viltu kasta?: "))
        teningakast = []
        #For slaufa sem keyrir jafn oft og notendi bað upp og kemur með tölur frá 1 upp í 6 tvisvar og bætir í lista og prentar umm leið köstin og byrtir númer
        for x in range(oft):
            kast = random.randint(1,6)
            kast_2 = random.randint(1,6)
            print("Kast nr.",x+1,"\t Teningur eitt=",kast,"\t Teningur tvö=",kast_2)
            teningakast.append(kast)
            teningakast.append(kast_2)
        print()
        #For slaufa sem  sen keyrir einu sinni fyrir hverja hlið á tening og telur þá hve margar tölur eru í listanum af þeirri hlið og byrtir
        for x in range(1,7):
            oftlisti.append(teningakast.count(x))
            print(x,"kom upp",teningakast.count(x))
        print()
        #Finnum tölunu sem kom oftast með max
        oftast = max(oftlisti)
        print("Talan sem kom oftast er:",oftlisti.index(oftast)+1)
        #finnum tölunu sem kom sjaldnast með min
        print("Talan sem kom sjaldnast er:", oftlisti.index(min(oftlisti)) + 1)

    elif val == 6:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
