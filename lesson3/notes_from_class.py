print("hellow world")

print ("add function:")
add = lambda num1,num2:num1+num2 ### add - the variable that indicates the function
##the lambda function is always in one line
print(add(3,5))

print ("map and lambda function:")
result = map(lambda x: x**2,[1,2,3,4])
print(list(result))  ###the map function maped the function to everything that is in the brakets
##we had to define it as a list


#print ("first module name is:{}".format(__name__)) ####name is a special variable in python.
# it will give the name of the file to the code. in this example will return __main__

###but if we import a file, it will give me the name of the file
### see bla bla

#def main():
#    print ("first module name is:{}".format(__name__))

if __name__== '__main__':
    print ("run directly") ##if the file is the main - go to the main function and print what is in the main function
else:
    print ("run from import")
##is this file running directly by python or does it import the program
#print ("first module underscore is:{}".format(__name__))
###name is a special variable in python. it will give the name of the file to the code


#another option

def main():
    print("main module")

if __name__=='__main__':
    main()
