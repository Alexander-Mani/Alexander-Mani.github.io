
from os import listdir
from os.path import isfile, join
import os



on = True
while  on == True:
    for x in range(20):
        print()
    print("            VERKEFNIN")
    print("               MÍN   ")
    print("*********************************")
    print()
    print("Sláðu inn '1' fyrir: ",listdir()[0])
    print("Sláðu inn '2' fyrir: ",listdir()[1])
    print("sláðu inn '3' til að hætta: ")
    print("*********************************")
    val = input("           veldu möppu: ")
    for x in range(20):
        print()

    if val == "1":
        val =listdir()[0]

    elif val =="2":
        val=listdir()[1]
    elif val == "3":
        break

    stadsetning = val

    for x in range(len(listdir(stadsetning))):
        print("Sláðu inn '",x+1,"' fyrir: ",listdir(stadsetning)[x])
    print("sláðu inn '", len(listdir(stadsetning)) + 1, "' til að fara til baka")
    val_2 = input("veldu möppu: ")

    if val_2 == "1":
        val_2 =listdir(stadsetning)[0]

    elif val_2 =="2":
        val_2=listdir(stadsetning)[1]

    elif val_2 == "3":
        continue

    stadsetning = val+"/"+val_2

    for x in range(len(listdir(stadsetning))):
        print("Sláðu inn '",x+1,"' fyrir: ",listdir(stadsetning)[x])
    print("sláðu inn '",len(listdir(stadsetning))+1,"' til að fara til baka")
    val_3 = input("veldu verkefni: ")
    til_baka = str(len(listdir(stadsetning)) + 1)
    if val_3 == til_baka:
        continue

    print(len(listdir(stadsetning))+1)
    for x in range(len(listdir(stadsetning))):
        verkefni_nr = str(x+1)
        if val_3 == verkefni_nr:
            print("þú hefur valið",listdir(stadsetning)[x])
            verkefni = val+"/"+val_2+"/"+listdir(stadsetning)[x]


    print(verkefni)

    os.remove("python_preview.txt")
    os.remove("project_file.py")
    with open(verkefni, "r", encoding='utf-8') as py_file, open("python_preview.txt", "a") as txt_file:
        for line in py_file:
            txt_file.write(line)
    with open(verkefni, "r") as py_file, open("project_file.py", "a") as clone_file:
        for line in py_file:
            clone_file.write(line)

    print("Ýttu á ' 1 ' til að sjá kóðan og svo sjá forritið keyrt")
    print("Ýttu á ' 2 ' til að sjá kóðan")
    print("Ýttu á ' 3 ' til að sjá forritið keyrt")
    print("Ýttu á ' 4 ' til að fara til baka")
    print("Ath sum af æfingaverkefnunum eru mjög frumstæð og getur ef þú festist ekki hika við að refresha")
    print("Mælt er með að prenta út kóðan fyrst og svo keyra í æfingaverkefnum svo ávalt sé hægt að finna úrlausn")
    val_4 = input("veldu möguleika: ")
    print()
    if val_4 == "1":
        print("------------------ Hér er kóðinn prentaður út beint ------------------")

        with open("python_preview.txt", "r") as py_file:
            for x in py_file:
                print(x)

        print("----------------------------------------------------------------------")

        tilbuinn = input("Nú keyrist kóðinn venjulega ertu tilbúin/n  (Ýttu á hvaða takka sem er til að halda áfram)")
        import project_file
    elif val_4 == "2":
        print("------------------ Hér er kóðinn prentaður út beint ------------------")

        with open("python_preview.txt", "r") as py_file:
            for x in py_file:
                print(x)

        print("----------------------------------------------------------------------")
    elif val_4 == "3":
        tilbuinn = input("Nú keyrist kóðinn venjulega ertu tilbúin/n  (Ýttu á hvaða takka sem er til að halda áfram)")
        print("Annars getur þú skrifað nei til að fara til baka")
        if tilbuinn =="nei" or tilbuinn =="Nei" or tilbuinn =="n" or tilbuinn =="N" or tilbuinn =="No" or tilbuinn =="no":
            continue
        import project_file
    elif val_4 == "4":
        continue
    else:
        print("villa hefur komið upp :(")
        input("ýttu á hvaða takka sem er til að enduræsa forritið")
        continue










