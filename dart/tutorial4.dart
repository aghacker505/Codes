void main(){
  User userone = User();
  print(userone.name);
  print(userone.age);
  userone.login();

  User usertwo = User();
  print(usertwo.name);
}

class User {
  String name = 'Mario';
  int age = 18;

  void login(){
    print('user logged in');
  }
}