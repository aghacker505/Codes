class Assign2_IT_3A_B1
{
    public static void main(String args[])
    {
        FirstThread a1 = new FirstThread();
        SecondThread b1 = new SecondThread();

        a1.start();
        b1.start();
    }
}