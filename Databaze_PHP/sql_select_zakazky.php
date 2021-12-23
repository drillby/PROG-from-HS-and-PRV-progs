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

$sql = "SELECT * FROM Zakazky";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  // output data of each row
  while ($row = mysqli_fetch_assoc($result)) {
    echo "ID: " . $row["id_zakazka"] . " Název zakázky: " . $row["nazev_zakazka"] . " Hmotnost nákladu: " . $row["hmotnost"] . " Z: " . $row["z_mesta"] . " Do: " . $row["do_mesta"] . " Vzdálenost: " . $row["vzdalenost"] . " Cena/km: " . $row["cena_km"] . "<br>";
  }
} else {
  echo "0 results";
}

mysqli_close($conn);
