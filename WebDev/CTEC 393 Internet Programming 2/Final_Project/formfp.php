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
$cost = $_POST['Cost'];
$regex = '/\$\d{3}/';
//$J_ID = $_POST['Job_ID'];
//$regex_digits = '/^\d{4}$/';
//$S_Name = $_POST['Service_Name'];
//$regex_letter_cap = '/^[a-zA-Z]{0,10}$/';

if (preg_match($regex, $cost)) {

$sql = "INSERT INTO Jobs (Job_ID, Cost, Service_Name) VALUES ('".$_POST['Job_ID']."', '".$_POST['Cost']."',  '".$_POST['Service_Name']."')";

if ($conn->query($sql) === TRUE) {

    header("Location: confirmfp.html");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;

}
}
else {

        echo "Your entry is invalid. <br/> 
        Please click the back button in your browser to return to the form. <br/> 
        Please refer to the parentheses beside the fields. <br/>";
    
    }

$conn->close();

echo "<hr/>Last Modified: ".strftime('%a, %b %d, %Y at %I:%M %p',filemtime($_SERVER['SCRIPT_FILENAME']));