//Larry Baucum
//11/6/22
//Description: Testing predefined methods

import java.util.*;
import static java.lang.Math.*;



public class wk7cw1 {


    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        int num1;
        int num2;

        try{

            System.out.println("Enter your first number: ");
            num1 = input.nextInt();

            System.out.println("Enter your second number: ");
            num2 = input.nextInt();


            System.out.println("The maximum of your two numbers is "+Math.max(num1,num2));
            System.out.println("The minimum of your two numbers is "+Math.min(num1,num2));


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
