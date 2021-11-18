<?php
$servername = "dbs.spskladno.cz";
$username = "student14";
$password = "spsnet";
$dbname = "vyuka14";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT id_dojete, nazev_zakazka, jmeno, prijmeni FROM
                        Dojete
                        JOIN Zakazky ON Dojete.dojete_zakazka = Zakazky.id_zakazka 
                        JOIN Ridici ON Dojete.dojete_ridic = Ridici.id_ridi";
                        
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
  // output data of each row
  while($row = mysqli_fetch_assoc($result)) {
    echo "ID: " . $row["id_dojete"]. " Dojetá zakázka: " . $row["nazev_zakazka"]. " Ridičem: " . $row["jmeno"]. " " . $row["prijmeni"]."<br>";
  }
} else {
  echo "0 results";
}

mysqli_close($conn);
?>
