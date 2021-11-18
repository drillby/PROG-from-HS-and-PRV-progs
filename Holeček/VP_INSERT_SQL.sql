INSERT INTO Garaze (nazev_garaz, mesto, produktivita) VALUES
	("Alfa", "Praha", 95),
	("Beta", "Brno", 66);

INSERT INTO Zakazky (nazev_zakazka, hmotnost, z_mesta, do_mesta, vzdalenost, cena_km) VALUES
	("Procesory", 3, "Ostrava", "Oslo", 1596, 35),
	("Automobily", 15, "Vídeň", "Brno", 148, 41);

INSERT INTO Ridici (jmeno, prijmeni, garaz, tahac, hodnoceni) VALUES
	("Daniel", "Vávra", 1, "Scania S Normal Roof", 3),
	("Halina", "Pawllovská", 2, "Scania S High Roof", 4);

INSERT INTO Dojete(dojete_zakazka, dojete_ridic) VALUES
	(1, 1),
	(2, 2);

