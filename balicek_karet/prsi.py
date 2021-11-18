import random

druhy = ["Žaludy", "Srdce", "Kule", "Zelené"]


class Karta:
    def __init__(self, hodnota, druh):
        self.druh = druh
        self.hodnota = hodnota

    def ukaz(self):
        if self.hodnota == 14:
            print(f"Eso, {self.druh}")

        elif self.hodnota == 13:
            print(f"Král, {self.druh}")

        elif self.hodnota == 12:
            print(f"Svršek, {self.druh}")

        elif self.hodnota == 11:
            print(f"Spodek, {self.druh}")

        else:
            print(f"{self.hodnota}, {self.druh}")


class LizaciBalicek:
    def __init__(self):
        self.karty = []
        self.seszav_balicek()

    def seszav_balicek(self):
        for d in druhy:
            for h in range(7, 15):
                self.karty.append(Karta(h, d))

    def ukaz(self):
        for k in self.karty:
            k.ukaz()

    def zamichej(self):
        for i in range(len(self.karty) - 1, 0, -1):
            rand = random.randint(0, i)
            self.karty[i], self.karty[rand] = self.karty[rand], self.karty[i]

    def lizejKartu(self):
        return self.karty.pop()


class Hrac:
    def __init__(self):
        self.ruka = []

    def lizej(self, balicek):
        self.ruka.append(balicek.lizejKartu())
        return self

    def ukazRuku(self):
        for karta in self.ruka:
            karta.ukaz()

    def zahod(self, zahod_kartu_input):
        self.ruka.pop(zahod_kartu_input - 1)

    def zahozena_karta(self):
        return self.ruka[zahod_kartu_input - 1]


class OdhazocaviBalicek:
    def __init__(self):
        self.zahozene_karty = []

    def zahozena_karta1(self):
        self.zahozene_karty.append(hrac1.zahozena_karta())

    def zahozena_karta2(self):
        self.zahozene_karty.append(hrac1.zahozena_karta())

    def ukaz(self):
        for karta in self.zahozene_karty:
            karta.ukaz()


balicek = LizaciBalicek()
hrac1 = Hrac()
hrac2 = Hrac()
odhazovaci_balicek = OdhazocaviBalicek()
balicek.zamichej()

kolik_karet = int(input("S kolika kartami budete začínat? "))
for cislo in range(kolik_karet):
    hrac1.lizej(balicek)
    hrac2.lizej(balicek)

while hrac1.ukazRuku and hrac2.ukazRuku:
    if not balicek.karty:
        balicek.karty = odhazovaci_balicek.zahozene_karty
        balicek.zamichej()
        for k in odhazovaci_balicek.zahozene_karty:
            odhazovaci_balicek.zahozene_karty.pop(0)

    hrac1.ukazRuku()
    zahod_kartu_input = int(input("Jakou kartu chceš zahodit? "))
    odhazovaci_balicek.zahozena_karta1()
    hrac1.zahod(zahod_kartu_input)

print("Game over!")
