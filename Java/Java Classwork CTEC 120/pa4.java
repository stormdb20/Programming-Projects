//Larry Baucum
//11/20/22
// This program will take grades from the user and output the precentage above 70%

import java.util.*;


public class pa4 {

    public static void main(String[] args){
//declare variables
        Scanner input = new Scanner(System.in);
        double grade;//grades above 70
        double amt;//amount of numbers
        int count; //hold loop control count 
        double percent; //calc percentage of grades above 70
        int num; //store current num


try
{
    //prompt user
    System.out.println("Enter how many grades you will enter ");
    amt = input.nextDouble();
//loop control counts
    count = 0;
    grade = 0;
    
//while loop to count grades above 70
    while(count < amt){

        System.out.println("Enter grade: ");
        num = input.nextInt();
        
        if (num > 70){
            grade++;
            count++;
        }
        else{
            count++;
        }
        
    }
    percent = grade/amt;
    //output data
    System.out.println("Grades above 70: "+grade);
    System.out.println("Amount of grades: "+amt);
    System.out.println("Your percentage of grades over 70 is %"+percent*100);

}//end try

catch (InputMismatchException imeRef){

    System.out.println(" Hello Larry here! You entered an invalid value!!");

}            

catch(ArithmeticException aeRef){
    System.out.println(" Hello Larry here! Your arithmetic logic is wrong!!");
}

System.out.println("Your program is a smooth operator");

input.close();  


    }//end main
    
}//end class
