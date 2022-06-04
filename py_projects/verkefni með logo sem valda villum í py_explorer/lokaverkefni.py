import random

class Spil:
    def __init__(self, tegund, numer):
        self.tegund = tegund
        self.numer = numer

    def __str__(self):
        return "{self.tegund}".format(self=self)+"{self.numer}".format(self=self)

#Þetta fall skilgreinir grunnreglur spilsins
def reglur(s, u):
    if s.tegund  == u.tegund:
        return "ja"
    elif s.numer == u.numer:
        return "ja"
    elif s.numer == 8:
        return "ja"
    else:
        return "nei"

#Þetta fall athugar hvort það sé eh spil í listanum sem getur gert
def tolva(l,u):
    for x in range(len(l)):
        svar = reglur(l[x],u)
        if svar == "ja":
            return "ja"
    return "nei"

#Þetta fall sér um að draga ef ekkert passar
def draga(l):
    ny_spil = []
    for x in range(3):
        spil = spilastokkur[0]
        spilastokkur.remove(spil)
        l.append(spil)
        svar = reglur(spil, uti_spil)
        ny_spil.append(spil)
        if svar == "ja":
            l.remove(spil)
            bunki.append(spil)
            hepni = "Sem smell passar ofan á bunkann!"
            ny_spil.append(hepni)
            return ny_spil
    hepni = "Ekkert af spilunum sem þú drógst passa ofan á bunkann"
    ny_spil.append(hepni)
    ny_spil.append(":(")
    return ny_spil

def attu_breyta(s):
    if svar == 1:
        spil = Spil("\033[1;31;40m \u2665","8")
    elif svar == 2:
        spil = Spil("\033[1;37;40m \u2660","8")
    elif svar == 3:
        spil = Spil("\033[1;31;40m \u2666","8")
    elif svar == 4:
        spil = Spil("\033[1;37;40m \u2663","8")
    return spil




#Þessi lykkja býr til spilastokk gefur honum lit, logo og nr/nöfn og býr til spil með Spil klassanum
spilastokkur = []
a = ""
b = ""
for x in range(4):
    x = x+1
    if x == 1:
        a = "\033[1;31;40m \u2665"
    elif x == 2:
        a = "\033[1;37;40m \u2660"
    elif x == 3:
        a = "\033[1;31;40m \u2666"
    elif x == 4:
        a = "\033[1;37;40m \u2663"
    for y in range(13):
        y = y+1
        if y == 1:
            b = "Ás"
        elif y == 11:
            b = "Gosi"
        elif y == 12:
            b = "Drottning"
        elif y == 13:
            b = "Kóngur"
        else:
            b = y
        spilid = Spil(a, b)
        spilastokkur.append(spilid)
#Stokka spilastokkinn
random.shuffle(spilastokkur)

#Listarnir sem notaðir eru í spilinu
hendi_tol = []
hendi = []
bunki = []

#Gefið spil
for x in range(5):
    spil_1 = spilastokkur[x]
    spilastokkur.remove(spil_1)
    hendi_tol.append(spil_1)

    spil_2 = spilastokkur[x]
    spilastokkur.remove(spil_2)
    hendi.append(spil_2)

#Efsta spil úr sðilastokki lagt við hlið bunkans
spil = spilastokkur[0]
spilastokkur.remove(spil)
bunki.append(spil)

staða = ""
ummferd = 0
while staða != "leik lokið":
    ummferd = ummferd +1
    print("\033[0;37;40m")
    uti_spil = bunki[-1]
    print("Ummferð nr", ummferd)
    print("Tölvan er með: ",len(hendi_tol)," Spil á hendi")
    print()
    print("Eftirfarandi spil er úti: >", uti_spil, "\033[0;37;40m<")
    print()
    print("Þetta eru spilin þín (",len(hendi),") : ")
    for x in range(len(hendi)):
        if x+1 != len(hendi):
            print(hendi[x], end=" \033[0;37;40m // ")
        else:
            print(hendi[x])
    #Notum fall til að athuga hvort notandi geti gert
    svar = tolva(hendi,uti_spil)
    print("\033[0;37;40m")
    if svar == "ja":
        print()
        print("Þú átt leik")
        print("Þú getur slegið inn 0 til að sjá sætisröð spila")
        adgerd = int(input("Sláðu inn Sætisnr á því spili sem þú vilt leika:"))
        print()
        # Sætisröð
        if adgerd == 0:
            print()
            uti_spil = bunki[-1]
            print("Eftirfarandi spil er úti: >", uti_spil, "\033[0;37;40m<")
            print()
            print("Sætisröð")
            for x in range(len(hendi)):
                print(x + 1, ". ", hendi[x])
            adgerd = int(input("Sláðu inn Sætisnr á því spili sem þú vilt leika:"))
            print()
        if adgerd != 0:
            spil = hendi[adgerd - 1]
            svar = reglur(spil, uti_spil)
            # Leika spili
            if svar == "ja":
                spil = hendi[adgerd - 1]
                hendi.remove(spil)
                # ef spil er átta
                if spil.numer == 8:
                    print("Hvaða tegund skal áttan vera?")
                    print("1. \033[1;31;40m \u2665 Hjarta")
                    print("2. \033[1;37;40m \u2660 Spaði")
                    print("3. \033[1;31;40m \u2666 Tígull")
                    print("4. \033[1;37;40m \u2663 Lauf")
                    svar = int(input("Sláðu inn Nr. á þeirri tegund sem þér líkar: "))
                    print()
                    spil = attu_breyta(svar)
                    bunki.append(spil)
                    print("Þú spilaðir eftirfarandi spili: ", spil)
                else:
                    bunki.append(spil)
                    print("Þú spilaðir eftirfarandi spili: ", spil)
            elif svar == "nei":
                print("Þú mátt ekki leika þennan leik vinsamlegast reyndu aftur")
                continue
            else:
                break
    #Draga fyrir notenda
    else:
        print("Þú getur ekkert gert")
        input("Skrifaði D til þess að draga")
        dragningur = draga(hendi)
        print("Þú drógst")
        for x in range(len(dragningur)):
            spil = dragningur[x]
            print(spil)
        print()
        uti_spil = bunki[-1]
        print("Eftirfarandi spil er úti: >", uti_spil, "\033[0;37;40m<")
        print()
        if len(dragningur) > 4:
                print("þú neyðist til þess að segja PASS")
        input("viltu halda áfram? (Y/N)")
        print()

    #Ólsen fyrir notenda
    if len(hendi) == 0:
        print("Hvað vilt þú gera: ")
        print("1 Segja ÓLSEN ÓLSEN!")
        print("2 Sleppa því að segja ÓLSEN ÓLSEN")
        svar = int(input("Sláðu sætistöluna á þeim möguleika sem þú vilt: "))
        print()
        if svar == 1:
            print("Þú þarft ekki að draga nein spil!")
            print("...")
            print("Því þú hefur unnið til hamingju með sigurinn!!!")
            quit()
        elif svar == 2:
            print("obba boj þú sagðir ekki ÓLSEN ÓLSEN og þarft að draga 3 spil!")
            for x in range(3):
                spil = spilastokkur[x]
                spilastokkur.remove(spil)
                hendi.append(spil)
    #ÓLSEN ÓLSEN fyrir notenda
    elif len(hendi) == 1:
        print("Hvað vilt þú gera: ")
        print("1 Segja ÓLSEN!")
        print("2 Sleppa því að segja ÓLSEN")
        svar = int(input("Sláðu sætistöluna á þeim möguleika sem þú vilt: "))
        print()
        if svar == 1:
            print("Þú þarft ekki að draga nein spil!")
            print()
        elif svar == 2:
            print("obba boj þú sagðir ekki ÓLSEN og þarft að drag 3 spil!")
            for x in range(3):
                spil = spilastokkur[x]
                spilastokkur.remove(spil)
                hendi.append(spil)
    print("\033[0;37;40m")
    uti_spil = bunki[-1]

    #Tölvan gerir
    print("Tölvan á leik")
    #Ákvað að geyma þetta hérna fyrir þig, til þess að sjá spilin hjá tölvunni
    #for x in range(len(hendi_tol)):
    #    print(hendi_tol[x])
    print()
    for x in range(len(hendi_tol)):
        svar = reglur(hendi_tol[x],uti_spil)
        if svar == "ja":
            spil = hendi_tol[x]
            hendi_tol.remove(spil)
            if len(hendi_tol) == 0:
                svar = random.randint(1, 4)
                if svar == 1:
                    print("obba boj Tölvan sagðir ekki ÓLSEN ÓLSEN og þarf að draga 3 spil!")
                    for x in range(3):
                        spil = spilastokkur[x]
                        spilastokkur.remove(spil)
                        hendi_tol.append(spil)
                    print("Heimska Tölva")
                    print()
                    break
                else:
                    print("Tölvan segr:")
                    print("Bíbb ÓLSEN Búbb ÓLSEN ")
                    input("Tölvan hefur sigrað!!! Reyndu betur næst :)")
                    print()
                    quit()
            elif len(hendi_tol) == 1:
                svar = random.randint(1, 4)
                if svar == 1:
                    print("obba boj Tölvan sagði ekki ÓLSEN og þarf að draga þrjú spil !")
                    for x in range(3):
                        spil = spilastokkur[x]
                        spilastokkur.remove(spil)
                        hendi_tol.append(spil)
                    print("Heimska Tölva")
                    print()
                    break
                else:
                    print("Tölvan segr:")
                    print("Bíbb Búbb ÓLSEN Búbb")
                    input("Tölvan á aðeins eitt spil eftir!!! viltu halda áfram? (Y/N)")

                    print()
                    break
                # ef spil er átta
            elif spil.numer == 8:
                svar = random.randint(1,4)
                spil = attu_breyta(svar)
                bunki.append(spil)
                print("Tölvan breytti í ", spil)
                print()
                break
            else:
                bunki.append(spil)
                print("Tölvan spilaði eftirfarandi spili: ", spil)
                break

    if svar == "nei":
        dregningur = draga(hendi_tol)
        if len(dregningur) < 5:
            print("Tölvan dróg",len(dregningur)-1,"Spil")
            print("Og spilaði spilinu: ",dregningur[-2])
        else:
            print("Tölvan dróg þrjú spil en engin pössuðu á borðið")
            print("Tölvan sagði því PASS")

    #Snúa við spilastokki
    if len(spilastokkur) == 0:
        lengd = len(bunki)
        for x in range(lengd):
            spil = bunki[0]
            bunki.remove(spil)
            spilastokkur.append(spil)
        spil = spilastokkur[-1]
        spilastokkur.remove(spil)
        bunki.append(spil)