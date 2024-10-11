//Larry Baucum
//11/1/22
//This program will take input from the user and print with appropriate meassage

//import my scanner class
import java.util.*;

//controlling class
public class w2cw1 {

//main method
    public static void main(String[] args){

        //Declare variables
        Scanner input = new Scanner(System.in);
        String name1;
        String name2;
        String exp_grade;
        int age;
        double height;
        double num1;
        double num2;
        double sum;
       


        //Initialize variables
        System.out.println("Please enter your first name ");

        name1 = input.nextLine();

        System.out.println("Please enter your last name ");

        name2 = input.nextLine();

        System.out.println("Please enter your age ");

        age = input.nextInt();

        input.nextLine();
        
        System.out.println("Please enter your expected grade ");

        exp_grade = input.nextLine();
        
        System.out.println("Please enter your height ");

        height = input.nextDouble();


        System.out.println("Please enter your first number ");

        num1 = input.nextDouble();

        System.out.println("Please enter your second number ");

        num2 = input.nextDouble();

        sum = num1+num2;
        
        

        // Print the user input with message
        System.out.println("Your first name is " +name1);
        System.out.println("Your last name is " +name2);
        System.out.println("Your age is " +age);
        System.out.println("Your height is " +height);
        System.out.println("Your expected grade is " +exp_grade);
        System.out.println("Your first number is " +num1);
        System.out.println("Your second number is " +num2);
        System.out.println("Your sum is " +sum);
        System.out.println("Your average is " +sum/2);
        

        input.close();  

    }

    
}