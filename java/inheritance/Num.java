public class Num {
    int a, b;
    void get_num()
    {
        a = 5;
        b = 6;
    }
}

class Add extends Num{
    int c;
    void get_add(){
        get_num();
        c = a+b;
    }
}

class Display_Add extends Add{
    void display_add()
    {
        get_add();
        System.out.println(c);
    }
}

class Multi_level_inherit
{
    public static void main(String[] args) {
        Display_Add A1 = new Display_Add();
        A1.display_add();
    }
}