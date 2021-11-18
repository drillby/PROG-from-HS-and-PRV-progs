def preved_do_desitkove(cislo, vstupni_soustava):
    """
    :param cislo: [cifra1, cifra2, cifra3,...]
    :return:
    """
    cifra = 1
    vysledek = 0
    for hodnota in reversed(cislo):
        vysledek += hodnota*cifra
        cifra *= vstupni_soustava

    return vysledek


#print(preved_do_desitkove([1, 1, 1, 1, 1], 2))


def preved_z_desitkove(cislo, vstupni_soustava):
    vysledek = []
    while cislo != 0:
        vysledek.append(cislo % vstupni_soustava)
        cislo = cislo // vstupni_soustava

    return list(reversed(vysledek))


print(preved_z_desitkove(11, 3))
