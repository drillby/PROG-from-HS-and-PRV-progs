<?php

	if ($_POST==[]) 
		{
		echo "Script nelze volat přímo";
		die();
		}

	$jmeno=$_POST["jmeno_ridic"];
	$prijmeni=$_POST["prijemni_ridic"];
	$tahac=$_POST["tahac_ridic"];
	$garaz=$_POST["id_garaz"];
	$hodnoceni=$_POST["hodnoceni_ridic"];
    
	if ($jmeno=="" || $prijemni =="" || $tahac=="" || $garaz=="" || $produktivita>100)
	{
		header("Location: http://xeon.spskladno.cz/~valimj/garaze.html");
		die ();
	}

$servername = "dbs.spskladno.cz";
$username = "student14";
$password = "spsnet";
$dbname = "vyuka14";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
// prepare and bind
$stmt = $conn->prepare("INSERT INTO Garaze (nazev_garaz, mesto, produktivita) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $nazev, $mesto, $produktivita);
$nazev=$_POST["nazev_garaz"];
$mesto=$_POST["mesto_garaz"];
$produktivita=$_POST["produktivita_garaz"];
$stmt->execute();

  echo "Nový záznam byl úspěšně zaznamenán";

$stmt->close();
$conn->close();
?>







