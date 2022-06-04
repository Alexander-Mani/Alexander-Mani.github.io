#Alexander_Máni_Einarsson
#03/04/20
#Hengimann


lausn_listi = []
gisk_listi = []
lausn_ord = "halldor"
for x in range(len(lausn_ord)):
    lausn_listi.append(lausn_ord[x])

print("Hengimann")
lif = 5
while lif != 0  or lif < 0:
    print()
    gisk = input("Giskaðu á staf eða orð: ")
    print()
    if len(gisk) >= 2:
        if gisk == lausn_ord:
            print("til hamingju þú vannst")
            lif = 0
            break
        else:
            print("Orðið er ekki rétt, þú misstir eitt líf")
            lif = lif -1
            print()
            print("Líf = ",lif)
    else:
        if gisk not in lausn_listi and gisk not in gisk_listi:
            lif = lif - 1
            print("Þú giskaðir á rangana staf þú átt",lif,"Líf eftir")
        elif gisk in gisk_listi:
            print("Þú hefur þegar giskað á þennan staf")
        elif gisk in lausn_listi:
            print("Rétt hjá þér!")
        gisk_listi.append(gisk)
    vinningur = 0
    if lif != 0:
        print()
        for x in range(len(lausn_listi)):
            if lausn_listi[x] not in gisk_listi:
                print(lausn_listi[x].replace(lausn_listi[x], "_"),end=" ")
                vinningur = vinningur +1
            else:
                print(lausn_listi[x],end=" ")
    print()
    if lif == 0:
        print("Þú hefur því miður tapað")
    elif vinningur == 0:
        lif = 0
        print()
        print("Þú vannst!!!")










