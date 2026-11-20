import sys
import random
import time
import os
s = 0
pontok = 0
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
        
    print("TALÁLD EL A SZAMOT 1-5 KÖZÖTT és TIÉD A KEZDÉS JOGA")
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
            mhp -= sdm
            time.sleep(1)
            print(f"(ÉLETED: {mhp}")
            if mhp <= 0:
                print("MEGHALTÁL")
                break
            else:
                gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                
                if gyogy == "SIMA":
                    mhp += 1
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
            mhp -= sdm
            time.sleep(1)
            print(f"(ÉLETED: {mhp}")
            time.sleep(1)
            if mhp <= 0:
                print("MEGHALTÁL")
                break
            else:
                gyogy=input("SIMA GYOGYITASZ VAGY EXTREM GYOGYITASZ(KOCKAZATOS)? SIMA/EXTREM")
                if gyogy == "SIMA":
                    mhp += 1
                    print(f"GYOGYITÁSOD EREDMÉNYE ÉLETED:{mhp}")
                
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
                        
                        
                print(f"(SZÖRNY ÉLETE: {shp}")
                if shp <= 0:
                    print("A SZÖRNY MEGHALT")
                    break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
    
    