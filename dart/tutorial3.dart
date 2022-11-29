void main(){
    List names =['Abhay', 'Devansh', 'Deepu'];
    List<String> grp =['Abhay', 'Devansh', 'Deepu']; //this argument inside the <> fix the data type inside the list
    List<int> numbers =[01, 29, 12]; //this will throw the error bcz it only store the int values inside the list
    names.add('Tanu');
    names.remove('Deepu');
    print(names);
    print(grp);
    print(numbers);
}