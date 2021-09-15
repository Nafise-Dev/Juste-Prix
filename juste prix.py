from time import*
actu =time()
fin=time()+3
import random



while fin - actu >= 0  :
    print ("Le jeux commence dans ",round(fin - actu),"secondes.")
    sleep(1)
    actu = time()

print("DÃ©but du Juste Prix! Tu as 1min!")



y=random.randint(10000,40001)


import time
debut = time.time()

for k in range(1,1000,1):
    if (time.time() - debut >60):
        print("Le temps est Ã©coulÃ©")
        break




    x=(int(input("Entrez une proposition: ")))
    print("Proposition",k,":",x)


    if x<y:
        Commentaire="C'est plus"
        print(Commentaire)

    if x>y:
        Commentaire="C'est moins"
        print(Commentaire)

    if x==y:
        Commentaire="Bravo tu as trouvé le nombre!"
        print(Commentaire)
        if 25<k<50:
            print("C'est pas mal")


        if 0<k<=25:
            print("Trop fort!")


        if 50<k<=100:
            print("Trop nul!")



        if k>100:
            print("C'est trÃ¨s nul!")



        break