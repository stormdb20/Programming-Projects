//Larry Baucum
//12/14/22
//Program to take a name and two numbers. Returns name length and true/false if number is even or odd

import java.util.*;

public class FinalpA {

    static Scanner input = new Scanner(System.in);
    public static void main(String[] args){//Start main

        String name;
        int num1;
        int num2;

try{//Start try

            System.out.println("Please enter your name and we will tell you it's length:");
            name = input.nextLine();

            System.out.println(name+" the length of your name is "+namelen(name));

            System.out.println("Please enter your first positive number:");
            num1 = input.nextInt();

            System.out.println("Please enter your second positive number:");
            num2 = input.nextInt();

            System.out.println("The product of your two numbers is "+product(num1,num2));


        }//end try

        catch (InputMismatchException imeRef){

            System.out.println("Invalid input, Please try again!!!");
        }
        
        catch (ArithmeticException aeRef){
        
            System.out.println("Invalid arithmetic, Please try again!!!");
        }  

    }//End main


  

    public static int namelen(String name){//start name length method

        int len;
        len = name.length();
        return len;

    }//end name length method


    public static String product(int num1, int num2){//start even/odd product method

        int product;

        product = num1*num2;
        
        if (product%2 == 1)
            return "odd making it False";
        else
            return "even making it True";

    }//end even/odd product method

    
}//end class
