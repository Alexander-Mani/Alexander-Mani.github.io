#Alexander_Máni_Einarsson
#29/08/19
#Skilaverkefni_1

#liður_1:
#Hér fær foritið gildi fyrir nafn notenda m.ö.o. fyrir breytuna "nafn". Einnig skilgreinir það að gildið eigi að vera texti(str)
nafn = str(input("Góðan daginn, hvað heitir þú?"))
#Hér fær foritið gildi fyrir uppáhalds áfanga notenda m.ö.o. fyrir breytuna "afangi". Einnig skilgreinir það að gildið eigi að vera texti(str)
afangi = str(input("Hvert er þitt uppáhalds fag"))
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) með áður ákveðnu gildi fyrir breytunar "afangi" og "nafn"
print("velkomin/nn í áfangann,", afangi, "Þetta verður skemmtileg önn hjá okkur,", nafn)

#milliliður_1
#Ath þessi milliliður kemur fyrir fimm sinnum og verður þar að leiðandi bara útskýrður einu sinni.
#Hér fær foritið gildi fyrir svar notenda m.ö.o. fyrir breytuna "naest_1". Einnig skilgreinir það að gildið eigi að vera texti(str)
naest_1 = str(input("Viltu halda áfram í næsta lið(J/N)"))
#Hér segir foritð að ef(if) textinn er eftirfarandi eða(or) eftirfarandi eigi að...
if naest_1 == str("J") or naest_1 == str("j"):
    #Prenta eftirfarandi texta(Allt sem er grænt)(svo heldur foritið sjálfkrafa áfram í næsta lið).
    print("Nú verður haldið áfram:")
#Hér segir foritð að ef ekkert áður upptalið á við(elif) og textinn er eftirfarandi eða(or) eftirfarandi eigi að...
elif naest_1 == str("N") or naest_1 == str("n"):
    #Prenta eftirfarandi texta(Allt sem er grænt).
    print("Nú verður foritnu lokað")
    #Loka(quit) foritinu(())
    quit()
#Hér segir foritð að ef ekkert annað eigi við(else) og textinn er eftirfarandi eða(or) eftirfarandi eigi að...
else:
    #Prenta eftirfarandi texta(Allt sem er grænt)(svo heldur foritið sjálfkrafa áfram í næsta lið).
    print("Svarið þitt var ekki nægilega skýrt, nú heldur foritið áfram:")


#liður_2:
#Hér prentar foritið út lýsingu á eftirfarandi aðgerðum:
print("Hæ, hér gerir foritið pínu stærðfræði")
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "tala". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
tala = int(input("Sláðu inn heila tölu sem er hærri en 100"))
#Hér segir foritð að ef(if) talan er hærri en 100 eigi að...
if tala > 100:
    #Deila með henni í töluna 5,5 og síðan breyta gildiinu á breytunni "tala" í útkomuna. Einnig skilgreinir það að gildið eigi að vera kommutala(float).
    tala = tala/float(5.5)
    #Hér prentar foritið út eftir farandir texta(Allt sem er grænt) og útkommunna sem er núverandi gildi breytunnar "tala" einnig námundar(round) foritið upp að tveimur(2) aukastöfum.
    print("Talan þín deild í 5,5 er:", round(tala, 2))
#Hér segir foritð að ef ekkert annað eigi við...
else:
    #Prenta eftirfarandi texta(Allt sem er grænt).
    print("Þú hefur ekki slegið inn það sem beðið var um")

#milliliður_2
naest_1 = str(input("Viltu halda áfram í næsta lið(J/N)"))
if naest_1 == str("J") or naest_1 == str("j"):
    print("Nú verður haldið áfram:")
elif naest_1 == str("N") or naest_1 == str("n"):
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þitt var ekki nægilega skýrt, nú heldur foritið áfram:")

#liður_3
#Hér prentar foritið út lýsingu á eftirfarandi aðgerðum:
print("Hæ, hér gerir foritið pínu stærðfræði")
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "tala_1". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
tala_1 = int(input("Sláðu inn tvær heilar tölu. Fyrri töluna hér:"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "tala_2". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
tala_2 = int(input("Seinni töluna hér:"))
#Hér reiknar foritið út margfeldi gildi breytnanna "tala_1" og "tala_2" og notar útkomunna til að finna gildi breytunnar "tala_3".
tala_3 = tala_1*tala_2
#Hér reiknar foritið út frádrátt gildi "tala_1" frá gildi "tala_2" og notar útkomunna til að finna gildi breytunnar "tala_4".
tala_4 = tala_2-tala_1
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) og birtir gildi "tala_3" og "tala_4" þar sem breytunnar standa.
print("Margfeldi talnana er:", tala_3, "Frádráttur fyrri tölunar frá þeirri seinni er:", tala_4)

#milliliður_3
naest_1 = str(input("Viltu halda áfram í næsta lið(J/N)"))
if naest_1 == str("J") or naest_1 == str("j"):
    print("Nú verður haldið áfram:")
elif naest_1 == str("N") or naest_1 == str("n"):
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þitt var ekki nægilega skýrt, nú heldur foritið áfram:")

#liður_4
#Hér prentar foritið út lýsingu á eftirfarandi aðgerðum:
print("Hæ, hér reiknar foritið út rúmmal rétthyrnings")
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "l". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
l = int(input("Hver er lengd rétthyrningsins?"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "b". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
b = int(input("Hver er breidd rétthyrningssins?"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "h". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
h = int(input("Hver er hæð rétthyrningssins?"))
#Hér reiknar foritið út gildi fyrir "r" með því að margfalda saman gildi "l", "b" og "h".
r = l*b*h
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) og gildi "r".
print("Rúmmál rétthyrningssins er:", r)

#milliliður_4
naest_1 = str(input("Viltu halda áfram í næsta lið(J/N)"))
if naest_1 == str("J") or naest_1 == str("j"):
    print("Nú verður haldið áfram:")
elif naest_1 == str("N") or naest_1 == str("n"):
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þitt var ekki nægilega skýrt, nú heldur foritið áfram:")

#liður_5
#Hér prentar foritið út lýsingu á eftirfarandi aðgerðum:
print("Hæ, hér reiknar foritið út aldur föður þíns þegar þú fæddist")
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "aldur_1". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
aldur_1 = int(input("Hve gammal/gömul ert þú í árum?"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "aldur_2". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
aldur_2 = int(input("Hve gamall er faðir þinn í árum?"))
#Hér reiknar foritið út gildi á "aldur_3" með því að draga "aldur_1" frá "aldur_2"
aldur_3 = aldur_2-aldur_1
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) og gildi fyrir "aldur_3".
print("þegar þú fæddist var pabbi þinn:", aldur_3,"ára")

#milliliður_5
naest_1 = str(input("Viltu halda áfram í næsta lið(J/N)"))
if naest_1 == str("J") or naest_1 == str("j"):
    print("Nú verður haldið áfram:")
elif naest_1 == str("N") or naest_1 == str("n"):
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þitt var ekki nægilega skýrt, nú heldur foritið áfram:")

#liður_6
#Hér prentar foritið út lýsingu á eftirfarandi aðgerðum:
print("Hæ, hér reiknar foritið út meðalaldur þriggja einstaklinga.")
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "nafn". Einnig skilgreinir það að gildið eigi að vera texti(str)
nafn = str(input("Til að byrja sláðu inn nafnið þitt?"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "madur_1". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
madur_1 = int(input("Sláðu inn aldur fyrsta einstaklingsins"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "madur_2". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
madur_2 = int(input("Sláðu inn aldur annars einstaklingsins"))
#Hér fær foritið gildi fyrir tölu notenda m.ö.o. fyrir breytuna "madur_3". Einnig skilgreinir það að gildið eigi að vera heiltala(int)
madur_3 = int(input("Sláðu inn aldur síðasta einstaklingsins"))
#Hér reiknar foritið út gildi fyrir "medalaldur" með að leggja saman gildi "madur_1," "madur_2" og "madur_3"
medalaldur= madur_1+madur_2+madur_3
#Hér reiknar foritið út nýtt gildi fyrir "medalaldur með því að deila gildinu í þrennt". Þessum reikingum er skipt í tvennt í stað þess að gera stærfræðilegan sviga.
medalaldur= medalaldur/3
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) og gildi fyrir "medalaldur".
print("Meðalaldur einstaklinganna er:", medalaldur)
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt) og gildi fyrir "nafn".
print("Gaman að geta aðstoðað þig við þessa útreikninga,", nafn)
#Hér prentar foritið út eftirfarandi texta(Allt sem er grænt).
print("Þakkir fyrir að prufa foritið mitt")

