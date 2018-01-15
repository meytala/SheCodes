print("bla")

print('if else:')
x= 5
y= 3
z = 5

if x < y:
    print ('y is greater than x ')
else:
    print ('y is not greater than x')
## to write equal you need double ==
## to write not equal !=
##else only link to the last if
## if there are 2 "If"  statements, and the first is false and the second is true - the second one will run, without the else

###elif - nce there is an elif statement that is true, it will stop there.
##otherwise, the last if will run

print('if elif:')
a=5
b=10
c=22
if a>b:
    print ('a is greater than b')
elif a<c:
    print ('A IS LESS THAN C')
elif 2<5:
    print ('2 is less than 5')
else:
    print ('if and elif never run')

print('functions:')
#####functions
### start with def - a short for define and than use a word to define the name of the function
### try to not use a common name - as it might conflict with existing module
### after the definition of the sample name - () in which you put parameters
### after than you use :  and enter
#### anything after will be the function block
print('example 1 for functions:')
def example():
    print ('basic function')
    z=3+9
    print (z)

###after defining the function you need to call the function
example()

print('example 2 for functions:')
def simple_addition (num1, num2):  ###the parameters will act like variables in a function
    answer = num1 + num2
    print ('num1 is ',num1)
    print (answer)

simple_addition (5, 3) ###can also write (num1=5, num2=3)

print('example 3 for functions:')
def simple (num1, num2=5):
    print (num1, num2)

simple (2)

print('example 4 for functions:')
def basic_window (width, hight, font='ariel',
                  bgc='W', scrollbar= True):
    print (width, hight, font, bgc)

basic_window (5,4) ###we only need to spesify values for parameters that are not defined

print ('global and local variables:')
##"global variable - can be accessed anywhere, local - can be accessered within its environment


print('example 5 for functions:')
x1= 6
def example5 ():
    global x1 ### saying that x1 is a globla variable
    print (x1)
    print (x1+5)
    x1+=5  ##we can only do that because we defined x as a global variable

example5 () ###will  print x1, and x1+5

print('example 6 for functions:')
x1= 6
def example6 ():
    globx = x1  ### saying that x1 is a local variable
    print (globx)
    globx+=5  ##this is only in this function - changed the globx
    print (globx)

    return globx ###the function is going to becoe the return value
x2=example6 ()
print (x2)

print('example 7 for functions:')
def doubleit(x):
    return 2*x          ##when we use the heyword return in a function
                        ## the function is actually become the return value
                        ## whereever the function is called
x=doubleit(4)
print (x)

print('example 7 for functions:')

def cat_dog (x):
    if x>5:
        return ('cat')
    else:
        return ('dog')

x=cat_dog (6)
print (x)  ###will print cat



