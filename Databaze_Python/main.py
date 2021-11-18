import mysql.connector

mydb = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student14",
    password="spsnet",
    database="vyuka14"except mysql.connector.Error as err: #errory
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE:", err.sqlstate)
    print("Message:", err.msg)
)
mycursor = mydb.cursor()
try:
    sql_create = """CREATE TABLE Soutez( 
        id INT,
        nazev CHAR(20))"""


    sql_insert = """INSERT INTO Soutez(id, nazev) VALUES
        (1, "Extraliga"),
        (2, "Prvni liga"),
        (3, "Okresni prebor")"""

    mycursor.execute(sql_create) #potvrzeni k provedeni
    mycursor.execute(sql_insert)
    mydb.commit() #provede executy



sql_select = "SELECT id, nazev FROM Soutez"
mycursor.execute(sql_select)

myresult  =mycursor.fetchmany(3) #kolik radku stahnu
print(myresult)

for index, nazev in myresult:
    print("Soutez: ", nazev, "má index", index)



mydb.close()