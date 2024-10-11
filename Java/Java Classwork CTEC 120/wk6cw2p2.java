//Larry Baucum
//12/1/22
//Description: COunt controlled for loop practice 
import java.io.*;
import java.util.*;



public class wk6cw2p2 {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        int stop;
        int num;

        
    try{//begin try
        System.out.println("Enter how many numbers you want to test: ");
        stop = input.nextInt();


        for(int i = 0; i < stop; i++){

            System.out.println("Enter a number to test if it's positive, negative, or zero ");
            num = input.nextInt();

            if (num > 0)
            System.out.println("Your number is positive");
            if (num < 0)
            System.out.println("Your number is negative");
            if (num == 0)
            System.out.println("Your number is zero");

        }//end loop
    }//end try
    
    catch (InputMismatchException imeRef){

        System.out.println("Invalid input, Please try again!!!");
    }
    
    catch (ArithmeticException aeRef){
    
        System.out.println("Invalid arithmetic, Please try again!!!");
    }

    input.close();  
    }//end main
    
}//end class
