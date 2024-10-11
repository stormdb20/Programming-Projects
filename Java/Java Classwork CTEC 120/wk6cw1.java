//Larry Baucum
//11/29/22
//


import java.util.*;


public class wk6cw1 {

    static Scanner input = new Scanner(System.in);
    static final int CONTROL = -999;

    public static void main(String[] args){

        
        int num;
        
        try{//beign try

            System.out.println("Enter a number to see if it is positive negative or zero ");
            num = input.nextInt();

            while (num != CONTROL){//end loop

                
                if (num < 0){

                    System.out.println("Your number is negative");
                    System.out.println("");
                }

                if (num > 0){

                    System.out.println("Your number is positive");
                    System.out.println("");
                }
                if (num == 0){

                    System.out.println("Your number is zero");
                    System.out.println("");
                }
                System.out.println("Enter another number or -999 to escape the number simulation");
                num = input.nextInt();


            }//end loop

            System.out.println("You've escaped the number simulation this time");

            


        }//end try

        catch (InputMismatchException imeRef){

            System.out.println("Invalid input, Please try again!!!");
        }
        
        catch (ArithmeticException aeRef){
        
            System.out.println("Invalid arithmetic, Please try again!!!");
        }


input.close();

    }//end class
    
}//end main
