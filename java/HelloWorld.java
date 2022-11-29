import java.applet.Applet;
import java.awt.Graphics;

//HelloWorld class extends Applet
public class HelloWorld extends Applet
{
    public static void main(String args[]){
        @Override
        public void paint(Graphics g)
        {
            g.drawString("Hello World", 20, 20);
        }
    }
}