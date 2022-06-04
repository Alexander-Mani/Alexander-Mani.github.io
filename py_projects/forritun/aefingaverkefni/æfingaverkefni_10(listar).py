#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni
import random

on = True
while on:
    print()
    print("=-=-=-> Æfingaverkefni 10 listar <-=-=-=")
    print()
    print("1. Innkaupalisti ")
    print("2. Random tölur ")
    print("3. Fyrsta og síðasta ")
    print("4. Nemendur ")
    print("5. Hætta ")
    val = int(input("Veldu: "))
    if val == 1:
        listi= []
        svar = "j"
        while svar != "J" or svar !="j":
            print()
            k = input("Hverju viltu bæta við á listan: ")
            listi.append(k)
            svar = input("viltu hætta? J/N: ")
            listi.sort()
            print(listi)

    elif val == 2:
        print()
        listi=[]
        sum = 0
        for x in range(15):
            random_tala = random.randint(5, 25)
            sum = random_tala + sum
            listi.append(random_tala)
            listi.sort()
        print("Raðaður listi: ", listi)
        print("Hæsta stakið er: ", max(listi))
        print("Lægsta stakið er: ", min(listi))
        print("Summan er: ",sum)
        print("lengd listans er: ", len(listi))

    elif val == 3:
        print()
        listi = []
        for x in range(20):
            random_tala = random.randint(1, 20)
            print(x)
            listi.append(random_tala)
        nylisti = []
        nylisti.append(listi[0])
        nylisti.append(listi[-1])
        print(listi)
        print(nylisti)

    elif val == 4:
        print()
        sum = 0
        listi=[]
        while sum < 10:
            nafn = input("Skrafaðu nafn: ")
            if nafn in listi:
                print("Mátt ekki slá inn sama nafnið tvisvar")
            else:
                listi.append(nafn)
                sum = sum +1
        print(listi)



    elif val == 5:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")