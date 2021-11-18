class Bunka:
    def __init__(self, zprava):
        self.zprava = zprava
        self.dalsi_bunka = None

    def __str__(self):
        return "Bunka se zpravou: "+self.zprava


class Zasobnik:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self.velikost = 0
        self.prvni_bunka = None

    def pridej(self, nova_bunka: Bunka):
        if self.velikost < self.kapacita:
            nova_bunka.dalsi_bunka = self.prvni_bunka
            self.prvni_bunka = nova_bunka
            self.velikost += 1
        else:
            print("Zasobník je plný, nejde přidat další buňka")

    def odeber(self):
        if self.velikost == 0:
            print("Zásobník je prázdný, nejde odebrat buňku")
            return None
        else:
            aktualni = self.prvni_bunka
            predposledni = None
            while aktualni.dalsi_bunka is not None:  # je aktualní poslední buňka ve frontě?
                predposledni = aktualni
                aktualni = aktualni.dalsi_bunka

            predposledni.dalsi_bunka = None
            self.velikost -= 1
            return aktualni  # v aktualni je poslední buňka fronty

    def vypis_vsechny_bunky(self):
        print("=== Zasobnik ===")
        aktualni = self.prvni_bunka
        while aktualni is not None:
            print(aktualni)
            aktualni = aktualni.dalsi_bunka
        print("===  ===")


B1 = Bunka("Prvni")
B2 = Bunka("Druha")
B3 = Bunka("Treti")
B4 = Bunka("Ctvrta")

F1 = Zasobnik(3)
F1.pridej(B1)
F1.pridej(B2)
F1.pridej(B3)
F1.vypis_vsechny_bunky()
F1.pridej(B4)
F1.vypis_vsechny_bunky()
print("Odebírám: ", F1.odeber())
F1.vypis_vsechny_bunky()
print("Odebírám: ", F1.odeber())
print("Odebírám: ", F1.odeber())
F1.vypis_vsechny_bunky()
print("Odebírám: ", F1.odeber())
