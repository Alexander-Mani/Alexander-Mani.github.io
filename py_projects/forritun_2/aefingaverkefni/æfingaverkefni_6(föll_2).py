#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni

import math

def rummal_kulu(r):
    utkoma = ((4 * 3.14)*(r*r*r))/3
    return utkoma

def rummal_kass(l, b, h):
    utkoma = (l*b*h)
    return utkoma

def rummal_thrihyrnings(b, h):
    utkoma = (b*h)/2
    return utkoma

on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni <-=-=-=")
    print()
    print("1. Rúmmál kúlu")
    print("2. Rúmmál kassa")
    print("3. Rúmmál þríhyrnings")
    print("4. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print("Hér finnur forritið rúmmál kúlu")
        radius = int(input("Sláðu inn radíus"))
        print("Rúmmál kúlunar er",rummal_kulu(radius),"cm í þriðja")

    elif val == 2:
        print()
        print("Hér finnur forritið rúmmál fyrir þrjá kassa")
        kassalisti = []
        for x in range(len(kassalisti)):
            lengd = int(input("Sláðu inn lengd kassans: "))
            breidd = int(input("Sláðu inn breidd kassans: "))
            haed = int(input("Sláðu inn hæð kassans: "))
            kassalisti.append(rummal_kass(lengd,breidd,haed))
            print("Rúmmál kassa",x+1," er", rummal_kass(lengd,breidd,haed), "cm í þriðja")
        medaltal = sum(kassalisti)/len(kassalisti)
        print("Meðaltalið er",medaltal)


    elif val == 3:
        print()
        print("Hér finnur forritið rúmmál þríhyrnings")
        lengd = int(input("Sláðu inn lengdina: "))
        breidd = int(input("Sláðu inn breiddina: "))
        print("Rúmmál þríhyrningsins er", rummal_thrihyrnings(lengd, breidd), "cm í þriðja")

    elif val == 4:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
