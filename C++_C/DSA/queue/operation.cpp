#include <iostream>
#define MAXSIZE 5

using namespace std;

struct stk
{
  int top;
  int stack[MAXSIZE];
} s;
// void push();
// int pop();
// void display();

void push()
{
  int value;
  if (s.top == MAXSIZE - 1)
  {
    cout << "Overflow \n";
    return;
  }

  s.top = s.top + 1;
  cout << "\n Enter value to insert \n";
  cin >> value;
  s.stack[s.top] = value;
  return;
}

int pop()
{
  int temp;
  if (s.top == -1)
  {
    cout << "Underflow \n";
    return 0;
  }
  temp = s.stack[s.top];
  s.top = s.top - 1;
  return s.stack[s.top];
}

void display()
{
  int i;
  for (int i = 0; i <= s.top; i++)
  {
    cout << s.stack[i] << " ";
  }
  cout << endl;
  return;
}

int main()
{
  int choice = 1;
  int option;
  s.top = -1;

  while (choice)
  {
    cout << "1. Insert elememt at rear \n";
    cout << "2. Delete element at front \n";
    cout << "3. Display element of queue \n";
    cout << "4. Exit \n";

    cout << "Enter Option \n";
    cin >> option;

    // Switch case
    switch (option)
    {
    case 1:
      push();
      break;

    case 2:
    {
      int q = pop();
      cout << "Deleted element " << q << endl;
      break;
    }

    case 3:
      display();
      break;

    case 4:
      return 0;

    default:
      cout << "Invalid Choice \n";
    }

    cout << "Do you want to continue...(0 for No and 1 for yes..)" << endl;
    cin >> choice;
    if (choice == 0)
    {
      break;
    }
  }

  return 0;
}