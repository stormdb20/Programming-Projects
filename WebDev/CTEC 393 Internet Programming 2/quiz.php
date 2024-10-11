<?php

$subtotal = (float)0;
function items($subtotal){

    $choice1 = $_POST['chips'];
    $choice2 = $_POST['cookies'];
    $choice3 = $_POST['milk'];
    $choice4 = $_POST['eggs'];
    $choice5 = $_POST['butter'];
    $quantity1 =  (float)$_REQUEST['chipsq'];
    $quantity2 =  (float)$_REQUEST['cookiesq'];
    $quantity3 =  (float)$_REQUEST['milkq'];
    $quantity4 =  (float)$_REQUEST['eggsq'];
    $quantity5 =  (float)$_REQUEST['butterq'];

    $price = (float)0;

    if ($quantity1 != 0 )
    {

        echo "Your item is      " . $choice1." " . "You chose this amount:     " . $quantity1 ." ";
        $price = $price + ((float)$quantity1 * 0.50); 
    }

    if ($quantity2 != 0 )
    {

        echo "Your item is     " . $choice2." " . "You chose this amount:     " .  $quantity2." ";
        $price = $price + ((float)$quantity2 * 1.00);
    }

    if ($quantity1 != 0 )
    {

        echo "Your item is     " . $choice3." " . "You chose this amount:     " . $quantity3." ";
        $price = $price + ((float)$quantity3 * 2.00);
    }

    if ($quantity1 != 0 )
    {

        echo "Your item is    " . $choice4." " . "You chose this amount:    " . $quantity4." ";
        $price = $price + ((float)$quantity4 * 3.00);
    }

    if ($quantity1 != 0 )
    {

        echo "Your item is     " . $choice5." " . "You chose this amount:      " . $quantity5." ";
        $price = $price + ((int)$quantity5 * 1.50);
    }

    $subtotal = (float)$price;

return $subtotal;
}

function payinfo(){

    $n = $_POST["name"];
    $e = $_POST["email"];
    $ba = $_POST["address"]; 
    $cnum = $_POST["cnum"]; 
    $cv = $_POST["cvcode"];
    $exp = $_POST["expdate"]; 

    echo "Your name is    " . $n." ";
    echo "Your email is     " . $e." ";
    echo "Your billing address is     " . $ba." ";
    echo "Your credit card number is     " . $cnum." ";
    echo "Your cv code is    " . $cv." ";
    echo "Your expiration date is     " . $exp." ";

}













if($_SERVER['REQUEST_METHOD']=='POST')
{
    items($subtotal);
    payinfo();
    echo "Your subtotal is   ".$subtotal."   ";
    $tax = (float).06 * $subtotal;
    $total = (float)$tax + $subtotal;
    echo "Your total is   ".$total."   ";


} 


echo "<hr/>Last Modified: ".strftime('%a, %b %d, %Y at %I:%M %p',filemtime($_SERVER['SCRIPT_FILENAME']));