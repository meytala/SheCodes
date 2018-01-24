###list vs. tuples
# tupels cant be changed, list can
# x = 5,6,7,8 ##tupels - more efficiant - quicker, cant be modify
# x= [5,6,7,8] ##list -

def example():
    return 6, 15  ### will return 6,15


x, y = example ()  ## x- will be 6, y will be 15

a = (4, 7, 5, 8)
b = [4, 7, 5, 8]

print (a[0])  ##will run a wuth index 0

##list manipulations
c = [2, 5, 3, 6, 9, 4, 8, 7, 2, 1]
c.append (9)  ###will add 9 at the end of the vector c
print (c)  ###will print c with 9 at the end, because it ends information

c.insert (2, 88)  ##will inser the number 88 in index 2
print (c)

c.remove (2)  ##will remove the first 2
print (c)
c.remove (c[0])  ###will remove the first element in c
print (c)
c.pop ()  ##will remove the last variable in the list
print (c)
print (c[5])
print (c[5:8])  ##will print from index 5 to 7
print (c[-1])  ##will give me the last element
print (c[-2])  ##will give me one before last element
print (c.index (1))  ##the index value of 1  (it is 8)
print (c.count (9))  ###how many 9's are there? the answer is 2
c.sort ()  ##will sort the list. it actually change the list
print (c)

d = ['dan', 'maya', 'yael', 'nogah', 'rotem', 'uri']  ##remember that a list is in squere brakets
print (d)
d.sort ()
print (d)

####multidimentional lists
b = [4, 7, 5, 8]  ##one dimentional list
b = [[4, 0], [7, 0], [5, 0], [8, 0]]
print (b)
print (b[1])  # element in index 1
print (b[1][0])  # element o in index 1

###combine lists
users = ['tsviki', 'ima', 'aba']
age = [39, 69, 74]

allOfThem = users + age
print (allOfThem)
del (allOfThem[0])
print (allOfThem)

### dictionaries
##the ideas is to have keys and values
# a key will be a single element and value might be anything (lists, functions,
# to create a dictionary you use curly brakets {}
exDict = {'me': 38, 'tsviki': 39, 'nogah': 7, 'rotem': 5.5}
print (exDict)
print (exDict['me'])  ###will pring my age
###adding uri to the list
exDict['uri'] = 4
print (exDict)
exDict['me'] = 39  ##change my age to 39
print (exDict)
del exDict['me']  ##will remove me from the list
print (exDict)

exDict = {'me': 38, 'tsviki': 39, 'nogah': 7, 'rotem': 5.5}  ###add another variable for all keys
exDict = {'me': [38, 'brown'], 'tsviki': [39, 'blue'], 'nogah': [7, 'almond'], 'rotem': [5.5, 'brown']}
print (exDict['me'])
for k, v in exDict.items ():
    print (k, "=", v[0])

##sets
example = set ()  ##in set, the order doesnt metter

example.add (42)
example.add (False)
example.add (3.1415)
example.add ('somthing')
print (example)
##lets try to add another 42
example.add (42)
print (example)  ##sets to not contain duplicate elements
print(len(example))  ## how many elements the set have

example.remove(42)
print(example)

###union
##if we have a and b - the union is a or B - everything
##intersection is what is common to a and b

odd = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set({2,3,5,7})
composites = set([4,6,8,9,10])
print(odd.union(evens))
print(odd.intersection(primes))
print (2 in primes)
