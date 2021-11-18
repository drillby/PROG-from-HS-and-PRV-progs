<?php
$servername = "dbs.spskladno.cz"; // přihlašovací údaje
$username = "student14";
$password = "spsnet";
$database = "vyuka14";

try //zachytávání chyb
{
	$conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password); // přihlášení
	// set the PDO error mode to exception
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // přes tohle provádíš příkazy, něco jako v MyAdmin "proveď" v části kam píšeš SQL kód 
	echo "Přihášeno";

	/*$sql = "CREATE TABLE Pokus
		(
			id int AUTO_INCREMENT PRIMARY KEY,
			jmeno char(30) NOT NULL,
			prijmeni char(20) NOT NULL
		)"; // proměnná do který nahraješ SQL kód
		$conn->exec($sql); // příkaz na provedení SQL kódu*/
		echo "Tabulka vytvořena";
} 

catch(PDOException $e) // při chybe vypíše error podle SQL 
	{
	echo $sql . "<br>" . $e->getMessage();
	}

$conn = NULL; // odhlášení
?>