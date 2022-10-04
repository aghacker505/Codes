num = int(input("Enter any number: "))

rev = 0

while (num>0):
    dig = num%10
    rev = rev*10 + dig
    num = num//10

print("The revese number is:", rev)