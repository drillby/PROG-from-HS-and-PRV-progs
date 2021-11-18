# import math

# mocnina, odmocnina jako volba
# kruh
# kvadratická rovnice

while True:
    cislo_1 = float(input("první číslo"))
    cislo_2 = float(input("druhe cislo"))
    vysledek = cislo_1 + cislo_2
    pokus = 2 + 3 * 2  # 8
    print(vysledek)  # vypsal 8 => umí mat. pravidla
    print(pokus)
    zadani = input("zadej priklad ")
    print(zadani)
    print(eval(zadani))

    znak = input("zadej znak")
    if "=" in znak:
        print("***")

    if "=" not in znak:
        print("///")

    end = input("konec")
    if end == "y":
        exit()
