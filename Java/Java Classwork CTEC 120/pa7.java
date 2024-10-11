//Larry Baucum
//12/13/22
//Time conversion program using user defined methods


import java.util.*;

public class pa7 {//begin class

    static Scanner input = new Scanner(System.in);

    public static void main(String[] args){

        int options;
        double hrs;
        double days;
        double mins;
        double hours;

        try{//start try

    System.out.println("Select a conversion type");
                System.out.println("1. Hours to minutes");
                System.out.println("2. Days to hours");
                System.out.println("3. Minutes to hours");
                System.out.println("4. Hours to days");

                options = input.nextInt();

                switch (options){//begin switch

                    case 1:
                    System.out.println("Enter the amount of hours you want to turn into minutes");
                    hrs = input.nextDouble();
                    System.out.println(hrs+" Hours is "+htm(hrs)+" minutes");
                    break;

                    case 2:
                    System.out.println("Enter the amount of days you want to turn into hours");
                    days = input.nextDouble();
                    System.out.println(days+" Days is "+dth(days)+" hours");
                    break;

                    case 3:
                    System.out.println("Enter the amount of minutes you want to turn into hours");
                    mins = input.nextDouble();
                    System.out.println(mins+" Minutes is "+mth(mins)+" hours");
                    break;

                    case 4:
                    System.out.println("Enter the amount of hours you want to turn into days");
                    hours = input.nextDouble();
                    System.out.println(hours+" Hours is "+htd(hours)+" days");

                }//end switch

            }//end try


                catch (InputMismatchException imeRef){

                    System.out.println("Invalid input, Please try again!!!");
                }
                
                catch (ArithmeticException aeRef){
                
                    System.out.println("Invalid arithmetic, Please try again!!!");
                } 
                
            }//end main

            //method to calculate minutes from minutes
            public static double htm(double hrs){

                return hrs*60;
            }
            //method to calculate hours from days
            public static double dth(double days){

                return days*24;
            }
            //method to calculate hours from minutes
            public static double mth(double mins){

                return mins/60;
            }
            //method to calculate days from hours
            public static double htd(double hours){

                return hours/24;
            }




    
}//end class
