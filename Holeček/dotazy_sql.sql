/* smaže tabulku */
DROP TABLE Tym;

/* vytvoří tabulku */
CREATE TABLE Tym
(
	id int AUTO_INCREMENT UNIQUE, /* AUTO_INCREMENT = autofill může být PRIMARY KEY */
	nazev char(50) NOT NULL,
	mesto char(50) NOT NULL, /*DEFAULT "Kladno"*/
	zustatek int(16) DEFAULT 0,
	CONSTRAINT UNIKATNI_tym UNIQUE (nazev, mesto) /* UNIQUE na nazev a mesto zaroveň */
);

INSERT INTO Tym (nazev, mesto, zustatek) VALUES
	("HC Rytíři", "Kladno", 1000),
	("HC Slavie", "Praha", 5000),
	("HC Sparta", "Praha", 6000),
	("HC Sparta", "Brno", 5600);

CREATE TABLE Hrac2(
	id int AUTO_INCREMENT PRIMARY KEY,
	jmeno char(20),
	prijmeni char(20) NOT NULL,
	datum_narozeni DATE,
	tym_id int,
	pozice_id int,
	FOREIGN KEY (tym_id) REFERENCES Tym(id) ON DELETE CASCADE /*hráč musí mít přižazený tým*/
);

INSERT INTO Hrac2 (jmeno, prijmeni, datum_narozeni, tym_id, pozice_id) VALUES
	("Adam", "Prvni", '1996-06-02', 2, 2),
	("Pavel", "Druhy", '2000-09-09', 1, 3),
	("Kuba", "Treti", '1998-01-05', 3, 1),
	("Josef", "Čtvrtý", '1997-01-06', 6, 2);

CREATE TABLE Pozice(
	id_poz int PRIMARY KEY AUTO_INCREMENT,
		pojmenovani char(20)
);

INSERT INTO Pozice(pojmenovani) VALUES
	("Utocnik"),
	("Obrana"),
	("Brankar");
	

/* získání dat */
SELECT nazev, mesto FROM Tym LIMIT 1;

SELECT nazev AS "Název Klubu", mesto AS "Město" FROM Tym;

SELECT nazev, mesto FROM Tym WHERE mesto = "Kladno";

SELECT MAX(id) FROM Tym;

SELECT MIN(id) FROM Tym;

SELECt AVG(id) FROM Tym;

/* zobrazí celou tabulku */
SELECT * FROM Tym;

SELECT SUM(zustatek) FROM Tym; /* součet zustatků */

SELECT COUNT(zustatek) FROM Tym;

SELECT * FROM Tym ORDERED BY nazev; /* seřadí podle názvu abecedně, může se přidat další podmínka podle čeho řadit*/

SELECT * FROM Tym ORDERED BY mesto ASC; /* DESC */

SELECT * FROM Tym GROUP BY mesto; /* stejný města se daj do skupiny a vypíše se jenom počet unikátních měst */

SELECT mesto, SUM(zustatek) AS "peněz ve městě" FROM Tym GROUP BY mesto;

/* vnožené dotazy */
SELECT * FROM Tym WHERE zustatek > (SELECT AVG(zustatek) FROM Tym);

SELECT * FROM Tym WHERE zustatek > (SELECT AVG(zustatek) FROM Tym) AND mesto = "Praha";

SELECT * FROM Tym WHERE zustatek > (SELECT AVG(zustatek) FROM Tym) OR mesto = "Praha";

SELECT * FROM Tym WHERE mesto IN ("Praha");

/* wildcards - 
	% 0+ znaků co se vyplňí samy na základě filtrace
	_ přesně jeden znka co se vyplní sám na základě filtrace

*/
SELECT * FROM Tym WHERE mesto LIKE "K%";

SELECT * FROM Tym WHERE mesto LIKE "K__dno";

/* mazání dat */
DELETE FROM Tym WHERE id=3;

/* kombinace tabulek */
SELECT prijmeni, datum_narozeni, nazev, mesto FROM Hrac2 JOIN Tym; /* každý s každyým */
SELECT prijmeni, datum_narozeni, nazev, mesto FROM Hrac2 JOIN Tym ON Hrac2.tym_id = Tym.id;

SELECT * FROM Tym INNER JOIN Hrac2 ON Tym.id=Hrac2.tym_id;
SELECT * FROM Tym LEFT JOIN Hrac2 ON Tym.id=Hrac2.tym_id;
SELECT * FROM Tym RIGHT JOIN Hrac2 ON Tym.id=Hrac2.tym_id;

SELECT * FROM Tym INNER JOIN Hrac2 ON Tym.id=Hrac2.tym_id
UNION
SELECT * FROM Tym LEFT JOIN Hrac2 ON Tym.id=Hrac2.tym_id;

/*spojení 3 tabulek*/
SELECT * FROM
Tym
JOIN Hrac ON Tym.id = Hrac2.tym_id
JOIN Pozice ON Hrac2.pozice_id = Pozice.id_poz