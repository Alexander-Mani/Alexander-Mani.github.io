#Alexander_Máni_Einarsson
#03/09/19
#skilaverkefni_2

#liður1
print()
#Hér fær foritið gildi fyrir þrjár tölur:
print("Hæ, beðið verðu um þrjár tölur, ekki má skrifa inn sömu töluna tvisvar. Foritið segir svo hver talnana á heima í miðjunni ")
tala_1 = int(input("Sláðu inn fyrstu töluna: "))
tala_2 = int(input("Sláðu inn aðra töluna: "))
tala_3 = int(input("Sláðu inn þriðju töluna: "))
#Hér útskýrir foritið með stærðfræði að ef eh talnanna sé eins eigi ekki að halda áfram
if tala_1 == tala_2 or tala_2 == tala_3 or tala_1 == tala_3:
    print("Tvær eða fleiri tölur voru eins")
#Hér notar foritð stærðfræðði til að finna út hvort eh af tölunum sé í miðjunni, ef svo er prentar foritið út svarið.
    #Tala 1
elif (tala_1 < tala_2 and tala_1 > tala_3) or (tala_1 > tala_2 and tala_1 < tala_3):
    print("Fyrsta talan er í miðjunni")
    #Tala 2
elif (tala_2 < tala_1 and tala_2 > tala_3) or (tala_2 > tala_1 and tala_2 < tala_3):
    print("Önnur talan er í miðjunni")
    #Tala #
elif (tala_3 < tala_2 and tala_3 > tala_1) or (tala_3 > tala_2 and tala_3 < tala_1):
    print("Þriðja talan er í miðjunni")
else:
    print("þú hefur ekki slegið inn rétt")

#milliliður
#Ath þessi liður kemur 4 sinnum og verðu því aðeins útskýrður einu sinni
#Hér er milliðliður svo næsti liður fylli ekki strax upp skjáin
afram= input("Viltu halda áfram(j/n)?")
#Hér spyr foritið hvort notendi vilji halda áfram
#Ef valið er já prentar foritið út eftirfarandi græna text og heldur sjálfkrafa áfram(Innbyggður eiginleiki í Python)
if afram == "j" or afram == "J":
    print("Nú verður haldið áfram")
#Ef valið er nei prentar foritið út eftir farandi græna texta og lokar foritinu
elif afram == "n" or afram == "N":
    print("Nú verður foritnu lokað")
    quit()
#Annars heldur það bara áfram
else:
    print("Svarið þit var ekki nægilega skýrt, nú verður haldið áfram")

#liður2
print()
#Foritið prentar út valmöguleika fyrir notend
print("Hæ, þetta forit umbreyttir tommum í sentimetra eða setimetrum í tommur.")
print("1. Tommur í sentimetra")
print("2. Sentimetra í tommur")
#Foritið fær gildi fyrir svarið
svar = input("Veldu þann möguleika sem þú vilt")
#Ef valið er einn er stærðfræði jafna sem umbreytir tommum í cm og prentar svo út svarið
if svar == "1":
    tommur = float(input("Fjöldi tomma:"))
    cm = tommur * 2.54
    print("Það eru:", cm, "sentimetrar")
#Ef valið er tvo er stærðfræði jafna sem umbreytir sentimetrum í tommur og prentar svo út svarið
elif svar == "2":
    cm = float(input("Fjöldi sentimetra:"))
    tommur = cm / 2.54
    print("Það eru:", tommur, "tommur")
#Ef ekki er valið það sem beðið er um prentast út eftirfarandi græni texti
else:
    print("Þú hefur ekki valið rétt")

#milliliður
afram= input("Viltu halda áfram(j/n)?")
if afram == "j" or afram == "J":
    print("Nú verður haldið áfram")
elif afram == "n" or afram == "N":
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þit var ekki nægilega skýrt, nú verður haldið áfram")

#liður3
#Hér prentar foritið út valmöguleika fyrir notenda
print()
print("Hæ, þetta forit segir þér hvaða árstíð er")
print("1. Janúar")
print("2. Febrúar")
print("3. Mars")
print("4. Apríl")
print("5. Maí")
print("6. Júní")
print("7. Júlí")
print("8. Ágúst")
print("9. September")
print("10. Október")
print("11. Nóvember")
print("12. Desember")
manudur = input("Sláðu inn númer á mánuði")
#Hér skilgreinir foritið hvorri árstíð mánuður tilheyrir fyrir alla mánuðinni og hvaða setningu skal byrta fyrir hvern mánuð
#Fyrir mánuð 12, 1 og 2
if manudur == "12" or manudur == "1" or manudur == "2":
    print("Nú er vetur")
    if manudur == "1" or manudur == "2":
        print("Nú er daginn tekið að lengja")
    elif manudur == "12":
        print("Núna styttist í jólin")
#Fyrir mánuð 3, 4 og 5
elif manudur == "3" or manudur == "4" or manudur == "5":
    print("Nú er vor")
    if manudur == "3":
        print("Nú er daginn tekið að lengja")
    elif manudur == "4" or manudur == "5":
        print("Vorið er komið og grundirnar gróa")
#Fyrir mánuð 6,7 og 8
elif manudur == "6" or manudur == "7" or manudur == "8":
    print("Nú er sumar")
    if manudur == "6" or manudur == "7" or manudur == "8":
        print("Núna er sumarið komið með blóm í haga")
#Fyrir mánuð 9, 10 og 11
elif manudur == "9" or manudur == "10" or manudur == "11":
    print("Nú er haust")
    if manudur == "9" or manudur == "10":
        print("Núna er Haustið gengið í garð")
    elif manudur == "11":
        print("Núna styttist í jólin")
else:
    print("Rangur innsláttur")

#milliliður
afram= input("Viltu halda áfram(j/n)?")
if afram == "j" or afram == "J":
    print("Nú verður haldið áfram")
elif afram == "n" or afram == "N":
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þit var ekki nægilega skýrt, nú verður haldið áfram")

#lidur_4
print()
#Foritið fær gildi fyrir nafn og kyn notend
nafn = input("Hvað heitir þú")
kyn = input("Ertu kk(Karlkyns) eða kvk(Kvenkyns)?")
#Foritið velur rétt kyn eftir kyn notenda
if kyn == "kk" or kyn == "KK" or kyn == "Kk":
    kyn = "Blessaður"
elif kyn == "kvk" or kyn == "KVK" or kyn == "Kvk   ":
    kyn = "Blessuð"
else:
    kyn = "Blessaður eða blessuð ég veit ekki hvors kyns þú ert"
#Hér fær foritið gildi fyrir ýmsar breytur:
tala_1 = int(input("Skrifaður tvær heiltölur, fyrri hér:"))
tala_2 = int(input("Seinni hér:"))
utkoma = tala_2 - tala_1
staerd = "mismunur minni eða meiri"
#Hér er if lengja sem kemst að því hvort mismunur tveggja talna valdar af notenda séu minni eða stærii en 100
if utkoma > 100:
    staerd = "Mismunur talnana er stærri en 100"
elif utkoma < 100:
    staerd = "Mismunur talnana er minni en 100"
elif utkoma == 100:
    staerd = "Mismunur talnana er hundrað"
#If lengja sem segir hvort fyrri eða seinni talan sé stærri
if tala_1 < tala_2:
    tala_1 = "Seinni talan er stærri"
elif tala_1 > tala_2:
    tala_1 = "Fyrri talan er stærri"
else:
    tala_1 = "Tölunar eru jafn stórar"
#Útkomur prentaðar út
print(kyn, nafn)
print(tala_1,"og", staerd)

#milliliður
afram= input("Viltu halda áfram(j/n)?")
if afram == "j" or afram == "J":
    print("Nú verður haldið áfram")
elif afram == "n" or afram == "N":
    print("Nú verður foritnu lokað")
    quit()
else:
    print("Svarið þit var ekki nægilega skýrt, nú verður haldið áfram")

#lidur_5
print()
#Heiltala fengin frá notenda
tala = int(input("sláðu inn heiltölu sem er lægri en 0 eða hærri en 10"))

#Komist að því hvort talan sé lægri en 0 eða hærri en 10 og útkoman prentuð út
if tala > -1 and tala < 11:
    print("þessi tala er ekki lægri en 0 eða hærri en 10")
else:
    print("Vel gert")
print("takk fyrir að prufa foritið mitt")










