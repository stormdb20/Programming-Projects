//Larry Baucum
//11/26/22
//

import java.util.*;

public class w5cw1 {

    Scanner input = new Scanner(System.in);

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        String user_ans;
        String user_state;
        int age;

        try{//begin try
        
        //Prompt user to see if they want to use the program
        System.out.println("Please enter yes or no if this is your desired program ");
        user_ans = input.nextLine();

        if ((user_ans.compareTo("yes")==0)){

            System.out.println("Thank you for choosing our program!!");
            System.out.println("You must be at least 18 and be a maryland resident to vote in maryland.");
            
            System.out.println("Please enter your age: ");
            age = input.nextInt();

            input.nextLine();
            System.out.println("Please enter your home state: ");

            user_state = input.nextLine();

            if ((age >= 18) && (user_state.compareToIgnoreCase("Maryland")==0)){

                System.out.println("You may vote in Maryland!!");


            }

            else{
                System.out.println("You may not vote in Maryland!");
            }






        }

        else{

            System.out.println("See you next time!");
        }


    }//end try

    catch (InputMismatchException imeRef){

        System.out.println("Invalid input, Please try again!!!");
    }

    catch (ArithmeticException imeRef){

        System.out.println("Invalid arithmetic, Please try again!!!");
    }

        
    input.close();  


    }//End main
    
}//End class
