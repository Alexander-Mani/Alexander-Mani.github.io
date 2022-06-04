#Alexander_Máni_Einarsson
#13/02/20
#Skilaverkefni

#Fyrir lið 1 & 2
def bua_til_dict():
    lita_dict = {1 :"gulur",2:"rauður",3:"grænn",4:"blár",5 :"svartur",6:"hvítur",7 :"fjólublár",8:"brúnn",9 :"bleikur",10:"appelsínugulru"}
    return lita_dict

#Fyrir lið 3
def eyda_lit_dict(nr,dict):
    dict.pop(nr)
    return dict

#Fyrir lið 4
def prent_lit_dict(nr, dict):
    dict = dict.get(nr)
    return dict

#Fyrir lið 5
def afrit_af_dict(dict):
    afrit = dict.copy()
    dict.clear()
    return "Afritið: ",afrit, "Upprunulega orðabókin: ",dict


#Fyrir lið 6
def breytur_dict(dict):
    a= dict.items()
    b= dict.keys()
    c= dict.values()
    print("Items gerir svona: ", a)
    print( "Keys gerir svona: ", b)
    print( "Values gerir svona: ", c)
    print("Clear gerir svona: ", dict.clear())

#Fyrir lið 7
def bua_nafna_dict(nr, nafn):
    nafna_dict={}
    for x in range(len(nr)):
        nafna_dict[nr[x]]= nafn[x]
    return nafna_dict


on = True
while on:
    print()
    print("=-=-=-> Skilaverkefni <-=-=-=")
    print()
    print("1. Búa til dictionary")
    print("2. Prenta dictionary")
    print("3. Eyða lit")
    print("4. Prenta ákveðin lit")
    print("5. Gera afrit af dict – eyða dict og prenta síðan bæði")
    print("6. Sýna notkun fallanna")
    print("7. Gerðu fall sem býr til nýtt dictionary með tölum sem lykli/key og nöfnum sem gildi/value.")
    print("8. Hætta")
    val = int(input("Veldu: "))
    if val == 1:
        print()
        print(bua_til_dict())

    elif val == 2:
        print()
        for x in bua_til_dict():
            print(x,bua_til_dict()[x])

    elif val == 3:
        print()
        for x in bua_til_dict():
            print(x,bua_til_dict()[x])
        print()
        lit = int(input("Veldu númerið á þeim lit sem þú vilt eyða:"))
        eyda_lit_dict(lit,bua_til_dict())
        for x in eyda_lit_dict(lit,bua_til_dict()):
            print(x,eyda_lit_dict(lit,bua_til_dict())[x])
        #Skák og mát

    elif val == 4:
        print()
        for x in bua_til_dict():
            print(x,bua_til_dict()[x])
        print()
        tala = int(input("Veldu númerið á þeim lit sem þú vilt prenta:"))
        print(prent_lit_dict(tala,bua_til_dict()))



    elif val == 5:
        print()
        print(afrit_af_dict(bua_til_dict()))

    elif val == 6:
        print()
        print(breytur_dict(bua_til_dict()))

    elif val == 7:
        print()
        fjoldi = int(input("Sláðu inn fjölda nafna"))
        nafnalisti =[]
        talnalisti =[]
        for x in range(fjoldi):
            numer = x+1
            nafn = input("Sláðu inn nafn: ")
            talnalisti.append(numer)
            nafnalisti.append(nafn)
        print(bua_nafna_dict(talnalisti,nafnalisti))


    elif val == 8:
        print()
        print("Nú verður foritinu hætt")
        quit()
    else:
        print("Villa hefur komið upp")
