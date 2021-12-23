<?php

if ($_POST == []) {
	echo "Script nelze volat přímo";
	die();
}

$nazev = $_POST["nazev_zakazka"];
$hmotnost = $_POST["hmotnost_zakazka"];
$odkud = $_POST["od_zakazka"];
$kam = $_POST["do_zakazka"];
$vzdalenost = $_POST["vzdalenost_zakazka"];
$cenakm = $_POST["cena_zakazka"];


if ($nazev == "" || $hmotnost == "" || $odkud == "" || $kam == "" || $vzdalenost == "" || $cenakm == "") {
	header("Location: http://xeon.spskladno.cz/~valimj/zakazky.html");
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
$stmt = $conn->prepare("INSERT INTO Zakazky (nazev_zakazka, hmotnost, z_mesta, do_mesta, vzdalenost, cena_km) VALUES (?, ?, ?, ?, ?, ?)");
$stmt->bind_param("ssssss", $nazev, $hmotnost, $odkud, $kam, $vzdalenost, $cenakm);
$nazev = $_POST["nazev_zakazka"];
$hmotnost = $_POST["hmotnost_zakazka"];
$odkud = $_POST["od_zakazka"];
$kam = $_POST["do_zakazka"];
$vzdalenost = $_POST["vzdalenost_zakazka"];
$cenakm = $_POST["cena_zakazka"];
$stmt->execute();

echo "Nový záznam byl úspěšně zaznamenán";

$stmt->close();
$conn->close();
