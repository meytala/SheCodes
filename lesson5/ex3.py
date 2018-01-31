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

