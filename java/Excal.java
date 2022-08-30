import java.util.Scanner;

class calculation {
    int a, b;
    float c;

    void add(int a, int b) {
        c = a + b;
        System.out.println(c);
    }

    void sub(int a, int b) {
        if (a > b) {
            c = a - b;
            System.out.println(c);
        }

        else {
            c = b - a;
            System.out.println(c);
        }
    }

    void multi(int a, int b) {
        c = a * b;
        System.out.println(c);
    }

    void dev(int a, int b) {
        if (a > b) {

            c = a / b;
            System.out.println(c);
        }

        else {
            c = b / a;
            System.out.println(c);
        }
    }

    class Excal {
        public static void main(String args[]) {
            calculation c1 = new calculation();
            Scanner sc = new Scanner(System.in);
            int x, y;
            x = sc.nextInt();
            y = sc.nextInt();
            c1.add(x, y);
            c1.sub(x, y);
            c1.multi(x, y);
            c1.dev(x, y);
        }
    }
}
