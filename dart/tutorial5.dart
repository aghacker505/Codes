void main(){
  User userone = User('Abhay', 30);
  print(userone.username);

  User usertwo = User('Deepu', 30);
  print(usertwo.username);

}

class User{
  String username;
  int age;

  User(String username, int age){
    this.username = username;
    this.age = age;
  }
}