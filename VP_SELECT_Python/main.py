import mysql.connector


vyber_databazi = """Zvol databázi ze které chceš vypsat data:
1. Garáže
2. Řidiči
3. Zakázky
4. Dojeté zakázky
SPECIAL pro vlastní příkaz"""

rozsah = "ZADEJTE PLATNÝ PŘÍKAZ!"

chyba = "PŘÍKAZ V TAKOVÉTO FORMĚ NEMŮŽE EXISTOVAT!"

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
mycursor = mydb.cursor()

print(vyber_databazi)
volba = input("Vaše volba: ")

if volba != "SPECIAL":
    while volba < "1":
        print("\n")
        print(rozsah)
        volba = input("Vaše volba: ")

    while volba > "5":
        print("\n")
        print(rozsah)
        volba = input("Vaše volba: ")

print("\n")

if volba == "1":
    sql_select = "SELECT * FROM Garaze"
    mycursor.execute(sql_select)
    myresult = mycursor.fetchall()
    for index, nazev_garaz, mesto, produktivita in myresult:
        print("Garáž s ID", index, "s názvem", nazev_garaz, "ve městě",
              mesto, "má produktivitu na", produktivita, "%")

elif volba == "2":
    sql_select = """SELECT * FROM
                    Ridici 
                    JOIN Garaze ON Ridici.garaz = Garaze.id_garaz """
    mycursor.execute(sql_select)
    myresult = mycursor.fetchall()
    for index, jmeno, prijmeni, tahac, garaz, hodnoceni, id_garaz, nazev_garaz, mesto, produktivita in myresult:
        print("Řidič s ID", index, "má jméno", jmeno, prijmeni, "sídlí v garáži", nazev_garaz,
              "ve městě", mesto, "řídí tahač", tahac, "a má hodnocení", hodnoceni, "%")

elif volba == "3":
    sql_select = "SELECT * FROM Zakazky"
    mycursor.execute(sql_select)
    myresult = mycursor.fetchall()
    for index, nazev_zakazka, hmotnost, z_mesta, do_mesta, vzdalenost, cena_km in myresult:
        print("Zakázka s ID", index, "názvem", nazev_zakazka, "hmontostí", hmotnost, "tun, putuje z města",
              z_mesta, "do města", do_mesta, "vzdálenost je", vzdalenost, "km a cena za km činí", cena_km, "Kč")
        print("Řidič si za zakázku vydělá", (vzdalenost *
                                             cena_km) + ((vzdalenost * cena_km)/5), "Kč")

elif volba == "4":
    sql_select = """SELECT id_dojete, nazev_zakazka, jmeno, prijmeni FROM
                        Dojete
                        JOIN Zakazky ON Dojete.dojete_zakazka = Zakazky.id_zakazka 
                        JOIN Ridici ON Dojete.dojete_ridic = Ridici.id_ridic"""
    mycursor.execute(sql_select)
    myresult = mycursor.fetchall()
    for index, nazev_zakazka, jmeno, prijmeni in myresult:
        print("Zakázku s ID", index, "názvem",
              nazev_zakazka, "dovezl řidič", jmeno, prijmeni)

elif volba == "SPECIAL":
    try:
        print("Nyní zadejte příkaz pro vypsání z databáze")
        print("pozn.: Výsledek nebude přehledně vypsán, vypíše se tak jak se data zapsala do databáze")
        sql_select = input("Váš příkaz: ")
        mycursor.execute(sql_select)
        myresult = mycursor.fetchall()
        print(myresult)

    except mysql.connector.Error as err:
        print(chyba)
        print("Zpráva:", err.msg)

mydb.close()
