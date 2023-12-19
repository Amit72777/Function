# input the list size and elment and print the spuare of list 

def sqrare(sq):
    for i in range(len(sq)):
        sq[i] = sq[i] ** 2 
    return sq


def i_list(l1):
    a = int(input("Enter teh size of list "))
    for i in range (a):
        b = int(input(f"Enter the {i}  index  element "))
        l1.append(b)

    l2 = sqrare(l1)
    return l2


list = []
i_list(list)
print(list)