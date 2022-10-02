// Java Program to swap two numbers without using temporary
// variable

class swap_two_numbers {
	public static void main(String[] args)
	{
        // here value of x is 10
		int x = 10;
        // here value of y is 5
		int y = 5;

		// Code to swap 'x' and 'y'
		x = x * y; // x now becomes 50
		y = x / y; // y becomes 10
		x = x / y; // x becomes 5

		System.out.println("After swaping:"
						+ " x = " + x + ", y = " + y);   // after swaping values of x and y are interchanged
	}
}