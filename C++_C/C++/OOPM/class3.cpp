#include <iostream>
using namespace std;

class employee{
    string name;
    float age;

    public:
    void getdata();
    void putdata();
};

    void employee :: getdata(){
        cout << "enter name: "<<endl;
        cin>>name;
        cout << "enter age: "<<endl;    
        cin>>age;
        // cout<<"Enter the size of the employee."<<endl;
        // cin>>size;
        }

    void employee :: putdata(){
        cout << "name: "<< name<<endl;
        cout << "age: "<< age<<endl;
        }

const int size = 3;
int main() {
    employee manager[size];

    for(int i = 0; i < size; i++){
        cout<<"Deails of manager: "<< i+1<<endl;
        manager[i].getdata();
    }

    cout<<endl;

    for(int i = 0; i < size; i++){
        cout<<"\n manager: "<< i+1<<endl;
        manager[i].putdata();
    }

    return 0;
}