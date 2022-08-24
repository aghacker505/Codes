class add
{
    int a,b,c;
    void addnum(int x, int y)    
    {
        a=x;
        b=y;
        c=a+b;
        System.out.print("The sum is "+c);
    }
}
class ExAdd
{
    public static void main (String args[])
    {
        add A1 = new add();
        A1.addnum(10,20);
    }
}
