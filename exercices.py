#Exercice 1

def call (f):
    return f ()

def sayHello ():
    print ('Hello')

call (sayHello)

#Exercice 2

def call2 (f, *args):
    return f (*args)

def add (a,b):
    return a+b

print (call2 (add, 5, 4))

#Exercice 3:

def compute (a, b, op=add):
    return op (a,b)

def sub (a,b):
    return a-b

def call3 (f, *args, **kwargs):
    return f (*args, **kwargs)

print (call3 (compute, 5,4))
print (call3 (compute, 5,4, op=sub))

#Exercice 4 : 




