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

from time import sleep

def delay (f):
    def wrapper (*args):
        sleep (0.1)
        f(*args)
    return wrapper

@delay
def printnum (i):
    print (i)

counter = 3
while counter >=0:
    printnum (counter)
    counter-=1
print ("KA-BOOM!")

#Exercice 5:

def delay2 (delayTime):
    def decorator (f):
        def wrapper (*args):
            sleep (delayTime)
            f (*args)
        return wrapper  
    return decorator

@delay2 (0.1)
def printnum2 (i):
    print (i)

cnt = 15
while cnt >=0:
    printnum2 (cnt)
    cnt -=5
print ('KA-BOOM!')

#Exercice 6 :

def binrep (number):
    pass

b = binrep (12)
while True :
    try : 
        print (next (b))
    except StopIteration:
        break