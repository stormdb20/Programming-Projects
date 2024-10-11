//Larry Baucum
//11/14/22
//This program will take a users order of pizza and soda and output the order and price before and after tax



import java.util.*;

public class Test1Pizza {
    
    //Instaiate global variables for item prices and tax
    public static double pizza = 1.99;
    public static double soda = 1.25;
    public static double tax = 0.05;

    public static void main(String [] args){
        //Declare variables
            Scanner input = new Scanner(System.in);
            String name;
            String order_name;
            int slices;
            int drinks;
            double t1;
            double t2;
            double total;
            double addtax;
            double rounded;
            
            //Prompt user for their name and their order name
            System.out.println("Hello what is your name? ");
            name = input.nextLine();
            System.out.println("Welcome to our pizzaria "+name);
            
            System.out.println("May we have a name for your order ");
            order_name = input.nextLine();
            
            //Prompt user for item quantities
            System.out.println("Enter how many slices of pizza you want: ");
            slices = input.nextInt();
            System.out.println("Enter how many sodas you want: ");
            drinks = input.nextInt();
        
            //Calculate total, individual item prices, and tax
            t1 = slices*pizza;
            t2 = drinks*soda;
    
            total = (t1+t2);
            addtax = total*tax;
            rounded = (total+addtax);
            //Print my order and totals with and without tax
            System.out.println("Confirming your order for "+order_name);
            System.out.println("Pizza: "+slices);
            System.out.println("Soda: "+drinks);
            System.out.println("Your total before tax is "+total);
            System.out.printf("Your total after tax is %.2f",rounded);

    input.close();  

}
}
