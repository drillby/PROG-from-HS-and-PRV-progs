def je_sude(cislo: int):
    """
    Kontroluje sudost čísla
    """
    if cislo % 2 == 0:
        return True


def funkce():
    """
    Každé reáalné číslo časem dojde k 1
    """
    cislo = input("Pocatecni cislo: ")
    cislo = int(cislo)
    while cislo != 1:
        if je_sude(cislo):
            cislo /= 2
        else:
            cislo = 3*cislo + 1
        print(cislo)


funkce()
