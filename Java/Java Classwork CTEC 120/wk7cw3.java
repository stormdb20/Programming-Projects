//Larry Baucum
//12/9/22
//This program will convert english numbers to spanish




public class wk7cw3 {

    public static void main(String[] args){//begin main method

        int i;



        Hello();

        for (i = 1; i <= 10; i++){// to call my method 10 times

            System.out.println("The number "+i+" in spanish is "+ConverttoEspanol(i));


        }

        Goodbye();



    }//end main method

    //Create method 
    //Body, return type, parameters

    public static String ConverttoEspanol(int x){

        if (x==1)
            return "Uno";

        else if (x==2)
            return "Dos";

        else if (x==3)
            return "Tres";

        else if (x==4)
            return "Cuatro";

        else if (x==5)
            return "Cinco";
        
        else if (x==6)
            return "Seis";

        else if (x==7)
            return "Siete";

        else if (x==8)
            return "Ocho";

        else if (x==9)
            return "Nueve";

        else if (x==10)
            return "Diez";

        else return "Invalid";
    }//end converttoespanol method

    public static void Hello(){

        System.out.println("Hello and welcome to our program");
    }

    public static void Goodbye(){

        System.out.println("Goodbye and thank you for using our program");
    }



    
}//end class
