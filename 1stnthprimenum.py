# write a progarmm to first n  prime number 

def check_in(n):
    a = 0
    i = 2 
    l1 = []
    while(len(l1) < n ):
        chk = 0 
        for j in range(1,i//2+1):
            if  i%j == 0 :
                chk +=1


        if chk == 1 :
            l1.append(i)
            
        i+=1

    return l1 

num = int(input("enter the n  prime number "))
print(check_in(num))