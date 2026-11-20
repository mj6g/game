import sys
import random
import time
import string


nev = "fejezet.txt"
valaszt = random.randint(2,2)

if valaszt == 1:
    nev = "1fejezet.txt"
    
if valaszt == 2:
        nev = "2fejezet.txt"    
    
if valaszt == 3:
        nev = "3fejezet.txt"    

if valaszt == 4:
    nev = "4fejezet.txt"
    
if valaszt == 5:
    nev = "5fejezet.txt"
    
if valaszt == 6:
    nev = "6fejezet.txt"
    
if valaszt == 7:
    nev = "7fejezet.txt"
    
if valaszt == 8:
    nev = "8fejezet.txt"
    
if valaszt == 9:
    nev = "9fejezet.txt"
    
if valaszt == 10:
    nev = "10fejezet.txt"
    
if valaszt == 11:
    nev = "11fejezet.txt"
    
if valaszt == 12:
    nev = "12fejezet.txt"
    
if valaszt == 13:
    nev = "13fejezet.txt"
    
if valaszt == 14:
    nev = "14fejezet.txt"
    
if valaszt == 15:
    nev = "15fejezet.txt"
    
if valaszt == 16:
    nev = "16fejezet.txt"
    
if valaszt == 17:
    nev = "17fejezet.txt"
    
    
if valaszt == 18:
    nev = "18fejezet.txt"
    
    
if valaszt == 19:
    nev = "19fejezet.txt"
    
    
if valaszt == 20:
    nev = "20fejezet.txt"
    
    
if valaszt == 21:
    nev = "21fejezet.txt"
    
    
if valaszt == 22:
    nev = "22fejezet.txt"
    
    
if valaszt == 23:
    nev = "23fejezet.txt"
 
if valaszt == 24:
    nev = "24fejezet.txt"
 
if valaszt == 25:
    nev = "25fejezet.txt"


szo1 =""
szo2 =""
szo3 =""
szo4 =""
szo5 =""
szo6 =""
szo7 =""
szo8 =""
szo9 =""
szo10 =""
szo11 =""
szo12 =""
szo13 =""
szo14 =""

szavakszam = 14





 
 
 
 
print(f"{nev}")
print("Mondat megalkotása")
while szavakszam > 0:
    with open(nev, 'r', encoding='utf-8') as fajl:
        sorok = [sor.strip() for sor in fajl if sor.strip()]
    if sorok:
        valasztott_sor = random.choice(sorok)
    
    # Szétvágjuk a sort szavakra
    szavak = valasztott_sor.split()
    
    if szavak:
        valasztott_szo = random.choice(szavak)
        
       
        tisztaszo = valasztott_szo.strip(string.punctuation + '„”’…–— ')
        
        
    if tisztaszo != ""and not tisztaszo.isdigit():
        
        
        
        if szavakszam ==14:
            szo1 = tisztaszo
        if szavakszam ==13:
            szo2 = tisztaszo
        if szavakszam ==12:
            szo3 = tisztaszo
            
        if szavakszam ==11:
            szo4 = tisztaszo
            
        if szavakszam ==10:
            szo5 = tisztaszo
            
        if szavakszam ==9:
            szo6 = tisztaszo
            
        if szavakszam ==8:
            szo7 = tisztaszo
            
        if szavakszam ==7:
            szo8 = tisztaszo
            
        if szavakszam ==6:
            szo9 = tisztaszo
            
        if szavakszam ==5:
            szo10 = tisztaszo
            
        if szavakszam ==4:
            szo11 = tisztaszo
            
        if szavakszam ==3:
            szo12 = tisztaszo
            
        if szavakszam ==2:
            szo13 = tisztaszo
            
        if szavakszam ==1:
            szo14 = tisztaszo
            
        
        
        szavakszam -= 1

szavak = [szo1, szo2, szo3, szo4, szo5, szo6, szo7, szo8, szo9, szo10, szo11, szo12, szo13, szo14]



kivalasztott_index = random.randint(0, len(szavak) - 1)




szavak[kivalasztott_index] = " .............. "

print("Feldolgozás", end="", flush=True)


for _ in range(10):
    time.sleep(0.5)
    print("*", end="", flush=True)

print()




####
print(*szavak, end=".\n")
####




        
        
