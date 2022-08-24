public class function_overloading {
    public static void main(String args[])
    {
        Average av = new Average ();
        System.out.println("Average is: "+ av.average(10, 20, 30));
        System.out.println("Average is: "+ av.average(10, 20, 30, 40));
    }}

    class Average {
        double average(double a, double b, double c)
        {
            double result = (a+b+c)/3;
            return result;
        }

        double average(double a, double b, double c, double d)
        {
            double result = (a+b+c+d)/4;
            return result;
        }
    }
