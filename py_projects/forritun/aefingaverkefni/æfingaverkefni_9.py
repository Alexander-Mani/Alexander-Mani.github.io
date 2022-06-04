#Alexander Máni Einarsson
#24/09/19
#Skilaverkefni_9

on = True
while on:
    print()
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    val = int(input("Veldu: "))
    if val == 1:
        nyr = ""
        nafn = "Anna Marín Jónsdóttir"
        for x in nafn:
            if x == "n":
                nyr = nyr + "*"
            else:
                nyr = nyr + x
        print(nyr)
        ""
    elif val == 2:
        ""
    elif val == 3:
        ""
    elif val == 4:
        ""
    elif val == 5:
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")


