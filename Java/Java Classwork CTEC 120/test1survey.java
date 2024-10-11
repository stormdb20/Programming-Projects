//Larry Baucum
//11/14/22
//This program will ask students for input for a school survey

import java.util.*;

public class test1survey {


    public static void main(String [] args){

        //Declare my variables
        Scanner input = new Scanner(System.in);
        String fname;
        String lname;
        int age;
        String major;
        String feedback;

        //Prompt the user 
        System.out.println("Welcome to the college survey");

        System.out.println("Enter your first name ");
        fname = input.nextLine();

        System.out.println("Enter your last name ");
        lname = input.nextLine();

        System.out.println("Enter your age ");
        age = input.nextInt();
        input.nextLine();
        
        System.out.println("Enter your major ");
        major = input.nextLine();
       
        System.out.println("Please provide feedback on your major  ");
        feedback = input.nextLine();

        //Output the users input with message
        System.out.println("Confirmation of your information: ");
        System.out.println("Your first name is: "+fname);
        System.out.println("Your last name is: "+lname);
        System.out.println("Your age is: "+age);
        System.out.println("Your major is: "+major);
        System.out.println("Your feedback is: "+feedback);



        input.close();  







    }
    
}
