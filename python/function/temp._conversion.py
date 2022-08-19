def temperature(Cel):
    conversion = (Cel*9/5)+32
    return conversion

def temperaturef(Fah):
    conversion1 = (Fah-32)*(5/9)
    return conversion1

line1 = input("Enter your temperature ")
line2 = input("Enter C for conversion in Celcius or enter F for conversion in fahrenheit ")
if line2 == "c":
    convert1 = temperaturef(int(line1))
    print("This is the temperature in Celcius ",convert1)

elif line2 == 'f':
    convert2 = temperature(int(line1))
    print("This is the temperature in fahrenheit ",convert2)