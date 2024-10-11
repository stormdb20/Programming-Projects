//Larry Baucum
//11/10/22
//This program will calculate the total price of butter, milk, and bread

import java.util.*;

public class w3cw3 {
    //Instaiate global variables for item prices
    public static double bread = 2.67;
    public static double milk = 4.50;
    public static double butter = 2.89;

    public static void main(String [] args){
    //Declare variables
        Scanner input = new Scanner(System.in);
        int bread_amt;
        int milk_amt;
        int butter_amt;
        double t1;
        double t2;
        double t3;
        double total;
        //Prompt user for item quantities
        System.out.println("Enter amount of bread ");
        bread_amt = input.nextInt();
        System.out.println("Enter amount of milk ");
        milk_amt = input.nextInt();
        System.out.println("Enter amount of butter ");
        butter_amt = input.nextInt();
        //Calculate total and individual item prices
        t1 = bread_amt*bread;
        t2 = milk_amt*milk;
        t3 = butter_amt*butter;

        total = (t1+t2+t3);
        //Print my total
        System.out.println("Your total is "+total);
        System.out.printf("Your total rounded to two deciaml places is %.2f",total);



        input.close();  


    }
    
}
