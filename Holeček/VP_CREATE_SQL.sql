CREATE TABLE Garaze
(
	id_garaz int AUTO_INCREMENT PRIMARY KEY,
	nazev_garaz char(50) UNIQUE NOT NULL,
	mesto char(50) NOT NULL,
	produktivita int(3) DEFAULT 0
);

CREATE TABLE Zakazky
(
	id_zakazka int AUTO_INCREMENT PRIMARY KEY,
	nazev_zakazka char(50) NOT NULL,
	hmotnost int NOT NULL,
	z_mesta char(50) NOT NULL,
	do_mesta char(50) NOT NULL,
	vzdalenost int DEFAULT 1,
	cena_km int DEFAULT 1
	/*celkova cena = vzdalenost * cena_km + 20%*/
);


CREATE TABLE Ridici
(
	id_ridic int AUTO_INCREMENT PRIMARY KEY,
	jmeno char(50) NOT NULL,
	prijmeni char(50) NOT NULL,
	tahac char(50) NOT NULL,
	garaz int, 
	hodnoceni int,
	FOREIGN KEY (garaz) REFERENCES Garaze(id_garaz) ON DELETE CASCADE
);

CREATE TABLE Dojete
(
	id_dojete int AUTO_INCREMENT PRIMARY KEY,
	dojete_zakazka int NOT NULL,
	dojete_ridic int NOT NULL,
	FOREIGN KEY (dojete_zakazka) REFERENCES Zakazky(id_zakazka),
	FOREIGN KEY (dojete_ridic) REFERENCES Ridici(id_ridic)
);

/*DROP TABLE Dojete, Ridici, Garaze, Zakazky*/