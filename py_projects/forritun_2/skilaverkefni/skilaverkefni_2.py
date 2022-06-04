#Alexander_Máni_Einarsson
#03/02/20
#Skilaverkefni_2

import random

#allt sem byrjar á def(stutt fyrir defintion) eru föll
#það er hægt að kalla á föll með því að skrifa inn nafn fallsins(guli textinn)
#og setja síðan inn viðeigandi breytu fyrir stuðulinn inn í sviganum aftan við nafnið

#Fyrir lið 1
def farenh_i_celsius(f):
    #Formúla fyrir celsius(c) út frá farenheit(f)
    c = (f -32)/1.8
    #Skilar svarinu á formúlunni námundað upp á tvo aukastafi
    return (round(c,2))
def celsius_i_farenheit(c):
    # Formúla fyrir farenheit(f) út frá celsius(c)
    f = c *1.8 +32
    # Skilar svarinu á formúlunnin námundað upp á tvo aukastafi
    return (round(f,2))

#Fyrir lið 2
def hversuHratt(h):
    #Ef h(hraði er minni er 95 prentast
    if h < 95:
        print("Ókílídókílí")
    #Annars ef h(hraði er hærri eða jafnt og 95 gerist eftirfarandi
    elif h >= 95:
        #Refsistig er búið til sem er eitt refsistig fyrir hverja fimm heila viðbætta yfir 90
        refsistig = (h-90)//5
        #Ef refsistig eru jafnt og eða meira en 12 prentast eftirfarandi
        if refsistig >= 12:
            print("Þú missir ökuréttindið!!!")
        #Ef refsistig eru minni en tólf prentast:
        else:
            print("Þú ert með",refsistig,"refsistig!!!")
    #Ef ef-lykkjan tekur ekki við sér prentast þetta út(vonandi)
    else:
        print("þú hefur ekki slegið inn viðeigandi hraða")

#Fyrir lið 3
def reiknaVeldi(tala, veldi):
    #Þar sem veldið á að geta tekið við float(aukastöfum) í tölu
    #Þarf fyrst að draga heilutölu frá hálftölu
    #Hér er veldið ánn kommu
    heil_veldi = veldi//1
    heil_veldi = int(heil_veldi)
    #Hér er einungins kommu partur veldisins
    half_veldi = veldi % 1
    #Heild verður notað til að geyma svar/summu tölunar í veldinu(veldi)
    #Það þarf að vera 1 svo að það sé hlutlaust því fyrsta sem það þarf að gera er að margfalda
    heild = 1
    #Við gerðina á þessu verkefni kunni ég ekki að nota pow og ég fýla þessa lykkju frekar mikið
    #Svo þetta er lykkja fyrir veldi
    #Talan sem sagt margfaldast með útkomonni sinni og sjálfri sér(Sem er skilgreiningin á veldi)
    for x in range(heil_veldi):
        heild = heild *tala
    #Hér ef partur af veldinu var kommustafur bætum við því þar sem for lykkja getur bara keyrt
    #í heil skipti þ.a.s. getur ekki keyrt hálfum sinnum og það er minni en einn svo því þarf bara
    #að bæta við einu sinni og ef enginn kommu tala er verður viðbætan 0 og ekkert breytist
    heild = heild + (tala*half_veldi)
    # Skilar svarinu á formúlunni
    return round(heild, 4)

#Fyrir lið 4
def reiknaBMI(thyngd,haed):
    #Formúlan fyrir BMI stuðulinn
    bmi = thyngd/(haed*haed)
    bmi = round(bmi, 2)
    #Ef-lykkja fyrir skilgreiningar bmi af þyngdarflokkum
    if bmi <= 18.5:
        print("einstaklingur er Of létt/ur")
    elif bmi > 18.5 and bmi < 25:
        print("einstaklingur er Kjörþyngd")
    elif bmi >= 25 and bmi < 30:
        print("einstaklingur er Yfirþyngd")
    elif bmi >=30:
        print("einstaklingur er Ofþyngd")
    # Skilar svarinu á formúlunni
    return bmi

#Fyrir lið 5
def gallon_i_litra(g):
    #formúla fyrir lítra(l) útfrá gallons(g)
    l = g/3.785
    # Skilar svarinu á formúlunni
    return l

def litrar_i_gallon(l):
    # formúla fyrir gallons(g) útfrá lítra(l)
    g = l * 3.785
    # Skilar svarinu á formúlunni
    return g

#Fyrir lið 6
def heilsa(n):
    #n er nafn finnur hvort son er í nafni og prentar eftirfarandi með nafni í endan (+ n)
    if "son" in n:
        return "Sæll og blessaður " + n
    # n er nafn finnur hvort dóttir er í nafni og prentar eftirfarandi með nafni í endan (+ n)
    elif "dóttir" in n:
        return "Sæl og blessuð " + n
    else:
        print("Þú ert ekki með rétt nafn fyrir forritið")

#Fyrir lið 7
def kasta(hveoft):
    #Býr til lista
    teningalisti = []
    #Kastar teningum jafn oft og notandi valdi
    for x in range(hveoft):
        teningur = random.randint(1,6)
        teningalisti.append(teningur)
    summan = sum(teningalisti)
    # Skilar svarinu á summunni
    return summan

#Fyrir lið 8
def eins(ellefu, tolf, threttan):
    print()
    fjordi_listi = []
    #For lykkja sem athugar hvort eitthvað af tölum inn í listanum sem kom fyrir
    #ellefu er inn í eitthvað af hinum listunum og ef svo er
    #þá bætir það tölunni í fjordalistann ef talan er nú þegar ekki þar
    for x in range(len(ellefu)):
        if ellefu[x] in tolf and ellefu[x] in threttan and ellefu[x] not in fjordi_listi:
            fjordi_listi.append(ellefu[x])
    #Skilar fjórða listanum
    return fjordi_listi






on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni 2 <-=-=-=")
    print()
    print("1. Celsíus Farenheit")
    print("2. Hraðatakmörk")
    print("3. Veldisreikningur")
    print("4. Reikna BMI")
    print("5. Lítrar eða gallon")
    print("6. Kveðja")
    print("7. Teningakast")
    print("8. Listar")
    print("9. Hætta")
    val = int(input("Veldu: "))

    if val == 1:
        print()
        svar = 0
        while svar != 3:
            print()
            print("1. Fahrenheit í Celsius")
            print("2. Celsius í  Fahrenheit")
            print("3. Hætta")
            svar = int(input("Sláðu inn töluna hjá því verkefæri sem þú villt nota"))
            if svar == 1:
                print()
                fahrenheit = int(input("Sláðu inn hitastigið í farhenheit"))
                print(farenh_i_celsius(fahrenheit))

            elif svar ==2:
                print()
                #Býr til breytu og prenta fallið sem er hér fyrir neðan
                celsius = int(input("Sláðu inn hitastigið í celsius"))
                print(celsius_i_farenheit(celsius))

            else:
                print("Villa hefur komið upp")

    elif val == 2:
        print()
        print("Hraðaforritið hér prentar út stöðu þína gagnvart lögunum  á eftirfarandi veg")
        #Býr til breytu setur inn í fallið og kallar á það
        hradi = int(input("Sláðu inn aksturhraðan þinn"))
        hversuHratt(hradi)

    elif val == 3:
        print()
        print("Forritið setur tölu í veldi")
        nr = float(input("Sláðu inn tölu"))
        # Býr til breytu og prentar fallið sem er hér fyrir neðan
        veldisvisir = float(input("Sláðu inn veldið"))
        print("Svarið eru: ",reiknaVeldi(nr,veldisvisir))

    elif val == 4:
        print()
        print("Sláðu inn hæð og þyngd og forritið segir þér stöðu þín samkæmt BMI kvarðanum")
        # Býr til breytu setur inn í fallið og kallar á það
        kg = float(input("Sláðu inn þyngd þína í kg"))
        m = float(input("Sláðu inn hæð þína í m"))
        print(reiknaBMI(kg, m))

        print()
        print("Sláðu nú inn þyngd og hæð fimm einstaklinga og finnum meðaltal þeirra")
        bmilisti= []
        #meðaltal
        # #Býr til breytu setur inn í fallið og kallar á það
        for x in range(5):
            print()
            kg = float(input("Sláðu inn þyngd í kg"))
            m = float(input("Sláðu inn hæð í m"))
            bmilisti.append(reiknaBMI(kg, m))
        medaltal = sum(bmilisti)//len(bmilisti)
        print()
        print("Meðalatalið er :", medaltal)

    elif val == 5:
        print()
        svar = 0
        #valmynd
        while svar != 3:
            print()
            print("1. Gallon í Lítra")
            print("2. Gallon í  Gallon")
            print("3. Hætta")
            svar = int(input("Sláðu inn töluna hjá því verkefæri sem þú villt nota"))
            if svar == 1:
                print()
                # Býr til breytu og prenta fallið sem er hér fyrir neðan
                gallon = float(input("Sláðu inn rúmmálið í Gallonum"))
                print(gallon_i_litra(gallon))

            elif svar == 2:
                print()
                # Býr til breytu og prenta fallið sem er hér fyrir neðan
                litrar = float(input("Sláðu inn rúmmálið í Lítrum"))
                print(litrar_i_gallon(litrar))
            else:
                print("Villa hefur komið upp")

    elif val == 6:
        print()
        # Býr til breytu og prenta fallið sem er hér fyrir neðan
        nafn = input("Sláðu inn fullt nafn: ")
        print(heilsa(nafn))

    elif val == 7:
        print()
        # Býr til breytu og prenta fallið sem er hér fyrir neðan
        kost = int(input("Sláðu inn hve oft þú villt kasta tening: "))
        print("Summa kastanna er :",kasta(kost))

    elif val == 8:
        print()
        #Býr til 3 lista
        talnalisti_listi_1 = []
        talnalisti_listi_2 = []
        talnalisti_listi_3 = []
        #Setur tíu random tölur inn í alla listana
        for x in range(10):
            rando_tala_1 = random.randint(1,10)
            talnalisti_listi_1.append(rando_tala_1)
            rando_tala_2 = random.randint(1,10)
            talnalisti_listi_2.append(rando_tala_2)
            rando_tala_3 = random.randint(1,10)
            talnalisti_listi_3.append(rando_tala_3)
        print("Forritið finnur út hvaða tölur í listunum eru eins hverju sinni")
        print("Listanir að þessu sinni eru")
        print("listi 1: \t",talnalisti_listi_1)
        print("listi 2: \t",talnalisti_listi_2)
        print("listi 3: \t",talnalisti_listi_3)
        print()
        print("þessar tölur/tala  eru/er eins í öllum listum: ",end="")
        #Setur listana inn í fallið og prentar það snyrtilega út með lykkju
        for x in range(len(eins(talnalisti_listi_1, talnalisti_listi_2, talnalisti_listi_3))):
            print(eins(talnalisti_listi_1, talnalisti_listi_2, talnalisti_listi_3)[x], end="")
        print()


    elif val == 9:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
