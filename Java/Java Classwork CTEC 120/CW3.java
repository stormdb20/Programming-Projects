// Larry Baucum
// 10/28/2022
// This program will store my variables and print them
public class CW3{	
public static void main(String[] args) {
		// Declare variables 
		String name1;
		String name2;
		int num1;
		double num2;
		String welcome;
        double sum;
        double product;
        double avg;

		
		
		//Initialize variables
		name1 = "Larry";
		name2 = "Baucum";
		num1 = 7;
		num2 = 6.5;
		sum = num1 + num2;
        product = num1 * num2;
        avg = sum/2;
        welcome = "Welcome to friday's class";

		
		//Print my variables with a message
		System.out.println("My first name is " +name1);
		System.out.println("My last name is " +name2);
		System.out.println("The product is " +product);
		System.out.println("The sum is " +sum);
		System.out.println("The average is " +avg);
		System.out.println(welcome);

	}
}
