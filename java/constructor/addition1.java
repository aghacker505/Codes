package constructor;

public class addition1 {
    int a,b;
    addition1(int x, int y)
    {
        a = x;
        b = y;
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