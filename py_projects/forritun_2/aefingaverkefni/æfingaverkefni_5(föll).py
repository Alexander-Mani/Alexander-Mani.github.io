#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni

import random
def brandari():
    print("Haha api lol XD")

def brandarar(tala):
    if tala == 1:
        print("Jonni á tómata")
    elif tala == 2:
        print("Titanc")
    elif tala ==3:
        print("Halldór Laxness gerði eh að viti")

def kyn(ord=""):
    if ord == "kk":
        print("Þú ert Karlmaður")
    elif ord == "kvk":
        print("Þú ert Kvenmaður")
    else:
        print("Þetta kyn þekkji ég ekki")
    return ord


on = True
while on:
    print()
    print("=-=-=-> Föll 1 <-=-=-=")
    print()
    print("1. Brandari")
    print("2. Brandarar")
    print("3. Kyn")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        #1.	Fall sem nefnist brandari og skrifar út
        # brandara í hvert skipti sem kallað er á það.
        brandari()


    elif val == 2:
        print()
        #2.	Fall sem nefnist brandarar og hefur heiltölu færibreytu 1,2 eða 3.Það eiga svo að
        # koma mismunandi brandarar eftir hvaða tala er valin sem færibreyta.
        nr = int(input("Sláðu inn núme rfrá 1-3 fyrir brandara"))
        print()
        brandarar(nr)

    elif val == 3:
        print()
        #3.	Fall sem tekur inn strengjabreytu (kyn). Biðið notandann að slá inn kyn.
        # Ef slegið er inn kk þá skrifast á skjáinn „þú ert karlmaður“ ef skrifað er kvk
        # þá prentast út „þú ert kvennmaður“ annars skrifast út þetta kyn þekki ég ekki.Hafið
        # aðferðina þannig að ef  engin færibreyta er sett inn í sviga birtist „þetta kyn þekki
        # ég ekki“.
        stafir = input("veldu kyn Sláðu inn kk,kvk")
        kyn(stafir)

    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
