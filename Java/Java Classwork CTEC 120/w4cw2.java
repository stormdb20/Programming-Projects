//Larry Baucum
//11/17/22
//Try and catch demonstration

import java.util.*;

public class w4cw2{

    public static void main(String [] args){


        Scanner input = new Scanner(System.in);
        double num1;
        double num2;
        double sum;
        double division;

        //Secure the code 
try{//start try

        System.out.println("Eneter number: ");
        num1 = input.nextDouble();

        System.out.println("Eneter number: ");
        num2 = input.nextDouble();

        sum = num1+num2;
        division = num1/num2;

        System.out.println("The sum of your numbers is "+sum);
        System.out.println("The division of your numbers is "+division);
}//End try

catch (InputMismatchException imeRef){

    System.out.println(" Hello Larry here! You entered an invalid value!!");

}            
System.out.println("Your program is a smooth operator");

input.close();
        

    }//End main 

}//End class