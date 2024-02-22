

def add_(n):  # create function for generator 
    for i in range(2,n+1,2):
        yield i 



a = add_(10)
for i in  a:
    print(i)

# generator comprehension 
print("\n\n Generator Compreshension \n \n ")
gen = (i ** 2 for i in range(2,10))

for i in gen:  
    print(i)
