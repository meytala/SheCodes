condition = 1
while condition < 10:  ### will run untill the condition is not met i.e. until 9
    print(condition)
    condition +=1

#while True: ##infinite loop - while it is always true
#    print ("doing stuff")
###to stop - hit ctrl+c

exampleList = [1,4,2,3,5,7,3,4,6,7]
for x in exampleList:
    print (x)
    print ("next line")

i=0
for i in range (100):
    print (i)  ##for i in the ramge of 100 print the i
    if i>5:  ###but there is a condition - if the i is more than 5, stop
        break
    else:  ## otherwise (i=0,1,2,3,4,5), print hello
        print ("hello")

print ("please come here")
#### in the first 6 runs, it doesnt stop because it goes to else. only when i>5 it stops. and print please come in

i=0
for i in range (100):
    print (i)  ##for i in the ramge of 100 print the i
    if i>5:  ###but there is a condition - if the i is more than 5,
        continue  #continue with the loop - going back to the begining of the loop without continued to the next phase
    else:  ##
        print ("hello")

    print ("please continue") ###after 6 will print i


i=0
for i in range (100):
    print (i)  ##for i in the ramge of 100 print the i
    if i>5:  ###but there is a condition - if the i is more than 5,
        pass  #do nothing. move forword once >5 is activated, do nothing move on to the statment
    else:  ##
        print ("hello")

    print ("passing") ###after 6 will print i
