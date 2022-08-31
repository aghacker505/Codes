class Add1
{
    int a, b, c;
    Add1(int x, int y)
    {
        a = x;
        b = y;
    }
   void add()
    {
        c = a+b;
        System.out.println(c);
    }
}

class Ex_Pera_con
{
    public static void main(String[] args) {
        Add1 A1 = new Add1(20, 29);
        A1.add();
    }
}