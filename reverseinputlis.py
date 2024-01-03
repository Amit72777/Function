# input the list elment and reverese them using pop and append fuction 

def revse(l2,b):
    l3 = []
    for i in range(b):
        a = l2.pop()
        l3.append(a)
    return l3


def i_list(l1):
    a = int(input("Enter teh size of list "))
    for i in range (a):
        b = int(input(f"Enter the {i}  index  element ")) # input element 
        l1.append(b) # add element in list 
    return revse(l1,a)

list = []
list2 = i_list(list)
print( " reverser of list is : " ,list2)

