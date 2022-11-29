void main(){
  String greet = greeting();
  int age = getage();
  print(greet);
  print(age);
}

//creating return function 
String greeting() => 'hello'; //we can also use arrow operator which is used in javascript same as return
// String greeting(){
//   return "hello";
// }

int getage() => 30;
// int getage(){
//   return 30;
// }

