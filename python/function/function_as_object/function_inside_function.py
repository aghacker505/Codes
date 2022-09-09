# define the function into another function
def display(str):
    def message():
        return "How are you? "
    mssg = message() + str
    return mssg

'''
here we call display functon which later call message function which
will return the writen message'''
p = display("Abhay")
print(p)