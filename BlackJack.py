import random

player=[]
machine=[]
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]

start=int(input("Szeretné elkezdeni a játékot?: 1: igen 2: nem\n"))

while start==1:
    while len(player)<2:
        player.append(random.choice(cards))
    print("Az ön lapjai: ", player)

    while len(machine)<2:
        machine.append(random.choice(cards)) 
    print("A gép lapjai: ", machine)

    sequel=int(input("1: Folytatás "))
    if sequel==1:
        player.append(random.choice(cards))
        print("Az ön lapjai: ", player)
        
        if sum(player)==21:
            print("gratulálok ön nyert")

        elif sum(player)>21:
            print("sajnálom nem nyert")
        else:
            print("A gép következik")
            machine.append(random.choice(cards))
            print("A gép lapjai: ", machine)
            
            if sum(player)>sum(machine) and sum(player)<=21:
                print("gratulálok ön nyert")

            elif sum(player)<sum(machine) and sum(machine)<=21:
                print("sajnálom nem nyert")

            elif sum(machine)>21:
                print("gratulálok ön nyert")

            elif sum(machine)==21:
                print("sajnálom nem nyert")

    else:
        print("Ismét a gép jön")
        machine.append(random.choice(cards))
        print("A gép lapjai: ", machine)

        if sum(player)>sum(machine) and sum(player)<=21:
           print("gratulálok ön nyert")

        elif sum(player)<sum(machine) and sum(machine)<=21:
           print("sajnálom nem nyert")

        elif sum(machine)==21:
           print("sajnálom nem nyert")

        elif sum(machine)>21:
            
           print("gratulálok ön nyert")

    start=int(input("Game over. Kilépés: 2\n"))
    if start==2:
        print("Várunk vissza!")

