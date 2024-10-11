//Larry Baucum
//12/1/22
//Description: Do while loop practice


import java.util.*;


public class wk6cw3 {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        String user;
        String pass;


        try{//beign try

            //Do while loop to ask for a users username and password until it meets the set conditions
            do{

                System.out.println("Enter a username greater than 8 characters: ");
                user = input.next();
                System.out.println("Enter a password that is different from your username: ");
                pass = input.next();

            }

            while(user.compareToIgnoreCase(pass) ==0 || pass.length() <8);

            System.out.println("Your username and password is valid!!");


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
