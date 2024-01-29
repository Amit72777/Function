# passing a function as a argument 
# square the list 

def fun(n):
    return n**2

def my_map(func,l):
    ne_list=[]
    for item in l:
        ne_list.append(fun(item))   # call functin and append it 
    return ne_list 

n = int(input("Enter the list  size ")) # list size 

l = [ int(input("enter the list item  ") ) for i in range(n) ]  # using list comprehinsion create a list 

print(my_map(fun,l))  # passing a function and print it 
