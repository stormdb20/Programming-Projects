<!DOCTYPE html>
<html>
	
<head>
   <meta charset="utf-8">
   <title>Cookies Read</title>
</head>
<body>
<?php
//read the cookies that have been saved on client's computer/browser
foreach ($_COOKIE as $key=>$value)
  print("<p>$key: $value</p>");

?>

</body>
</html>