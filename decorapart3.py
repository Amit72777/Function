# Solve dos.string problem in decorator 

from functools import wraps  # import module 


def decor_add(funtion):  # decorator function 
    @wraps(funtion)   
    def new_funtion(*args,**kwargs):
        ''' This is new function '''  # decorator doc_string 

        print("this is new addition ")  
        return funtion(*args,**kwargs)
    
    return new_funtion


@decor_add
def add_deco(*args):
    ''' this is add  function '''  # function doc_string 
    add = 0    
    for i in args:
        add+=i  # add item 
    return add


print(add_deco.__doc__)
print(add_deco.__name__)

print(add_deco(1,2,3,4,5))
