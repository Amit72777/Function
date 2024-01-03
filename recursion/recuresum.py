''' write a programm to create a recursive function to calculate the sum of number from 0 to n '''

def recur(n):
    if n == 1 : return 1
    

    return recur(n-1)+n # function call itself for add 

n = int(input("Enter the nth number ")) # take a input of nth number 
print(recur(n))