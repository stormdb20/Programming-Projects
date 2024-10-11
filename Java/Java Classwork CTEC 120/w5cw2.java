//Larry Baucum
//11/27/22
// Classwork 2 of week 5 carwash using switch


import java.util.*;

public class w5cw2 {


    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String u_reply;
        String user;
        String pass;
        int options;



try{
        System.out.println("Please enter yes or no if this is your desired program ");
        u_reply = input.nextLine();

        if ((u_reply.compareTo("yes")==0)){//primary if begin


            System.out.println("Thank you for choosing our program!!");
            System.out.println("Make a username and password please.");
            
            System.out.println("Please enter your username: ");
            user = input.nextLine();

            System.out.println("Please enter your password that is not the same as your username and is long than 12 characters: ");
            pass = input.nextLine();

            if ((pass.length() > 12) && (user.compareToIgnoreCase(pass) !=0)){//secondary if begin

                System.out.println("The password you entered is valid!!");

                System.out.println("Please select a the wash you want!");
                System.out.println("1. Normal wash");
                System.out.println("2. Super wash");
                System.out.println("3. Ultimate wash");

                options = input.nextInt();

                switch (options){//begin switch

                    case 1:
                    System.out.println("Normal wash it is");
                    break;

                    case 2:
                    System.out.println("Super wash nice choice");
                    break;

                    case 3:
                    System.out.println("A customer of class I see, Ultimate wash coming right up");
                    break;

                    default:
                    System.out.println("Sorry we're a car wash not a bakery!");

                }//end switch




            }//secondary if end

            else{
                System.out.println("Your password is invalid!");
            }//secondary else end
            

        }//primary if end

        else{//begin primary else

            System.out.println("See you next time!");
                }//end primary else 
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
