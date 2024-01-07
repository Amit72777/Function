'''
# This is Challenge

defin a function take any no of lists containing number 
[1,2,3],[4,5,6],[7,8,9] ..........
# return average 
(1,4,7)/3 , (2,5,8)/3, (3,6,9)/3.......😊😊
'''
def ope(*l1):
    new = []
    for pair in zip(*l1):
        new.append(sum(pair)/len(pair))

    return new
no = int(input("Enter the number of list :"))
mo = int(input("Size of list "))
print("Enter the element ")
lis =  [[ int(input(f"Enter  {j} list element ")) for i in range(mo)]  for j in range(no) ]
print( " The input list are ",lis)
print( " The Average  value are :- ", ope(*lis))
