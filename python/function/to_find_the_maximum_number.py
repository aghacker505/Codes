def function (num1, num2, num3):
    if (num2 > num3):
        if (num2 > num1 ):
            return num2
        else:
            return num1
    else:
        if (num1 > num3):
            return num1
        else:
            return num3

line1= input("Enter your first number = ")

line2 = input("Enter your second number = ")

line3 = input("Enter your third number = ")

m = function(line1, line2, line3)

print("The maximum number among the above is", m)