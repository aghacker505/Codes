class Add
{
    int a, b, c;
    Add()
    {

    }
   void add()
    {
        c = a+b;
        System.out.println(c);
    }
}

class Ex_NoArg_con
{
    public static void main(String[] args) {
        Add A1 = new Add();
        A1.add();
    }
}