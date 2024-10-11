//Larry Baucum
//11/27/22
//This program tests looping simple tasks such as prompting the user and adding numbers


import java.util.*;



public class w5cw3 {


    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        double num;
        double sum = 0;
        int i = 0;
        int limit; //loop control 
        try{//begin try

            System.out.println("How many numbers do you want to enter ");
            limit = input.nextInt();

            while (i < limit){

            System.out.println("Please enter a number: ");
            num = input.nextDouble();

            sum = sum + num;

            i++; //increment loop control




            }

            System.out.println("The sum of all your numbers is "+sum);






        }//end try

        catch (InputMismatchException imeRef){

            System.out.println("Invalid input, Please try again!!!");
        }
        
        catch (ArithmeticException aeRef){
        
            System.out.println("Invalid arithmetic, Please try again!!!");
        }
        input.close();  
    }
    
}
