class Firstthread extends Thread
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