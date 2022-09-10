# function can be passed as parameters to other functions
def display(func):
    return "How are you? " + func

def message():
    return "Abhay"

#call display() function and pass message() function
print(display(message()))