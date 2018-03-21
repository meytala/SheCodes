#enumerate - enalbke to see items in list and the order of the items

print("sample 1, enumerate:")
print(list(enumerate(('a', 'b', 'c'))))


# sample 1:
# [(0, 'a'), (1, 'b'), (2, 'c')]


print("sample 2, enumerate:")
arr=[2,3,47,10]
for i, elment in enumerate(arr): ##the i is for the index, the element is for the element
    print (i, elment)

# sample 2:
# 0 2
# 1 3
# 2 47
# 3 10


print("sample 3, enumerate:")
my_list = []
for (i, s) in enumerate(["a", "b", "c"]):
    my_list.append(i*s)

print(my_list)

# sample 3:
# ['', 'b', 'cc']


print("alternative to sample 3, , enumerate:")
my_list2 = [i*s for (i,s) in enumerate(["a", "b", "c"])]
print(my_list2)

# alternative to sample 3:
# ['', 'b', 'cc']

print("sample 4, dic.items():")
####dict.items() #מאחסן את המפתחות ואת הערכים של כל מפתח בטאפלy
my_dict = {4:0, 3:9, 100:8}
test = [my_tuple for my_tuple in my_dict.items ()]
print(test)
test2=[2*k+v for (k,v) in my_dict.items()]
print(test2)

# sample 4, dic.items():
# [(4, 0), (3, 9), (100, 8)]
# [8, 15, 208]


###zip = add to lists to one dictonarry
# movies = dict(zip(movie, actors))
print ("conditioning:")
a=5
if a==1:
    print ("a=1")
else:
    print ("a=5")

#a=5

print("alternatively:")

print('a=1') if a==1 else print('a=5')

#a=5

print("alternatively2:")
if a==1:
    print ("a=1")
elif a==2:
    print ("a=2")
else:
    print ("a=5")

# a=5

print("alternatively3:")
print("a=1") if a==1 else print("a=2") if a==2 else print("a=5")

# a=5


print ("condition with for:")
cond_with_for = [i for i in [1, None, 3, None, None, 6] if i !=None]
print(cond_with_for)

#[1, 3, 6]


print ("condition with for2:")
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
new_dict={list1[x]:list2[x] for x in range(len(list2)) if x !=4}
print(new_dict)

# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print("map:") ##built from a function and a list
list_a = list(range(1,20))
print(list_a)

def double(x):
     return x*2

print(list(map(double,list_a)))

print("filter:")
def is_even (x):
    return x%2==0  ##return true id even

print(list(filter(is_even, list_a)))####filter only the ones in the defined function - the ones that are true

print("lambda:") ##lambda = anonimus function
add = lambda num_1, num_2: num_1+num_2
print(add(1,2))

answer = map(lambda x:x**2, list_a)
print(list(answer))
