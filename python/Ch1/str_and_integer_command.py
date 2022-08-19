import string      #here w eneed to import string module


birth_year = input('Birth Year: ')          #here output is in string form
conv = int(birth_year)   #here we convert string into intger value using int
age = 2022 - conv    
print('Your age is', age)   #here we don't need to convert age into string bcz ,(comma) automaticaly covert the age into suitable data type (string module is required)
# print('Your age is ' +  str(age))   #here again we need to convert integer into string to add the add age in our sentence0