import os
import os.path
from datetime import date
from os import path
from PIL import Image

dnes = date.today()
datum = dnes.strftime("%Y_%m_%d")

cislo_img = "0001"
nazev_souboru_prejmenovat = "IMG_{cislo}.jpg".format(cislo=cislo_img)

cislo_faktury = input("Zadej číslo první faktury: ")


vsechny_soubory = "C:/Users/Administrátor/Documents/{datum}".format(
    datum=datum)

if not path.exists(vsechny_soubory):
    parent_dir = "C:/Users/Administrátor/Documents"
    cesta = os.path.join(parent_dir, datum)
    os.mkdir(cesta)

vsechny_soubory = os.listdir(
    "C:/Users/Administrátor/Documents/{datum}".format(datum=datum))

for soubor in vsechny_soubory:
    if soubor == nazev_souboru_prejmenovat:
        os.rename("C:/Users/Administrátor/Documents/{datum}/IMG_{cislo_obr}.jpg".format(
            datum=datum, cislo_obr=cislo_img), "C:/Users/Administrátor/Documents/{datum}/FP_{faktura}.jpg".format(datum=datum, faktura=cislo_faktury))

        obrazek = Image.open(
            "C:/Users/Administrátor/Documents/{datum}/FP_{faktura}.jpg".format(datum=datum, faktura=cislo_faktury))
        obrazek.save("C:/Users/Administrátor/Documents/{datum}/FP_{faktura}.pdf".format(
            datum=datum, faktura=cislo_faktury))
        os.remove("C:/Users/Administrátor/Documents/{datum}/FP_{faktura}.jpg".format(
            datum=datum, faktura=cislo_faktury))

        cislo_faktury = int(cislo_faktury) - 1
        if cislo_faktury < 100:
            cislo_faktury = "0{cislo}".format(cislo=cislo_faktury)

        cislo_img = int(cislo_img) + 1
        if cislo_img < 10:
            cislo_img = "000{cislo}".format(cislo=cislo_img)
        elif cislo_img > 10 and cislo_img < 100:
            cislo_img = "00{cislo}".format(cislo=cislo_img)
        elif cislo_img > 100 and cislo_img < 1000:
            cislo_img = "0{cislo}".format(cislo=cislo_img)
        elif cislo_img > 1000 and cislo_img < 10000:
            cislo_img = "{cislo}".format(cislo=cislo_img)

        cislo_img = str(cislo_img)
        nazev_souboru_prejmenovat = "IMG_{cislo}.jpg".format(cislo=cislo_img)
