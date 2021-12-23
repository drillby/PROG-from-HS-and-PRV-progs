<?php

if ($_POST == []) {
	echo "Script nelze volat přímo";
	die();
}

$nazev = $_POST["nazev_garaz"];
$mesto = $_POST["mesto_garaz"];
$produktivita = $_POST["produktivita_garaz"];

if ($mesto == "" || $nazev == "" || $produktivita == "" || $produktivita < 0 || $produktivita > 100) {
	header("Location: http://xeon.spskladno.cz/~valimj/garaze.html");
	die();
}

$servername = "";
$username = "";
$password = "";
$dbname = "";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}
// prepare and bind
$stmt = $conn->prepare("INSERT INTO Garaze (nazev_garaz, mesto, produktivita) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $nazev, $mesto, $produktivita);
$stmt->execute();

echo "Nový záznam byl úspěšně zaznamenán";

$stmt->close();
$conn->close();
