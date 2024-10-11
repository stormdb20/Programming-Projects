//Larry Baucum
//11/10/22
//This program will demostrate different uses of methods on strings

import java.util.*;

public class w3cw2 {

   public static void main(String [] args){

    //Declare variables for user input
    Scanner input = new Scanner(System.in);
    String statement;
    String str1;
    String str2;
    int index;

    //Prompt the user
    System.out.println("Enter a sentence");
    statement = input.nextLine();
    //initialize variables for substring, replace, and indexof methods
    str1 = statement.substring(0,4);
    str2 = statement.replace("o","p");

    index = statement.indexOf("o");
    //print my methods 
    System.out.println("The length of the statement is = "+statement.length());
    System.out.println("The character at index 4 is  "+statement.charAt(4));
    System.out.println("The index of the letter o is "+index);
    System.out.println("The letters from index zero to the last index are "+str1);
    System.out.println("Are your o's turning into p's "+str2);
    System.out.println("Uppercase statement looks like this "+statement.toUpperCase());
    input.close();  

   }
   
    


    





}
