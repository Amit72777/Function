''' 
create an inner function to calculate the addition in the following ay
1: create an outer function that will accept two parameters
2: create an inner function  inside an outer function that will calculate the addition of a and b 
3: At last, an outer function will add 5 into additon and return it 

'''


def out(a,b):

    def inn(a1,a2):
        return a1+a2
    
    return 5+inn(a,b)


a = int(input("Enter the number "))
b = int(input("Enter5 the second number "))

print(out(a,b))