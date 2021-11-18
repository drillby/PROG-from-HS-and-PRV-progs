import mysql.connector

# print(dir(mysql))

vyber_databazi = """Zvol databázi do které budeš zapisovat data:
1. Garáže
2. Řidiči
3. Zakázky
4. Dojeté zakázky"""

rozsah = "VYBER ČÍSLO V ROZSAHU!"

data = "ZADEJ HODNOTU!"

kladne = "ZADEJ KLADNÉ ČÍSLO!"

index = 0

mydb = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student14",
    password="spsnet",
    database="vyuka14"
)
mycursor = mydb.cursor()

print(vyber_databazi)
volba = int(input("Vaše volba: "))

while volba < 1:
    print("\n")
    print(rozsah)
    volba = int(input("Vaše volba: "))

while volba > 5:
    print("\n")
    print(rozsah)
    volba = int(input("Vaše volba: "))

print("\n")

try:
    if volba == 1:
        nazev_garaz_input = input("Název garáže: ")
        while not nazev_garaz_input:
            print("\n")
            print(data)
            nazev_garaz_input = input("Název garáže: ")

        mesto_input = input("Město: ")
        while not mesto_input:
            print("\n")
            print(data)
            mesto_input = input("Město: ")

        produktivita_input = int(input("Produktivita (v%): "))
        while produktivita_input < 0:
            print("\n")
            print(data)
            produktivita_input = int(input("Produktivita (v%): "))

        while produktivita_input > 100:
            print("\n")
            print("PRODUKTIVITA NESMÍ MÍT VÍCE JAK 100%!")
            produktivita_input = int(input("Produktivita (v%): "))

        sql_insert = """INSERT INTO Garaze (nazev_garaz, mesto, produktivita) VALUES
            ("{}", "{}", {});""".format(nazev_garaz_input, mesto_input, produktivita_input)

        mycursor.execute(sql_insert)
        mydb.commit()  # provede execute

    elif volba == 2:
        jmeno_input = input("Jméno řidiče: ")
        while not jmeno_input:
            print("\n")
            print(data)
            jmeno_input = input("Jméno řidiče: ")

        prijmeni_input = input("Příjmení řidiče: ")
        while not prijmeni_input:
            print("\n")
            print(data)
            prijmeni_input = input("Příjmení řidiče: ")

        sql_select = "SELECT id_garaz, nazev_garaz, mesto FROM Garaze"
        mycursor.execute(sql_select)
        myresult = mycursor.fetchall()
        for index, nazev_garaz, mesto in myresult:
            print("Garáž", nazev_garaz, "ve městě", mesto, "má ID", index)

        garaz_input = int(input("ID garáže: "))
        while garaz_input < 1:
            print("\n")
            print(rozsah)
            garaz_input = int(input("ID garáže: "))

        while garaz_input > index:
            print("\n")
            print(rozsah)
            garaz_input = int(input("ID garáže: "))

        tahac_input = input("Název tahače: ")
        while not tahac_input:
            print("\n")
            print(data)
            tahac_input = input("Název tahače: ")

        hodnoceni_input = int(input("Hodnocení řidiče (v%): "))
        while hodnoceni_input < 0:
            print("\n")
            print(rozsah)
            hodnoceni_input = int(input("Hodnocení řidiče (v%): "))

        while hodnoceni_input > 100:
            print("\n")
            print(rozsah)
            hodnoceni_input = int(input("Hodnocení řidiče (v%): "))

        sql_insert = """INSERT INTO Ridici (jmeno, prijmeni, garaz, tahac, hodnoceni) VALUES
            ("{}", "{}", {}, "{}", {});""".format(jmeno_input, prijmeni_input, garaz_input, tahac_input, hodnoceni_input)

        print(sql_insert)
        mycursor.execute(sql_insert)
        mydb.commit()  # provede execute

    elif volba == 3:
        nazev_zakazky_input = input("Název zakázky: ")
        while not nazev_zakazky_input:
            print("\n")
            print(data)
            nazev_zakazky_input = input("Název zakázky: ")

        hmotnost_input = int(input("Hmotnost zakázky (v kg): "))
        while hmotnost_input < 1:
            print("\n")
            print(kladne)
            hmotnost_input = int(input("Hmotnost zakázky (v kg): "))

        z_mesta_input = input("Z města: ")
        while not z_mesta_input:
            print("\n")
            print(data)
            z_mesta_input = input("Z města: ")

        do_mesta_input = input("Do města: ")
        while not do_mesta_input:
            print("\n")
            print(data)
            do_mesta_input = input("Do města: ")

        vzdalenost_input = int(input("Vzdálenost (v km): "))
        while vzdalenost_input < 1:
            print("\n")
            print(kladne)
            vzdalenost_input = int(input("Vzdálenost (v km): "))

        cena_km_input = int(input("Cena za km: "))
        while cena_km_input < 1:
            print("\n")
            print(kladne)
            cena_km_input = int(input("Cena za km: "))

        sql_insert = """INSERT INTO Zakazky (nazev_zakazka, hmotnost, z_mesta, do_mesta, vzdalenost, cena_km) VALUES
            ("{}", {}, "{}", "{}", {}, {})""".format(nazev_zakazky_input, hmotnost_input, z_mesta_input, do_mesta_input, vzdalenost_input, cena_km_input)

        mycursor.execute(sql_insert)
        mydb.commit()  # provede execute

    elif volba == 4:
        sql_select = "SELECT id_zakazka, nazev_zakazka FROM Zakazky"
        mycursor.execute(sql_select)
        myresult = mycursor.fetchall()
        for index, nazev_zakazka in myresult:
            print("Zakázka", nazev_zakazka, "má ID", index)

        dojete_zakazka_input = int(input("ID Zakázky: "))
        while dojete_zakazka_input < 1:
            print("\n")
            print(rozsah)
            dojete_zakazka_input = int(input("ID Zakázky: "))

        while dojete_zakazka_input > index:
            print("\n")
            print(rozsah)
            dojete_zakazka_input = int(input("ID zakázky: "))

        sql_select = "SELECT id_ridic, jmeno, prijmeni FROM Ridici"
        mycursor.execute(sql_select)
        myresult = mycursor.fetchall()
        for index, jmeno, prijmeni in myresult:
            print("Řidič", jmeno, prijmeni, "má ID", index)

        dojete_ridic_input = int(input("ID řiidče: "))
        while dojete_ridic_input < 1:
            print("\n")
            print(rozsah)
            dojete_ridic_input = int(input("ID řiidče: "))

        while dojete_ridic_input > index:
            print("\n")
            print(rozsah)
            dojete_ridic_input = int(input("ID řiidče: "))

        sql_insert = """INSERT INTO Dojete (dojete_zakazka, dojete_ridic) VALUES
            ("{}", "{}")""".format(dojete_zakazka_input, dojete_ridic_input)

        mycursor.execute(sql_insert)
        mydb.commit()

except mysql.connector.Error as err:  # errory

    # print("Error Code:", err.errno)
    # print("SQLSTATE:", err.sqlstate)
    # print("Message:", err.msg)

    if volba == 1 and err.errno == 1062:
        print("GARÁŽ S TÍMTO NÁZVEM JIŽ EXISTUJE!")

mydb.close()
