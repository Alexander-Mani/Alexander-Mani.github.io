#Alexander_Máni_Einarsson
#06/11/19
#Skilaverkefni

#Fyrir lið 1
def slettar_tolur():
    talnalisti = []
    for x in range(1001):
        tala = x+1
        if tala & 2 == 0 and  tala != 1 or tala == 2:
            talnalisti.append(tala)
    return talnalisti




on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni <-=-=-=")
    print()
    print("1. Sléttar t-lur")
    print("2. Prímatölur")
    print("3. Tuple Skrá")
    print("4. Dictionary")
    print("5. ")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print(slettar_tolur())

    elif val == 2:
        print()

    elif val == 3:
        print()

    elif val == 4:
        print()

    elif val == 5:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
