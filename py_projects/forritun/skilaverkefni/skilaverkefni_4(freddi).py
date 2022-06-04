#Alexander_Máni_Einarsson
#24/09/19
#Skilaverkefni_4(freddi)

import turtle
on = True
while on:
    print()
    print("1. 20 línur í runu")
    print("2. 10 stækkandi línur ")
    print("3. 10 stækkandi hringir")
    print("4. 15 stækkandi hringir með sama miðpunkt")
    print("5. Átthirningur")
    print("6. Hætta")
    val = int(input("Veldu: "))

#Dæmi 1
    if val == 1:
        fred = turtle
        fred.reset()
        fred.width(5)
        fred.color("red")
        fred.shape("turtle")
        for i in range(20):
            fred.forward(10)
            fred.up()
            fred.backward(10)
            fred.right(90)
            fred.forward(10)
            fred.left(90)
            fred.down()

#Dæmi 2
    elif val == 2:
        fred = turtle
        fred.reset()
        fred.width(5)
        fred.color("red")
        fred.shape("turtle")
        for i in range(10):
            fred.forward(i*10)
            fred.up()
            fred.backward(i*10)
            fred.right(90)
            fred.forward(10)
            fred.left(90)
            fred.down()

#Dæmi 3
    elif val == 3:
        fred = turtle
        fred.reset()
        fred.color("blue")
        fred.shape("turtle")
        for i in range(10):
            fred.circle(i*10)
    
#Dæmi 4
    elif val == 4:
        fred = turtle
        fred.reset()
        fred.color("blue")
        fred.shape("turtle")
        for i in range(15):
            fred.circle(i*10)
            fred.right(90)
            fred.up()
            fred.forward(10)
            fred.left(90)
            fred.down()

#Dæmi 5
    elif val == 5:
        fred = turtle
        fred.reset()
        fred.color("orange")
        fred.shape("turtle")
        fred.width(3)
        #for slaufa sem segir að skipanir á eftir þessari skipun keyra 8 sinnum með "range(8)"
        for i in range(8):
            #Fara eigi 30 áfram
            fred.forward(30)
            #Fara eigi 45° til vinstri
            fred.left(45)
            #Þetta býr til form með átta hornum(Átthyrning)

    elif val == 6:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")

