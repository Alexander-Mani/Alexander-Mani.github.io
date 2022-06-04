#Alexander_Máni_Einarsson
#24/09/19
#Skilaverkefni_4
from _ast import arg

on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni 4 <-=-=-=")
    print()
    print("1. Komast að því hvort að innslegin tala sé í 5 sinnum töflunni")
    print("2. Komast að því hvort að innslegið ár sé hlaupár ")
    print("3. Sjá útkomu á insleginni tölu eins og hún sé hrópmerkt(t.d. 3!=3*2*1=6)")
    print("4. Fá réttindan þríhyrnig með sömu hliðarlengd og grunnflöt og innslegin tala")
    print("5. Hætta")
    val = int(input("Veldu möguleika með því að slá inn tölu: "))
    print()

    if val == 1:
        svar = "j"
        #While lykkjan keyrir þar til notandinn svara já
        while svar == "J" or svar == "j":
            tala = int(input("Sláðu inn heiltölu: "))
            tala // 5
            if tala % 5 == 0:
                print("þessi tala er í 5 sinnum töflunni")
            else:
                print("þessi tala er ekki í 5 sinnum töflunni")
            print()
            svar = input("Viltu prufa aðra tölu J/N")

    elif val == 2:
        svar = "j"
        # While lykkjan keyrir þar til notandinn svara já
        while svar == "J" or svar == "j":
            ar = int(input("Sláðu inn ártal: "))
            # Hér er jafna til að athuga hvort innslegin tala sé hlaupár væri hún ár
            if ((ar % 400 == 0) or ((ar % 4 == 0) and (ar % 100 != 0))):
                print("þetta er hlaupár")
            else:
                print("Þetta er ekki hlaupár")
            print()
            svar = input("Viltu prufa aðra tölu J/N")

    elif val == 3:
        tala = int(input("Sláðu inn heiltölu :"))
        marg = 1
        #for lykkja sem reiknar tölu eins og hún sé hrópmerkt
        for x in range(tala, 0, -1):
            marg = marg * x
        print(marg)

    elif val == 4:
        tala = int(input("Sláðu inn heiltölu :"))
        #For lykkja sem teiknar þríhyrniga út frá ranginu tala bæði í grunnflöt og hæð
        for x in range(tala):
            x = x + 1
            print("*" * x)

    elif val == 5:
        print("Nú verður foritinu hætt")
        quit()

    else:
        print("Villa hefur komið upp")
