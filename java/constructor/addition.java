package constructor;

public class addition {
    int a,b;
    addition()
    {
        a = 12;
        b = 10;
    }

    void add()
    {
        System.out.println(a+b);
    }
}

class Ex_IT3AB1_const
{
    public static void main(String[] args)
    {
        addition A1 = new addition();
        A1.add();
    }
}