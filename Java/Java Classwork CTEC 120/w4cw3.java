//Larry Baucum
//11/18/22
//Secure program to prompt user for information to find out voter eligibility


import java.util.*;

public class w4cw3 {


    public static void main(String[] args)
    {

        Scanner input = new Scanner(System.in);
        int age;


try{

    System.out.println("Enter your age for voting eligibility ");
    age = input.nextInt();

    if (age < 18){

        System.out.println("You aren't eligible to vote. ");

    }
    else{

        System.out.println("You are eligible to vote! ");
    }



}//end try
catch (InputMismatchException imeRef){//start catch

    System.out.println(" Invalid age entry!!");

} //end catch          
System.out.println("Your program is a smooth operator");  
input.close();    
}//end of main
    
}//end of class
