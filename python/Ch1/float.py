#meaning of float is number with decimal or fraction
number = input('number: ')
result = 100 - float(number)  # here it will through the fractional output no matter how we enter input number weather in decimal or integer
# result = 100 - int(number)  #here it will through error if we enter number in decimal bcz interger is used to convert number into integer 
print(result)