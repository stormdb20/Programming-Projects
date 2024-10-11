
<?php

//echo "Please enter a password with the following criteria: <br/>";
//echo "At least 12-20 characters in length, with a combination of uppercase letters, lowercase letters, numbers, and symbols <br/>";


if (isset ($_POST["submit"])) {

    $pass = $_POST["pass"];
    $passreqs = '/^(?=.*[!@#$%^&*-])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{12,20}$/';

    if (empty ($_POST["pass"])) {  
        echo "Password is empty , Please enter a password <br/>";  
    }

    if (preg_match($passreqs, $pass)) {

        echo "Your password meets our criteria <br/>";
        echo "Your password is: " . $pass . "<br/>";

        $hashpass = hash('sha256', $pass);
        echo "Your SHA256 hashed password has a length of 64 and looks like this: " . $hashpass . "<br/>";

        $hashpass2 = hash('md5', $pass);
        echo "Your MD5 hashed password has a length of 32 and looks like this: " . $hashpass2 . "<br/>";

        $hashpass3 = hash('sha512', $pass);
        echo "Your SHA512 hashed password has a length of 128 and looks like this: " . $hashpass3 . "<br/>";
        
        echo "I believe SHA256 is the most secure as it is recommended by NIST. <br/> 
        It is used for tokenization, cryptocurrency transactions, password hashing, and integrity checks for files and software. <br/>";


    } 
    
    else {

        echo "Your password does not meet our criteria <br/>";
    }







    
    





}
















echo "<hr/>Last Modified: ".strftime('%a, %b %d, %Y at %I:%M %p',filemtime($_SERVER['SCRIPT_FILENAME']));