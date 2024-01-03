# writea a programm to create a function jo imput me employ me naam aur salary le aur ushko print kar de 



n = int(input("Enter the No. of employee"))
a = { input(f"enter the {i}name"):int(input("Enter the salary "))     for i in range(n)  }

def employ(a):
    for i,j in a.items():
        print( f" the name is { i}  and the salary is {j}")

employ(a)
