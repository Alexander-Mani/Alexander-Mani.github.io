#Alexander_Máni_Einarsson
#03/10/19
#æfingaverkefni_7b

on = True
while on:
    print()
    print("1. Tölur frá 1-5")
    print("2. Jafnar tölur")
    print("3. Milli 30-40")
    print("4. Sex dálkar")
    print("5. prenta A")
    print("6. Hætta")
    val = int(input("Veldu raðtöluna á því sem þú vilt velja"))
    if val == 1:
        print()
        for tala in range(1,6):
            print(tala)

    elif val == 2:
        print()
        for tala in range(1, 6):
            tala = tala * 2
            print(tala)

    elif val == 3:
        print()
        for tala in range(30, 41):
            print(tala)

    elif val == 4:
        print()
        for tala in range(10,16):
            print(tala, end=" ")
        print("\n")
        for tala in range(16,22):
            print(tala, end=" ")
        print("\n")
        for tala in range(22,28):
            print(tala, end=" ")
        print("\n")
        for tala in range(28,34):
            print(tala, end=" ")

    elif val == 5:
        for x in "A":
            print(x)
            print(x,x)
            print(x, x, x,)
            print(x, x, x, x)
            print(x, x, x, x, x)


    elif val == 6:
        print()
        print("Nú verður foritinu lokað")
        quit()
    else:
        print("Villa kom upp!")