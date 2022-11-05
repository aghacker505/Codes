class FirstThread extends Thread
{
    public void run()
    {
        for(int i = 0; i<4; i++)
        {
            try
            {
                if(i==3)
                {
                    sleep(4000);
                }
            }

        catch(Exception x)
        { }
        System.out.println(i);
        }
        System.out.println("First thread finished");
    }
}

class SecondThread extends Thread{
    public void run()
    {
        for(int i=0; i<4; i++)
        {
            System.out.println(i);
        }
        System.out.println("Second thread finished");
    }
}
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