#Alexander_Máni_Einarsson
#03/10/19
#æfingaverkefni_8

import random
on = True
while on:
    print()
    print("1. Teningakast")
    print("2. Yatsi kast")
    print("3. Finna oddatölur")
    print("4. Break og TrueFalse")
    print("5. Hætta")
    val = int(input("Veldu eh: "))

    if val == 1:
        random_tala = random.randint(1,6)
        print(random_tala)
    elif val == 2:
        for x in range(1, 6):
            tala = random.randint(1,6)
            print("Teningur",x,"er: ", tala)
    elif val == 3:
        summa = 0
        oddasumma = 0
        for x in range(1,26):
            tala = random.randint(1,26)
            summa = summa + tala
            if tala % 2 != 0:
                print("Hey ég fann oddatölu: ", tala)
                oddasumma = oddasumma + tala
            else:
                print(tala)
        print()
        print(summa)
        print(oddasumma)
    elif val == 4:
        fann_99 =False
        for x in range(250):
            random_tala = random.randint(25,115)
            print(random_tala)
            if random_tala == 73:
                print("Stopp")
                break
            if random_tala == 99:
                fann_99 =True
            print(random_tala)
        if fann_99 ==True:
            print("Tala 99 kom upp")


    elif val == 5:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")

