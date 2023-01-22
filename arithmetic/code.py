from utilities.function import data
from utilities.function2 import alpha

def value(a):
    print("the value is",a)


 
if __name__=="__main__":

    #it is based on utiity function write a code and importing a module
    #function1 here
    obj = data(1, 2, 3)
    print(obj.add())
    k=obj.add()
    print(k)

    #with the value come out from thefunction 1,passing to annother function in the same 
    #code

    throne=value(k)

    #importing function2 for performing operations

    obj2=alpha(1,2,3)
    l=obj2.multi()
    print(l)
    

