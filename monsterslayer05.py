import sys
import random
import time
import os
s = 0
pontok = 0

nev = input("ADD MEG NEVED NEMES HARCOS")

while True:
    s = 0
    shp = random.randint(20,50)
    sdm = random.randint(1,10)

    print("karakterek: 1. harcos, 2. vadasz,")

    valasztas=int(input("adja meg választott karaktere szamat? "))
     
    hhp = 10
    hdm = 15

    vhp = 15
    vdm = 10

    mhp = 0
    mdm = 0
    ms = 1

    if valasztas==1:
        print("VALSZTOTT KARAKTERED HARCOS")
        mhp = hhp
        mdm = hdm
        print(f"Élet={mhp}")
        print(f"SEBZES={mdm}")
        
    if valasztas==2:
        print("VALSZTOTT KARAKTERED VADASZ")
        mhp = vhp
        mdm = vdm
        print(f"Élet={mhp}")
        print(f"SEBZES={mdm}")
        
    print("SZÖRNY MEGJELENÉSE")
    print("____________________________")

    print(f"A szörny életerej {shp} A SZÖRNY SEBZÉSE {sdm}")

    igennem=input("harcolsz? IGEN/NEM")

    if igennem == "NEM":
        print("köszönöm a jatekot")
        sys.exit()
        
    if igennem == "IGEN":
        print("KEZDÖDJÖN")
        print("________________________________")
        time.sleep(1)
    
    
    print("                              ")
    print("MEGJELNIK AZ ERDEI TUDER!!!!")
    print(f"TUNDER: BÁTOR {nev} AZÉRT JÖTTEM HOGY SEGITSEK HA MEGOLDOT REJTVÉNYEMET ELNYERHETED A VARÁZS PAJZSOT")
    
    ###############################################################################################################


    k1 = "Mi az elet ertelme az egyetlen szeles korben efogadott vlasz"
    v1 = "42"

    k2 = "mennyi 5 + 5?"
    v2 = "10"

    k3 = "hany perces volt a tanora a gimiben"
    v3 = "45"

    k4 = "hany csapat jatszik egy sima finals mecsben?"
    v4 = "3"

    k5 = "Az iskola a hatron cimu regényben hogyhivajk a föszereplö barátját aki egy álatrol van elnevezve?"
    v5 = "medve"

# Kérdések és válaszok párban (tuplék listája)
    parok = [
        (k1, v1),
        (k2, v2),
        (k3, v3),
        (k4, v4),
        (k5, v5)
        ]

# Egy véletlenszerű párt választunk ki
    valasztott_kerdes, helyes_valasz = random.choice(parok)

    print(f" TUNDER: VALASZOLD MEG KERDESEMET DICSO {nev}.")
    print(f" {valasztott_kerdes}")

    valasz = input(f"MIT VALASZOLSZ DICSO {nev}? ")

    if valasz.strip().lower() == helyes_valasz.lower():
        print(" Helyes válasz! ELNYERTED A PAJZSOT")
        ms = 1
    else:
        print(f" Rossz válasz! hulye vagy {nev}")
        print("_________________________________________")
        
        
        
        
    print("A TUDNDER ELTÜNIK PONT MINT AHOGY MEGJELNT A SZÖRNY KÖZELEDIK")
    
          
        
    print("TALÁLD EL A SZAMOT 1-5 KÖZÖTT és TIÉD A TÁMADÁS JOGA")
    szam = random.randint(1,1)
    tipp = int(input("tedd meg tipedet!!"))
    talalt = 0
    if tipp == szam:
        print("TALÁT te kezdesz")
        talalt = 1
    else:
        print("NEM TALÁLT nem te kezdesz")
        talalt = 0
            
    while shp > 0 :      
        if talalt == 1:
            print("megtámadod a szörnyet")
            shp -= mdm
            time.sleep(1)
            print(f"(SZÖRNY ÉLETE: {shp}")
            time.sleep(1)
            if shp <= 0:
                print("A SZÖRNY MEGHALT")
                break
            else:print("A szörny támad")
            if ms == 1:
                print("__________________________________")
                print("VAN PAJZSOD AMIVEL EGY TAMDAST KIVEDHETSZ")
                pp = input("HASZNALOD A PAJZSOD? IGEN/NEM")
                if pp == "IGEN":
                    print("A PAJZSOT HASZNÁLVA KIVÉDET A TÁMADÁST")
                    ms = 0
                else:
                        print("NEM HASZNALOD A PAJZSOT TÁMAD A SZÖRNY")
                        mhp -= sdm
                        time.sleep(1)
                        print(f"(ÉLETED: {mhp}")
                        if mhp <= 0:
                            print("MEGHALTÁL")
                            break
                        else:
                            gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                
                            if gyogy == "SIMA":
                                mhp += 2
                                print(f"GYOGYITÁSOD EREDMÉNYE ÉLETED:{mhp}")
                                time.sleep(1)
                    
                            if gyogy == "EXTREM":
                                tipp2 = 0
                                szam2 = random.randint(1,10)
                                print("TALAÁLD EL 1-10 a számot és 10 életed gyogyithatsz")
                                tipp2 = int(input("TIPPELJ!!!!!!!!!"))
                                time.sleep(1)
                                if tipp2 == szam2:
                                    mhp += 10
                                    print(f"SIKERES GYOGYITÁS EREDMÉNYE életed:{mhp}")
                                    time.sleep(1)
                    
                            else:
                                time.sleep(1)
            
            
            else:
                mhp -= sdm
                time.sleep(1)
                print(f"(ÉLETED: {mhp}")
                if mhp <= 0:
                    print("MEGHALTÁL")
                    break
                else:
                    gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                
                if gyogy == "SIMA":
                    mhp += 2
                    print(f"GYOGYITÁSOD EREDMÉNYE ÉLETED:{mhp}")
                    time.sleep(1)
                
                
                
                
                if gyogy == "EXTREM":
                    tipp2 = 0
                    szam2 = random.randint(1,10)
                    print("TALAÁLD EL 1-10 a számot és 10 életed gyogyithatsz")
                    tipp2 = int(input("TIPPELJ!!!!!!!!!"))
                    time.sleep(1)
                    if tipp2 == szam2:
                        mhp += 10
                        print(f"SIKERES GYOGYITÁS EREDMÉNYE életed:{mhp}")
                        time.sleep(1)
                    
                else:
                    time.sleep(1)
        if talalt == 0:
            print("szörny Megtámad")
            if ms == 1:
                print("__________________________________")
                print("VAN PAJZSOD AMIVEL EGY TAMDAST KIVEDHETSZ")
                pp = input("HASZNALOD A PAJZSOD? IGEN/NEM")
                if pp == "IGEN":
                    print("A PAJZSOT HASZNÁLVA KIVÉDET A TÁMADÁST")
                    ms = 0
                else:
                    print("NEM HASZNALOD A PAJZSOT TÁMAD A SZÖRNY")
                    mhp -= sdm
                    time.sleep(1)
                    print(f"(ÉLETED: {mhp}")
                    if mhp <= 0:
                        print("MEGHALTÁL")
                        break
                    else:
                        gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                
                        if gyogy == "SIMA":
                            mhp += 2
                            print(f"GYOGYITÁSOD EREDMÉNYE ÉLETED:{mhp}")
                            time.sleep(1)
                            print("TE támadsz")
                            shp -= mdm
                            time.sleep(1)
                    
                        if gyogy == "EXTREM":
                            tipp2 = 0
                            szam2 = random.randint(1,10)
                            print("TALAÁLD EL 1-10 a számot és 10 életed gyogyithatsz")
                            tipp2 = int(input("TIPPELJ!!!!!!!!!"))
                            time.sleep(1)
                            if tipp2 == szam2:
                                mhp += 10
                                print(f"SIKERES GYOGYITÁS EREDMÉNYE életed:{mhp}")
                                time.sleep(1)
                                    
                                print("TE támadsz")
                                shp -= mdm
                                time.sleep(1)
                    
                            else:
                                time.sleep(1)
                                print("TE támadsz")
                                shp -= mdm
                                time.sleep(1)
            
            
            else:
                mhp -= sdm
                time.sleep(1)
                print(f"(ÉLETED: {mhp}")
                if mhp <= 0:
                    print("MEGHALTÁL")
                    break
                else:
                    gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                
                if gyogy == "SIMA":
                    mhp += 2
                    print(f"GYOGYITÁSOD EREDMÉNYE ÉLETED:{mhp}")
                    time.sleep(1)
                    
                    print("TE támadsz")
                    shp -= mdm
                    time.sleep(1)
                
                
                
                
                if gyogy == "EXTREM":
                    tipp2 = 0
                    szam2 = random.randint(1,10)
                    print("TALAÁLD EL 1-10 a számot és 10 életed gyogyithatsz")
                    tipp2 = int(input("TIPPELJ!!!!!!!!!"))
                    time.sleep(1)
                    if tipp2 == szam2:
                        mhp += 10
                        print(f"SIKERES GYOGYITÁS EREDMÉNYE életed:{mhp}")
                        time.sleep(1)
                        
                        print("TE támadsz")
                        shp -= mdm
                        time.sleep(1)
                    
                else:
                    time.sleep(1)
                    
                    print("TE támadsz")
                    shp -= mdm
                    time.sleep(1)
        
        
        
        
        
    if shp <= 0:
        print("_______________________")
        print("GRATUNÁLUNK GYÖZTÉL A BIRODALOM MEGMENEKÜLT")
        pontok += 1
        tovab=input("TOVABB MESZ?? IGEN/NEM")
        if tovab == "NEM":
            s += 1
    
    
    if mhp <= 0:
        print("_______________________")
        print("ELBUKTÁL A SZÖRNY LEGYÖZÖTT")
    
    