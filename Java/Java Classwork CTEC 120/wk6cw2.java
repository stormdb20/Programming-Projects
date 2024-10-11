//Larry Baucum
//12/1/22
//Description: Read in data  from file and output to a file

import java.io.*;
import java.util.*;


public class wk6cw2 {

    public static void main(String[] args)
    
    throws FileNotFoundException
    {

        String name1;
        String name2;
        int age;
        double height;
        
        Scanner inFile = new Scanner(new FileReader("C:\\Users\\larry\\OneDrive\\Desktop\\ctec-120-102\\Classwork\\employees.txt"));
        PrintWriter outfile = new PrintWriter("C:\\Users\\larry\\OneDrive\\Desktop\\ctec-120-102\\Classwork\\employeesoutputfile.txt");


        while(inFile.hasNext()){

            name1 = inFile.next();
            name2 = inFile.next();
            age = inFile.nextInt();
            height = inFile.nextDouble();

            outfile.println("Your first name is "+name1);
            outfile.println("Your last name is "+name2);
            outfile.println("Your age is "+age);
            outfile.println("Your height is "+height);
        }


        inFile.close();
outfile.close();
        


    }//end main
    
}//end class
