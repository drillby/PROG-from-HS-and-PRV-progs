<?php
$servername = "";
$username = "";
$password = "";
$dbname = "";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
	die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM Ridici
JOIN Garaze ON Ridici.garaz = Garaze.id_garaz";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
	// output data of each row
	while ($row = mysqli_fetch_assoc($result)) {
		echo "ID: " . $row["id_ridic"] . " Jméno: " . $row["jmeno"] . " Příjmení: " . $row["prijmeni"] . " Tahač: " . $row["tahac"] . " Garáž: " . $row["nazev_garaz"] . " Hodnocení: " . $row["hodnoceni"] . "<br>";
	}
} else
	echo "0 results";

mysqli_close($conn);
