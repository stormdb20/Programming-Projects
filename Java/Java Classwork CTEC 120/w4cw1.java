//Larry Baucum
//11/20/22
//Read in data from a file

import java.util.*;
import java.io.*;

public class w4cw1 {

    public static void main(String[] args)
            //Throw a file not found exception if necessary
            throws FileNotFoundException
    
    {
// Declare variables and I/O streams 
        Scanner inFile = new Scanner(new FileReader("C:\\Users\\larry\\OneDrive\\Desktop\\ctec-120-102\\Classwork\\ncw1.txt"));

        PrintWriter outFile =new PrintWriter("C:\\Users\\larry\\OneDrive\\Desktop\\ctec-120-102\\Classwork\\ocw1.txt");

        String name1;
        String name2;
        int age;
        double height;

        
        
        name1 = inFile.next();
        name2 = inFile.next();
        age = inFile.nextInt();
        height = inFile.nextDouble();

        //Output data to outfile
        outFile.println("My first name in my file is "+name1);
        outFile.println("My last name in my file is "+name2);
        outFile.println("My age in my file is "+age);
        outFile.println("My height in my file is "+height);

        //Close I/O streams
        inFile.close();
        outFile.close();

    }

    
}
