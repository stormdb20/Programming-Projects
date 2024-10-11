//Larry  Baucum
//11/4/22
//This program will take orders including burgers, fires, and sodas and output the price before and after tax

//import my scanner class 
import java.util.*;

//control method
public class w2cw3
{
	
	
	
	public static void main(String[] args) {
		
		//Input stream 
	    Scanner input = new Scanner(System.in);
		
		//declare global variables
		final double burger = 1.69;
		final double fries = 1.09;
		final double soda = .99;
		
		//local variables
		String name;
		String area;
		int burger_amt;
		int fries_amt;
		int soda_amt;
		double pre_total;
		double tax;
		double post_total;
		
		//Initialize variables and get inputs
		System.out.println("Hello and welcome to Cookout ");
		
		System.out.println("Please enter your name ");
        name = input.nextLine();
        
        System.out.println("Please enter your area ");
        area = input.nextLine();
        
        System.out.println("Please enter how many burgers you want ");
        burger_amt = input.nextInt();
        
        System.out.println("Please enter how many fry orders you want ");
        fries_amt = input.nextInt();
        
        System.out.println("Please enter how many sodas you want ");
        soda_amt = input.nextInt();
        
        pre_total = (burger_amt*burger) + (fries_amt*fries) + (soda_amt*soda);
        tax = .065;
        post_total = (pre_total * .065) + pre_total;
        
        //Output 
        System.out.println(name+ " your total before tax is " +pre_total);
        System.out.println(name+ " your tax is " +tax);
        System.out.println(name+ " your total after tax is " +post_total);
        
        
    input.close();  
        
        
	}
}