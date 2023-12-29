''' define a function 
input num,iterable(touple,list ) containg nubmers as args
aud output return the list of cube of every item
and if no pass args then print " Hey you  didn't pass a agrs" '''


def power(num,*args):
    if  not args: return "hey you didn't pass args "  # if args are empty then return it 
    l1 = [num**3]  
    l2= [ i**3 for i in args]
    l1.extend(l2)
    return l1

a = int(input('Enter the nubmer '))  # enter the number 
n = int(input("Enter the size of list ")) # enter the size of list 
lis = [ int(input()) for i in range(n)] # enter the the item of list 
print(power(a,*lis)) # call the function and print reurn value 
