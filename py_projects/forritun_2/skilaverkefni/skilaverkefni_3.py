#Alexander_Máni_Einarsson
#17/02/20
#Skilaverkefni_3

import random

#Fyrir lið 1
#a
#Prentar tuples snyrtilega
def prentaTuple(tup):
    for x in range(len(tup)):
        print(tup[x],end=" ")


#b
#Prentar 2 tuples hlið við hlið
def paraRod(tup1, tup2):
    for x in range(len(tup1)):
        print(tup1[x]," og ",tup2[x])

#c
#prentar 2 atriði ír 2 tuples af handahófi hvaða atriði er valið
def paraRandom(tup1, tup2):
    teningur_1 = random.randint(0,5)
    teningur_2 = random.randint(0,5)
    print("Hér er random par")
    print(tup1[teningur_1], " og ", tup2[teningur_2])

#d
def paraRandomStakur(tup1, tup2):
    paralisti_herrar = []
    paralisti_domur = []
    print("Random pör: ")
    for x in range(len(tup1)):
        svar = 0
        #Atriði valið af handahófi úr tuple og sett í lista svo er hent tening þangað til eh kemur
        #upp sem er ekki í listanum svo það sam er ekki valið aftur það er kastað þangað til eh
        #er valið útaf while
        while svar != "ok":
            teningur_1 = random.randint(0, 5)
            if teningur_1 not in paralisti_herrar:
                paralisti_herrar.append(teningur_1)
                svar = "ok"
        #sama gert og hér fyrir ofan nema fyrir anna tuples
        while svar != "ok!":
            teningur_2 = random.randint(0, 5)
            if teningur_2 not in paralisti_domur:
                paralisti_domur.append(teningur_2)
                svar = "ok!"
        #prentað út eitt handhóft par en þetta er keyrt jafn oft og for lykkjan sem keyrir jafn oft
        #og lengd tuplessin
        print(tup1[teningur_1], " og ", tup2[teningur_2])

#e
def finnaNafn(stafur,  tup2):
    nafnalisti = []
    #farið í gegnum hvern einasta staf í hverju einast nafni  í tuplesinu og ef stafurinn kemur einu
    #sinni eða oftar og er í hástaf eða lástaf er honunm bætt í lista sem er nafninu síðan skilað til notenda
    for x in range(len(tup2)):
        if stafur in tup2[x] or stafur.upper() in tup2[x]:
            nafnalisti.append(tup2[x])
    return nafnalisti

#f
def finnaNafnByrjun(stafur,  tup2):
    nafnalisti = []
    # farið í gegnum hvern einasta upphafsstaf í hverju einast nafni  í tuplesinu og ef stafurinn kemur
    # fyrir í hástaf eða lástaf er honunm bætt í lista sem er nafninu síðan skilað til notenda
    for x in range(len(tup2)):
        nafn = tup2[x]
        if stafur in nafn[0] or stafur.upper() in nafn[0]:
            nafnalisti.append(nafn)
    return nafnalisti

#g
def fleiriEn1N(tup1, tup2):
    nafnalisti = []
    #las fyrst að þetta ætii að vera tvö n eða fleiri því er þetta kannski óþarfa flókinn
    #kóði en ég breytti bara nokkrum atriðum til að athuga hvort væri 1 en eða fleiri og nafninu
    #á fallinu
    #En þetta fer í gegnum bæði tuplesin í einu og athugar hvort að það sé n í hverju einast nafni og ef svo er
    #er nafninu bætt í lista, einn lista frá báðum tuplesinum og skilað til notenda
    for x in range(len(tup2)):
        n_teljari_h = 0
        n_teljari_d = 0
        nafn = tup1[x]
        nafn_2 = tup2[x]
        for x in range(len(nafn)):
            if "n" in nafn[x] or "N" in nafn[x]:
                n_teljari_h = n_teljari_h+1
            if n_teljari_h >= 1:
                if nafn not in nafnalisti:
                    nafnalisti.append(nafn)
        for x in range(len(nafn_2)):
            if "n" in nafn_2[x] or "N" in nafn_2[x]:
                n_teljari_d = n_teljari_d+1
            if n_teljari_d >= 1:
                if nafn_2 not in nafnalisti:
                    nafnalisti.append(nafn_2)

    return nafnalisti

#Fyrir lið 2
def finnaSima(dict, persona):
    #Fallið nær í valueið fyrir keyið persona sem ræðst af notenda
    if persona in dict:
        return "Símanúmerið er: ",dict.get(persona)
    #Ef persona er ekki í samræmi við það sem er í dictionarinu er þessum texta skilað
    else:
        return "Þetta nafn er ekki til í skránni"

#Fyrir lið 3
#a
def prentaBekk(dict):
    #prentar value og key listans snyrtilega eitt í hverji línu
    print("Nafn \t Aldur")
    for item in dict.items():
        print(item)

#b
def yfir18(dict):
    print("Þessir einstaklingar eru 18 ára eða eldri")
    print()
    #Ef valueið(aldurinn) er átjan ára eða eldri er tiltekið key prentað tengt við tiltekna valuip
    #for lykkjan fer síðan í gegnum hvert einast item í dictinu og gerir þetta
    for key, value in dict.items():
        if value >= 18:
            print(key)

#c
def finnaMedalaldur(dict):
    summa = 0
    #Tekur valuin(aldurinn) úr dictinu plúsar þeim saman og deilir því
    #með fjöldanum lengd dictsins og skilar til baka námundað
    for value in dict.values():
        summa = summa + value
    medaltal = summa/len(dict)
    return round(medaltal, 2)

#d
def finnaHeildaraldur(dict):
    # Tekur valuin(aldurinn) úr dictinu plúsar þeim saman og skilar til baka námundað
    summa = 0
    for value in dict.values():
        summa = summa + value
    return summa

#e
def finnaStaf(stafur, dict):
    upphaf_staf_dict = {}
    #Athugar hvaða keys í dictinu byrja á stafinum sem notenda valdi
    #Ef einhver keys passa erþeim bætt í nýtt dict meða sama value og í upprunilega dictinu
    for key, value in dict.items():
        if stafur in key[0] or stafur.upper() in key[0]:
            upphaf_staf_dict[key] = value
    #Notað gömul föll til að prenta og finn meðalaldur
    prentaBekk(upphaf_staf_dict)
    print()
    print("Meðalaldur þeirra er: ")
    print(finnaMedalaldur(upphaf_staf_dict))

#Ath kommenatði aðeins hjá föllunum því það útskýrir líka hvernig kallað ætti á þau ef svo þyrfti
#Plús það allt hér fyrir neðan er sami skítur og í fyrrsa búinn að kommennta það nægilega oft og það
#er ekki viðfangsefnið að þessu sinn, takk fyrir mig




on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni 3 <-=-=-=")
    print()
    print("1. Danspörin")
    print("2. Símaskra")
    print("3. Skráning í bekk")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        herrar = ("Siggi","Halldór","Sævar","Alex","Jonni","Bjarni")
        domur = ("Saga","Snæfríður","Rakel","Linda","Katrín","Elma")
        prentaTuple(herrar)
        prentaTuple(domur)

        print()
        paraRod(herrar, domur)

        print()
        paraRandom(herrar, domur)

        print()
        paraRandomStakur(herrar, domur)

        print()
        print("Sláðu inn staf og þú færð lista með öllum nöfnum sem haf þann staf")
        bokstafur = input("Sláðu inn staf: ")
        listi_1 = finnaNafn(bokstafur, herrar)
        listi = listi_1 + finnaNafn(bokstafur, domur)

        print()
        print("Þessi nöfn innihalda bókstafinn", bokstafur,"/",bokstafur.upper(), "í sér: ")
        for x in range(len(listi)):
            print(listi[x])

        print()
        print("Sláðu inn staf og þú færð lista með öllum nöfnum sem hafa þann staf í upphafi")
        bokstafur = input("Sláðu inn staf: ")
        listi_1 = finnaNafnByrjun(bokstafur, herrar)
        listi = listi_1 + finnaNafnByrjun(bokstafur, domur)
        print("Þessi nöfn byrja á  bókstafum", bokstafur, "/", bokstafur.upper(), ": ")
        for x in range(len(listi)):
            print(listi[x])

        print()
        listi = fleiriEn1N(herrar, domur)
        print("Þessi nöfn hafa fleiri en 1 n/N í sér: ")
        for x in range(len(listi)):
            print(listi[x])


    elif val == 2:
        print()
        simaskra = {"Agnes": 12351844, "Alda": 6529133, "Siggi": 2589526, "Elma": 3529885, "Trausti": 8688468, "Daniela": 4728862, "Bára": 5577594, "Jóna": 1278977, "Gylfi": 2876821, "Hannes": 4296645}
        for keys in simaskra.keys():
            print(keys)
        einstaklingur = input("Sláðu nafnið á þeim sem þú villt finna símanr í símaskránni: ")
        print(finnaSima(simaskra, einstaklingur))

    elif val == 3:
        print()
        bekkur = {"Andri":29,"Stefán":16,"Baldur":18,"Ketill":31,"Guðrún":23,"Hallbera":30,"Gunnvör":18,"Búkolla":17,"Gilitrutt":28,"Steinar":18,"Valtýr":35,"Sævar":33,"Einar":20,"Davíð":15,"Golíat":16,}
        svar = 0
        while svar != 6:
            print()
            print("Skráning í bekk")
            print()
            print("1. Bekkjalisti")
            print("2. Allir yfir 18 ára")
            print("3. Meðalaldur")
            print("4. Heildaraldur")
            print("5. Hverjir byrja á staf x")
            print("6. Hætta")
            print()
            svar = int(input("Sláðu inn nr á þeim lið sem þú vilt ræsa"))

            if svar == 1:
                prentaBekk(bekkur)

            elif svar == 2:
                yfir18(bekkur)

            elif svar == 3:
                print()
                print("Meðlatal bekksins er: ",finnaMedalaldur(bekkur))

            elif svar == 4:
                print()
                print("Heildaraldur bekksins er: ", finnaHeildaraldur(bekkur))

            elif svar == 5:
                print()
                staf = input("Sláðu inn staf og forritið byrtir upplýsingar um alla sem byrja á þeim staf")
                print()
                finnaStaf(staf, bekkur)

            elif svar == 6:
                print("Aftur í aðal valmynd...")

            else:
                print("Villa!!!")




    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
