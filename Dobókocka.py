import random 

nyert=0
vesztett=0
bank=0
lejatszott=0
start=int(input("1: Kezdés 2: Kilépés\n"))

while start==1:
    lejatszott+=1
    dobokocka=random.randint(1,6)
    dobokockamachine=random.randint(1,6)
    
    
    print("Egyenlege: ",bank)
      
    print("Kezdés")
    tet=int(input("Kérem adjon meg egy tétet:  "))
    print("Az ön dobása: ",dobokocka)
    print("A gép dobása ", dobokockamachine)
    if dobokocka>dobokockamachine:
        print("Ezt a kört megnyerte:)")
        bank+=tet
        nyert+=1
        print("Egyenlege: ", bank)
        
    elif dobokocka<dobokockamachine:
        print("Ön most vesztett:(")
        bank-=tet 
        vesztett+=1
        print("Egyenlege: ", bank)
    else:
        print("A dobott értékek egyenlőek")
        print("Egyenlege: ", bank)



    dobokocka=random.randint(1,6)
    dobokockamachine=random.randint(1,6)
    
    print("Következő kör")
    tet=int(input("Kérem adjon meg egy tétet:  "))
    print("Az ön dobása: ",dobokocka)
    print("A gép dobása ", dobokockamachine)
    if dobokocka>dobokockamachine:
        print("Ezt a kört megnyerte:)")
        bank+=tet
        nyert+=1
        print("Egyenlege: ", bank)
        
    elif dobokocka<dobokockamachine:
        print("Ön sajnos vesztett:(")
        bank-=tet 
        vesztett+=1
        print("Egyenlege: ", bank)
    else:
        print("A dobott értékek egyenlőek")
        print("Egyenlege: ", bank)



    dobokocka=random.randint(1,6)
    dobokockamachine=random.randint(1,6)

    print("Utolsó kör")
    tet=int(input("Kérem adjon meg egy tétet:  "))
    print("Az ön dobása: ",dobokocka)
    print("A gép dobása ", dobokockamachine)
    if dobokocka>dobokockamachine:
        print("Gratulálunk, ön nyert:)")
        bank+=tet
        nyert+=1
        print("Egyenlege: ", bank)
        
    elif dobokocka<dobokockamachine:
        print("Vesztett, sajnáljuk:(")
        bank-=tet 
        vesztett+=1
        print("Egyenlege: ", bank)
    else:
        print("A dobott értékek egyenlőek")
        print("Egyenlege: ", bank)


    start=int(input("Szeretné az eddig  össze gyűlt pénzt kivenni vagy játszana tovább? 1: kiveszem a pénzt 2: játszom tovább"))
    if start==1:
        print("Lejátszott játékok: ", lejatszott)
        print("Megynyert körök: ", nyert)
        print("Vesztett körök: ", vesztett)
        print("Nyerési arány: ", nyert,":",vesztett,"=",nyert/vesztett)
