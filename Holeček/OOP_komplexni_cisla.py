import math


class Komplexni_cislo:
    def __init__(self, re, im):  # Spustí se pří vytváření Komplexni_cislo
        # Prázdné kus paměti RAM
        self.Real = re
        self.Imag = im

    def __str__(self):  # jak se Komplexni_cislo prevede na napis ( treba v print() )
        return "{} {} i{}".format(self.Real, "+" if self.Imag >= 0 else "-", abs(self.Imag))

    def vynasob(self, other):
        return Komplexni_cislo(self.Real*other.Real - self.Imag*other.Imag,
                               self.Real*other.Imag + self.Imag*other.Real)

    def secti(self, other):
        return Komplexni_cislo(self.Real + other.Real,
                               self.Imag + other.Imag)

    def velikost(self):
        return math.sqrt(self.Real**2 + self.Imag**2)


K1 = Komplexni_cislo(5, -2)
K2 = Komplexni_cislo(4, 7)
K3 = Komplexni_cislo(6, 3)

print(K1)  # --> 5 + i2
print(K2)
print(K3)

K4 = K1.vynasob(K2)  # vynasob(K1, K2)
print(K4)

K5 = K2.secti(K3)
print(K5)

print(K1.velikost())
K1.Imag = 100
print(K1.velikost())
