def in_put(l1):
    a = int(input("Enter the Size of lsit "))
    for i in range(a):
        b= int(input(f"Enter the {i} index element "))
        l1.append(b)
    return l1

def common(l1,l2):
    l3 = []
    for i in l1:
        if i in l2 :
            l3.append(i)

    return l3 




list1 = []
list2 = []
print("Enter the fist list :")
in_put(list1)
print("Enter the 2nd list ")
in_put(list2)
list3 = common(list1,list2)
print(list3)