//Larry Baucum
//11/3/22
//This program will get fahrenheit from the user and ouput it in celsius

//Import scanner
import java.util.*;


//Controlling class
public class w2c2 {

    //Main method
    public static void main(String[] args){

        //Declare variables
        Scanner input = new Scanner(System.in);
        Double fahrenheit;
        Double celsius;

        //Initialize variables
        System.out.println("Enter your fahrenheit please ");

        fahrenheit = input.nextDouble();

        celsius = (fahrenheit -32)  *(5.0/9.0);

        //Output temp in celsius 
        System.out.println("Your temperature in fahrenheit is "+fahrenheit+ ("and in celsius is " +celsius));

        input.close();  

    }
    
}
