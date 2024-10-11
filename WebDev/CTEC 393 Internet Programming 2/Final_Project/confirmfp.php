    <!DOCTYPE html>
<html>
<head>
 <link rel="Stylesheet" href="baucumfp.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, intial-scale=1.0">
    <title>Confirmation</title>
</head>
<body>
    <h1>Here is the information about Jones Landscaping!</h1>
    <h3>Return to the home page.</h3>
    <a href="indexfp.html">
    <button>Home</button>
</a>

<?php
    $servername = "localhost";
    $username = "qdfjfswb_ctec393";
    $password = "ctec350";
    $dbname = "qdfjfswb_ctec393";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    $sql1="SELECT * FROM Jobs";
    $result = mysqli_query($conn, $sql1);

if (mysqli_num_rows($result) > 0) {

  echo "<br/>";
  echo "<h2>Here are the current jobs</h2>";
  
  // output data of each row in a table
  echo "<table border='1'>
        <th>Job ID</th>
        <th>Service Name</th>
        <th>Cost($)</th>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>".$row['Job_ID']."</td>";
    echo "<td>".$row['Service_Name']."</td>";
    echo "<td>".$row['Cost']."</td>";
    echo "</tr>";
  }
  echo "</table>";

} else {
  echo "0 results";
}
 

    $sql2="SELECT * FROM Invoice";
    $result = mysqli_query($conn, $sql2);

if (mysqli_num_rows($result) > 0) {

  echo "<br/>";
  echo "<h2>Here are the past invoices</h2>";
  // output data of each row in a table
  echo "<table border='1'>
        <th>Employee ID</th>
        <th>Equipment ID</th>
        <th>Job ID</th>
        <th>Date</th>
        <th>Time</th>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>".$row['Employee_ID']."</td>";
    echo "<td>".$row['Equipment_ID']."</td>";
    echo "<td>".$row['Job_ID']."</td>";
    echo "<td>".$row['Date']."</td>";
    echo "<td>".$row['Time']."</td>";
    echo "</tr>";
  }
  echo "</table>";

} else {
  echo "0 results";
}


    $sql3="SELECT * FROM Employees";
    $result = mysqli_query($conn, $sql3);

if (mysqli_num_rows($result) > 0) {

  echo "<br/>";
  echo "<h2>Here are the current employees and their associated clients.</h2>";
  // output data of each row in a table
  echo "<table border='1'>
        <th>Employee ID</th>
        <th>Manager ID</th>
        <th>Name</th>
        <th>Client ID</th>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>".$row['Employee_ID']."</td>";
    echo "<td>".$row['Manager_ID']."</td>";
    echo "<td>".$row['Name']."</td>";
    echo "<td>".$row['Client_ID']."</td>";
    echo "</tr>";
  }
  echo "</table>";

} else {
  echo "0 results";
}


    $sql4="SELECT * FROM Clients";
    $result = mysqli_query($conn, $sql4);

if (mysqli_num_rows($result) > 0) {

  echo "<br/>";
  echo "<h2>Here are the current clients</h2>";
  // output data of each row in a table
  echo "<table border='1'>
        <th>Client ID</th>
        <th>Last Name</th>
        <th>Address</th>
        <th>City</th>
        <th>State</th>
        <th>Zip</th>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>".$row['Client_ID']."</td>";
    echo "<td>".$row['Last_Name']."</td>";
    echo "<td>".$row['Address']."</td>";
    echo "<td>".$row['City']."</td>";
    echo "<td>".$row['State']."</td>";
    echo "<td>".$row['Zip']."</td>";
    echo "</tr>";
  }
  echo "</table>";

} else {
  echo "0 results";
}

    $conn->close();
 echo "<br/>";
 echo "<hr/>Last Modified: ".strftime('%a, %b %d, %Y at %I:%M %p',filemtime($_SERVER['SCRIPT_FILENAME']));
 ?>

</body>
</html>

