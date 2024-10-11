function salesestimate(){
    let val1 = espressos();
    let val2 = drink();
    let val3 = ex();
    let tax = ((val1 + val2 + val3) * 0.10) 
    let totaled = + (val1 + val2 + val3) + tax;

    document.getElementById("total").value=totaled.toFixed(2);
    document.getElementById("total").disabled = true;
}


function espressos(){
		
    let espresso = document.querySelector( 'input[name="expresso"]:checked').value;  
    let sales;
    let size;
    
    if (espresso == "caffelatte")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "caramellatte")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "cappuccino")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "caramelmacchiato")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "cafemocha")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "whitechocmocha")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;

    else if (espresso == "caffeamericano")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15; 

    else if (espresso == "espresso")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.95;
        else if (size == "grande")
            sales = 3.65;
        else if (size == "venti")
            sales = 4.15;


    return sales;
        }
    
function drink(){ 
    let drinks = document.querySelector( 'input[name="drinks"]:checked').value;
    let sales;
    let size;
    
    if (drinks == "freshbrewedcoffee")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 1.85;
        else if (size == "grande")
            sales = 2.10;
        else if (size == "venti")
            sales = 2.45;
            
    else if (drinks == "chaitealatte")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 3.65;
        else if (size == "grande")
            sales = 4.25;
        else if (size == "venti")
            sales = 4.65;
            
    else if (drinks == "brewedhottea")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 1.95;
        else if (size == "grande")
            sales = 2.15;
        else if (size == "venti")
            sales = 2.45;
            
    else if (drinks == "hotchocolate")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.75;
        else if (size == "grande")
            sales = 3.25;
        else if (size == "venti")
            sales = 3.45;

    else if (drinks == "whitehotchocolate")
        size = prompt("choose a size from tall/grande/venti")
        if (size == "tall")
            sales = 2.75;
        else if (size == "grande")
            sales = 3.25;
        else if (size == "venti")
            sales = 3.45;


    return sales;
    }

function ex(){
    let addex=0;  
    let checkboxes = document.querySelectorAll('input[name="extras"]:checked'); 
    let values = [];  
    let count = 0
        checkboxes.forEach((checkbox) => {  
            values.push(checkbox.value);
            if (checkbox.value == 'flavorshot')
                addex += 0.50, ++count;
            else if (checkbox.value == "addespressoshot")
                addex += 0.59, ++count;
            else if (checkbox.value == "soyalmondmilk")
                addex += 0.50, ++count;

                if (count > 2){
                    window.alert("You've selected more than four items.")
                    ex()
                }
        });

    return addex;
}
    
                

function payinfoc(){ 
    
    let paytypec = document.querySelectorAll('input[value="credit"]:checked');

    if (paytypec == "credit")
        prompt();
        prompt("Please enter your name: ");
        prompt("Please enter your cv code: ");
        prompt("Please enter your expiration date (mm/yy): ");
        prompt("Please enter your zipcode: ");
        
    }
        
function payinfob(){ 
        let paytypeb = document.querySelectorAll('input[value="bsuflex"]:checked');
        
        if (paytypeb == "bsuflex") 
            prompt();
            prompt("Please enter your name: ");
            prompt("Please enter your BSU ID: ");
            prompt("Please enter your BSU Email: ");
    }