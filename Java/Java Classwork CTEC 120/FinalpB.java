//Larry Baucum
//12/14/22
//FInal exam part B program that displays the french word for numbers 11-20



public class FinalpB {

    public static void main(String[] args){//begin main method

        int i;


try{//start try
        
        for (i = 11; i <= 20; i++){// to call my method 10 times

            System.out.println("The number "+i+" in French is "+ConverttoFrench(i));


        }

        
    }//end try

    catch (ArithmeticException imeRef){

        System.out.println("Invalid arithmetic, Please try again!!!");
    }


    }//end main method



    public static String ConverttoFrench(int x){//start translate method

        if (x==11)
            return "Onze";

        else if (x==12)
            return "Douze";

        else if (x==13)
            return "Treize";

        else if (x==14)
            return "Quatorze";

        else if (x==15)
            return "Quinze";
        
        else if (x==16)
            return "Seize";

        else if (x==17)
            return "Dix-sept";

        else if (x==18)
            return "Dix-huit";

        else if (x==19)
            return "Dix-neuf";

        else 
            return "Vingt";

    }//end converttoespanol method
    
}//end class
