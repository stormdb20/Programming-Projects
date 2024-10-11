<!DOCTYPE html>
<html>
	
<head>
   <meta charset="utf-8">
   <title>Cookies Saved</title>
</head>
<body>
<?php
//define 5 days--> 60 secs * 60 minutes * 24 hours * 5 days
define("FIVE_DAYS",60 * 60 * 24 * 5); 
//Get form data values
$name = $_POST["name"];
$email = $_POST["email"];
$color = $_POST["color"];

setcookie("name",$name,time()+FIVE_DAYS);
setcookie("email",$email,time()+FIVE_DAYS);
setcookie("color",$color,time()+FIVE_DAYS);

echo "The cookie has been set with the following data: <br/>";
echo "Name: " . $name . "<br/>";
echo "Email: " . $email . "<br/>";
echo "Favorite color: " . $color . "<br/>";

echo 'Click ' . '<a href="readCookies.php">here</a>' . ' to read the saved cookie.<br/>';
?>

</body>
</html>