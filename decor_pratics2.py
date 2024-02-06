
''' In this programm we add the N number pass to the function  Using decorator '''

def decor(func):
    def waraper_fun(*args,):
        a = all( (type(i) == int or type(i) == float) for i in args)  # check all function is int or float 
        if a == False :
            return "Please enter Only int or float data type "      # if all number are not int or float then return the  funciton 
        return func(*args) 
    return waraper_fun

@decor # shortest way to assign a decorator 
def add_item(*args):
    total = 0 
    for i in args:
        total+=i

    return total 


print("The Addition of a function is :- ",add_item(23,3,4,5.2,5,1,))