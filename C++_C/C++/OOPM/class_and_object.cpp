// C++ program to demonstrate function
// declaration outside class

#include <iostream>
using namespace std;
class Student
{
	public:
	string Student_name;
	int roll_no;
	
	// printname is not defined inside class definition
	void printname();
	
	// printid is defined inside class definition
	void printroll()
	{
		cout <<"Roll no. is: "<<roll_no;
	}
};

// Definition of printname using scope resolution operator ::
void Student::printname()
{
	cout <<"Student is: "<<Student_name;
}
int main() {
	
	Student obj1;
	obj1.Student_name = "Robert downey Jr";
	obj1.roll_no=16;
	
	// call printname()
	obj1.printname();
	cout << endl;
	
	// call printid()
	obj1.printroll();
	return 0;
}
