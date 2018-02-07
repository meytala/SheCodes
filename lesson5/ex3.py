###Q1
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
#middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
#middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
#middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way (a,b):
    return '{},{}'.format(a[1],b[1])

a=[1,2,3]
b=[4,5,6]
print("The answer to Q1 is:")
print(middle_way(a,b))

###Q2
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0


def string_match(a,b):
    value = 0
    for i in range(0, min(len(a),len(b))-1):
        first_string = '{}{}'.format(a[i],a[i+1])
        second_string = '{}{}'.format(b[i], b[i+1])
        if  first_string == second_string:
           value += 1
    return value

a='abc'
b='abcabc'
results = string_match(a,b)
print('the answer to Q2 is:')
print(results)

# Q3
# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True
from itertools import count


def same_first_last(nums):
    length = len(nums)
    first = nums[0]
    last = nums[-1]
    if length >= 1 and first == last:
        return True
    else:
        return False


results = same_first_last([1, 2, 3])
print('the answer to Q3 is:')
print(results)

##Q4
def string_fun(a):
    value = 0
    for w in a:
        length = len(w)
        first = w[0]
        last = w[-1]
        if length >= 2 and first == last:
            value += 1
    return value


a = ["aba", "ima", "noam", "meytalm"]
results = string_fun(a)
print(results)



#Q5

def char_freq(a):
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    damy=""
    for key in range(0, len(symbol)-1):
        answer = "{}:{}, ".format(symbol[key], a.count(symbol[key]))
        if  a.count(symbol[key])>0:
            damy +=answer
    return damy

a = "blabla"
results2 = char_freq(a)
print('the answer to Q5 is:')
print(results2)

#Q5b
def char_freq2 (a):
   bla = {}
   for key in a:
        if key in bla:
           bla[key] +=1
        else: bla[key] = 1
   return bla

a = "blabla"
results2a = char_freq2(a)
print('the answer to Q5b is:')
print(results2a)


#def encode(a):
##def encode(a):

print ("q6")
alpha_bet = 'abcdefghijklmnopqrstuvwxyz'
new_dic= {}
def encode (a):
    for i in range(0, len(alpha_bet)):
        if i < 13:
            new_dic_index = i+13
        else: new_dic_index = i-13
        new_dic[alpha_bet[i]]=alpha_bet[new_dic_index]
    print(new_dic)
    translation = ""
    for j in a:
        if j in alpha_bet:
            translation += new_dic[j]
        else: translation += j
    return translation

a= "v nz yrneavat clguba jvgu fur pbqrf npnqrzl!"
answer3 = encode (a)
print (answer3)
