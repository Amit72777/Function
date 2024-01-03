def faboo(n):
    a = 0
    b = 1 
    for i in range(n):
        print(a,end = " ")
        c = a + b
        a = b
        b = c
n1 = int(input("Enter the Number of term "))
faboo(n1)