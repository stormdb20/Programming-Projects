<?php

function espressos(){	
    $espresso = $_REQUEST["expresso"]; 
    $size = $_POST["size"];
    $sales = 0;
    echo "<br/>";
    echo 'Your Espresso information is:' . '<br/>';
    echo "<br/>";
    
    if ($espresso == "caffelatte"){
        
        
        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall Caffe Latte $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande Caffe Latte $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Caffe Latte $4.15' . '<br/>';}}

    else if ($espresso == "caramellatte"){
        
        if ($size == "tall")
            {$sales = 2.95;
                echo 'You selected a Tall Caramel Latte $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
                echo 'You selected a Grande Caramel Latte $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Caramel Latte $4.15' . '<br/>';}}

    else if ($espresso == "cappuccino"){
        
        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall Cappuccino $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande Cappuccino $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Cappuccino $4.15' . '<br/>';}}

    else if ($espresso == "caramelmacchiato"){

        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall Caramel Macchiato $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande Caramel Macchiato $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Caramel Macchiato $4.15' . '<br/>';}}

    else if ($espresso == "cafemocha"){

        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall Cafe Mocha $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande Cafe Mocha $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Cafe Mocha $4.15' . '<br/>';}}

    else if ($espresso == "whitechocmocha"){
    
        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall White Choclate Mocha $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande White Choclate Mocha $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti White Choclate Mocha $4.15' . '<br/>';}}

    else if ($espresso == "caffeamericano"){
        
        if ($size == "tall")
            {$sales = 2.95;
            echo 'You selected a Tall Cafe Americano $2.95' . '<br/>';}
        else if ($size == "grande")
            {$sales = 3.65;
            echo 'You selected a Grande Cafe Americano $3.65' . '<br/>';}
        else if ($size == "venti")
            {$sales = 4.15;
            echo 'You selected a Venti Cafe Americano $4.15' . '<br/>';} }

    else if ($espresso == "espresso"){
        
        if ($size == "solo")
            {$sales = 1.75;
            echo 'You selected a Solo Espresso $1.75' . '<br/>';}
            
        else if ($size == "double")
            {$sales = 1.95;
            echo 'You selected a Double Espresso $1.95' . '<br/>';} }
    
    return $sales;
        }



    function drink(){ 
        $drinks = $_REQUEST["drinks"]; 
        $size2 = $_POST["size2"];
        $sales = 0;
        echo "<br/>";
        echo 'Your drink information is:' . '<br/>';
        echo "<br/>";

        if ($drinks == "freshbrewedcoffee"){
            
            if ($size2 == "tall")
                {$sales = 1.85;
                echo 'You selected a Tall Fresh brewed Coffee $1.85' . '<br/>';}
            else if ($size2 == "grande")
                {$sales = 2.10;
                echo 'You selected a Grande Fresh brewed Coffee $2.10' . '<br/>';}
            else if ($size2 == "venti")
                {$sales = 2.45;
                echo 'You selected a Venti Fresh brewed Coffee $2.45' . '<br/>';}}
                
        else if ($drinks == "chaitealatte"){
            
            if ($size2 == "tall")
                {$sales = 3.65;
                echo 'You selected a Tall Chai Tea Latte $3.65' . '<br/>';}
            else if ($size2 == "grande")
                {$sales = 4.25;
                echo 'You selected a Grande Chai Tea Latte $4.25' . '<br/>';}
            else if ($size2 == "venti")
                {$sales = 4.65;
                echo 'You selected a Venti Chai Tea Latte $4.65' . '<br/>';}}
                
        else if ($drinks == "brewedhottea"){
            
            if ($size2 == "tall")
                {$sales = 1.95;
                echo 'You selected a Tall Brewed Hot Tea $1.95' . '<br/>';}
            else if ($size2 == "grande")
                {$sales = 2.15;
                echo 'You selected a Grande Brewed Hot Tea $2.15' . '<br/>';}
            else if ($size2 == "venti")
                {$sales = 2.45;
                echo 'You selected a Venti Brewed Hot Tea $2.45' . '<br/>';}}
                
        else if ($drinks == "hotchocolate"){
            
            if ($size2 == "tall")
                {$sales = 2.75;
                echo 'You selected a Tall Hot Chocolate $2.75' . '<br/>';}
            else if ($size2 == "grande")
                {$sales = 3.25;
                echo 'You selected a Grande Hot Chocolate $3.25' . '<br/>';}
            else if ($size2 == "venti")
                {$sales = 3.45;
                echo 'You selected a Venti Hot Chocolate $3.45' . '<br/>';}}
    
        else if ($drinks == "whitehotchocolate"){
            
            if ($size2 == "tall")
                {$sales = 2.75;
                echo 'You selected a Tall White Chocolate $2.75' . '<br/>';}
            else if ($size2 == "grande")
                {$sales = 3.25;
                echo 'You selected a Grande White Chocolate $3.25' . '<br/>';}
            else if ($size2 == "venti")
                {$sales = 3.45;
                echo 'You selected a Venti White Chocolate $3.45' . '<br/>';}}
    
    
        return $sales;
        }



    function ex(){
        
        $addex=0; 
        echo "<br/>";
        echo 'Your extras information is:'.'<br/>';
        echo "<br/>";
        
        if(isset($_POST["flavorshot"]) )	{
			$addex += 0.50;
            echo "You chose to add flavor shot as an extra $0.50 <br/>";
		}

        if(isset($_POST["addespressoshot"]) )	{
			$addex += 0.59;
            echo "You chose to add expresso shot as an extra $0.59 <br/>";
		}

        if(isset($_POST["soyalmondmilk"]) )	{
			$addex += 0.50;
            echo "You chose to add soy almond milk as an extra $0.50 <br/>";
		}
    
        return $addex;
    }

function payinfo(){ 
    
    $paytype = $_REQUEST["pay"];

    //if(isset($_POST["credit"]) )	{
    if ($paytype == "credit"){
            //Get form data values
            $n = $_POST["name"];
            $cnum = $_POST["cardnum"];
            $exp = $_POST["expdate"];
            $cv = $_POST["cvcode"];

            echo "<br/>";
            echo "Your Credit Card information is: <br/>";
            echo "<br/>";
            echo 'Your name is: ' . $n . '<br/>';
            echo 'Your credit card number is: ' . $cnum . '<br/>';
            echo "Your credit card expiration date is: " . $exp . '<br/>';
            echo "Your credit card cv code is: " . $cv . '<br/>';
    
        
        }

    //if(isset($_POST["bsuflex"]) )	{
    else if ($paytype == "bsuflex") {
    //Get form data values 

        $n = $_POST["name"];
        $be = $_POST["bsuemail"];
        $bid = $_POST["bsuid"]; 
        
        echo "<br/>";
        echo "Your BSU Flex information is: <br/>";
        echo "<br/>";
        echo "Your name is: " . $n . '<br/>';
        echo "Your email is: " . $be . '<br/>';
        echo "Your id is: " . $bid . '<br/>';
    
    
    }
    }






//if($_SERVER['REQUEST_METHOD']=='POST')
if(isset($_POST['submit']))
{


    $pe = espressos();    
    $pd = drink();
    $e = ex();
    $subtotal = ($pd + $pe + $e);
    $tax = $subtotal * .06;
    $total =  $subtotal + $tax;
    echo "<br/>";
    echo payinfo();
    echo "<br/>";
    echo "Here is what you owe: <br/>";
    echo "<br/>";
    echo 'Your subtotal is ' . $subtotal . '<br/>';
    echo 'Your tax is ' . $tax . '<br/>';
    echo 'Your total is ' . $total . '<br/>';



}
echo "<hr/>Last Modified: ".strftime('%a, %b %d, %Y at %I:%M %p',filemtime($_SERVER['SCRIPT_FILENAME']));