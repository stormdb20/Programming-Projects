//Larry Baucum
//11/11/22
//Testing user defined methods by determining if a number is even or odd

import java.util.*;



public class w7cw2 {

    static Scanner input = new Scanner(System.in);


    public static void main(String[] args){//begin main

        int user_num;

        System.out.println("Enter a number to see if it's even or odd ");

        user_num = input.nextInt();

        System.out.println("Your number is "+oddeven(user_num));


    }//end main


    public static String oddeven(int number){//begin oddeven

        if (number%2 == 1)
            return "Odd";
        else
            return "Even";

    }//end oddeven
    
}
