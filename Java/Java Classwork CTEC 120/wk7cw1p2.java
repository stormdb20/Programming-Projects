//Larry Baucum
//11/6/22
//Description: Testing predefined methods for exponents

import java.util.*;
import static java.lang.Math.*;



public class wk7cw1p2 {


    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        int base;
        int exp;

        try{

            System.out.println("Enter your base number: ");
            base = input.nextInt();

            System.out.println("Enter your exponent number: ");
            exp = input.nextInt();


            System.out.println("The base of your two numbers is "+Math.max(base,exp));
            System.out.println("The exponent of your two numbers is "+Math.min(base,exp));
            System.out.println("The result of your exponent is "+Math.pow(base,exp));


        }

        catch (InputMismatchException imeRef){

            System.out.println("Invalid input, Please try again!!!");
        }
    
        catch (ArithmeticException imeRef){
    
            System.out.println("Invalid arithmetic, Please try again!!!");
        }

    input.close();

    }//end main
    
}//end class
