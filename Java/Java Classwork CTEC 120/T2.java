//Larry Baucum
//12/5/22
// test 2 covid vaccine selecction program

//import scanner class
import java.util.*;

public class T2 {


    public static void main(String[] args){
        //declare variables
        Scanner input = new Scanner(System.in);

        String u_reply;
        String fname;
        String lname;
        int age;
        int zipcode;        
        int options;



try{//start try
    //welcome message and promt user     
    System.out.println("Hello and welcome would you like to use our covid vaccine application? ");
        u_reply = input.nextLine();
// if/else for program entry
        if ((u_reply.compareTo("yes")==0)){//primary if begin

//thank you welcome message and instructions
            System.out.println("Thank you for choosing our program!!");
            System.out.println("Please enter the following information when prompted");
            
            //prompt user for input
            System.out.println("Please enter your first name: ");
            fname = input.nextLine();

            System.out.println("Please enter your last name: ");
            lname = input.nextLine();

            System.out.println("Please enter your age: ");
            age = input.nextInt();

            System.out.println("Please enter your zipcode: ");
            zipcode = input.nextInt();
            
            //print users input
            System.out.println("Your first name is "+fname);
            System.out.println("Your last name is "+lname);
            System.out.println("Your age is "+age);
            System.out.println("Your zipcode is "+zipcode);
            
            //prompt user and print choices
            System.out.println("Please select the covid vaccine you want!");
            System.out.println("1. Pfizer-BioNTech");
            System.out.println("2. Moderna");
            System.out.println("3. Johnson & Johnson's");
            System.out.println("4. Other");

                options = input.nextInt();
                // if/else to enter the switch case or print invalid message
            if ((options < 5) && (options > 0)){//begin second if
                switch (options){//begin switch

                    case 1:
                    System.out.println("You have been vaccinated with the Pfizer-BioNTec vaccine and qualify for a booster shot!");
                    break;

                    case 2:
                    System.out.println("You have been vaccinated with the Moderna vaccine and qualify for a booster shot!");
                    break;

                    case 3:
                    System.out.println("You have been vaccinated with the Johnson & Johnson's vaccine and qualify for a booster shot!");
                    break;

                    case 4:
                    System.out.println("You have been vaccinated with a vaccine other than the Pfizer-BioNTech  Moderna  Johnson & Johnson's and may NOT qualify for a booster shot! ");
                    break;

                    default:
                    System.out.println("You did not select a valid choice!");
                }//end switch

                

                }//end second if

                else{
                    System.out.println("You did not select a valid choice!");
                }
            

        }//primary if end

        else{//begin primary else

            System.out.println("You chose no, goodbye and thank you for using our program!");
                }//end primary else 
}//end try
//catch for input and arithmetic exceptions

catch (InputMismatchException imeRef){

    System.out.println("Invalid input, Please try again!!!");
}

catch (ArithmeticException aeRef){

    System.out.println("Invalid arithmetic, Please try again!!!");
}    
//Close input stream
input.close();      
    }//end main
    
}//end class
