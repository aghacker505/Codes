#include <iostream>
using namespace std;

int main(){
    float marks;

    cout<<"Enter your marks: ";
    cin>>marks;

    if (marks>=90){
        cout<<"Your grade is A+";
    }

    else if (marks>=80){
        cout<<"Your grade is A";
    }

    else if (marks>=75){
        cout<<"Your grade is B+";
    }

    else if (marks>=70){
        cout<<"Your grade is B";
    }

    else if (marks>=65){
        cout<<"Your grade is C+";
    }

    else if (marks>=60){
        cout<<"Your grade is C";
    }

    else if (marks>=55){
        cout<<"Your grade is D+";
    }

    else if (marks>=50){
        cout<<"Your grade is D";
    }

    else if (marks>=40){
        cout<<"Your grade is E";
    }

    else{
        cout<<"Your grade is F";
    }
    return 0;
}