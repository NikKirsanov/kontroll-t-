import random

def patsiendid():
    n = int(input("Sisesta patsientide arv: "))
    nimed = []
    D_vitamiini_sisaldus = []
    for i in range(n):
        nimi = input(f"Sisestage {i+1}. patsiendi nimi: ")
        nimed.append(nimi)
        D_vitamiini_sisaldus.append(random.randint(10, 50))
    return nimed, D_vitamiini_sisaldus

def nedefitsiit(nimed, D_vitamiini_sisaldus):
    nimi_list = []
    for i in range(len(nimed)):
        if D_vitamiini_sisaldus[i] < 30:
            nimi_list.append(nimed[i])
    if nimi_list:
       print("D-vitamiini vaegusega patsientide nimekiri:")

       for nimi in nimi_list:
           print(nimi)
       else:
           print("D-vitamiini vaegusega patsiente ei ole.")

def srednee(D_vitamiini_sisaldus):
    srednee = sum(D_vitamiini_sisaldus) / len(D_vitamiini_sisaldus)
    print(f"D-vitamiini keskmine: {srednee:.2f}")

def top_k(nimed, D_vitamiini_sisaldus):
    k = int(input("Sisestage kuvatavate patsientide arv:"))
    if k > len(nimed):
         k = len(nimed)
         sorted_indices = sorted(range(len(D_vitamiini_sisaldus)), key=lambda i: D_vitamiini_sisaldus[i], reverse=True)
         print(f"Kõige suurema D-vitamiini skooriga {k} patsienti:")
    for i in range(k):
        print(f"{nimed[sorted_indices[i]]}: {D_vitamiini_sisaldus[sorted_indices[i]]}")

def min_k(nimed, D_vitamiini_sisaldus):
    k = int(input("Sisestage kuvatavate patsientide arv:"))
    if k > len(nimed):
        k = len(nimed)
    sorted_indices = sorted(range(len(D_vitamiini_sisaldus)), key=lambda i: D_vitamiini_sisaldus[i], reverse=False)
    print(f"Топ-{k} madalaima D-vitamiini tasemega patsiendid:")
    for i in range(k):
        print(f"{nimed[sorted_indices[i]]}: {D_vitamiini_sisaldus[sorted_indices[i]]}")


def poisk_po_imeni(nimed, D_vitamiini_sisaldus):
    name = input("Sisesta otsingu nimi:")
    found = False
    for i in range(len(nimed)):
        if nimed[i] == name:
                print(f"{nimed[i]}: {D_vitamiini_sisaldus[i]}")
        found = True
    if not found:
          print(f"Patsienti nimega {name} ei leitud.")

# Заполнение массивов
nimed, D_vitamiini_sisaldus = patsiendid()

# Меню
while True:
    print("Valige toiming:")
    print("1. Koostage nimekiri D-vitamiini vaegusega patsientidest")
    print("2. Leidke keskmine D-vitamiin")
    print("3. Kuva kõrgeima punktisummaga K patsiendi loend")
    print("4. Otsige töötajaid nime järgi")
    print("5. Kuvage madalaima punktisummaga K patsiendi loend")
    print("0. Mine välja")
    choice = input("Valige toiming: ")
    if choice == "1":
        nedefitsiit(nimed, D_vitamiini_sisaldus)
    elif choice == "2":
        srednee(D_vitamiini_sisaldus)
    elif choice == "3":
        top_k(nimed, D_vitamiini_sisaldus)
    elif choice == "4":
        poisk_po_imeni(nimed, D_vitamiini_sisaldus)
    elif choice == "5":
        min_k(nimed, D_vitamiini_sisaldus)
        pass
    elif choice == "0":
        break
   