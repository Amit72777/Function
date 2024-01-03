''' write a programm to create a recursive function to calculate the factorial of number '''
def facto(n):
    if n==0 or n==1 : return 1
    return facto(n-1)*n

a = int(input("Enter the number "))
print("The factorial is ",facto(a))
