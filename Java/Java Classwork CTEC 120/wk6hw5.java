//Larry Baucum
//12/1/22
//Description: Factorial program


import java.util.*;


public class wk6hw5 {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        int num;
        int count;


        try{//beign try
     
                System.out.println("Enter a number you want to be factorialized: ");
                num = input.nextInt();

                count = num;
//Loop to decrement the number and multiply the numbers sequentially
            while(num > 1){
            
            count = (count * (num-1));
            
            
            num = num-1;

            }

            System.out.println("Your factorial is "+count);

            



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
