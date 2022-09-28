class Num   // parent class
{
    int a, b ;
    void get_num()
    {
        a = 5;
        b = 6;
    }
}

class Add extends Num
{
    int c;
    void get_num()
    {
        get_num();
        c = a+b;
        System.out.println(c);
    }
}
class Single_inherit
{
    public static void main(String[] args) {
        
        Add A1 = new Add();
        A1.get_num();
    }
}