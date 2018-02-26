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




Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

def string_match(a,b):
    num_match = 0
    for i in range (0, min(len(a), len(b))-1):
        a_string = '{}{}'.format(a[i],a[i+1])
        b_string = '{}{}'.format(b[i],b[i+1])
        if a_string == b_string:
            num_match += 1
    return num_match

results = string_match('abc', 'abc')
print(results)


#####write a function that accept a list of strings
#the fnctionj return the string that are longer than or equal to 2
#and the first and the last are identical

def string_test (a):
    text = []
    for i in a:
        if len(i) >= 2 and i[0]==i[-1]:
            text.append(i)
    return text

a= ['aba', 'xyz', 'aa', 'x', 'bbb']
result_2 = string_test(a)
print ('the answer to 2 is:')
print (result_2)
