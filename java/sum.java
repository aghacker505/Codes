import java.util.*;
class sum 
{
    public static void main (String args[])
    {
        int a,b,c;
        System.out.println("Enter two number: ");
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        c = a+b;
        System.out.println("the sum of two numbers is " + c);
    }
}