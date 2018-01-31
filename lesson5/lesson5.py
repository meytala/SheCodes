print("hello world")
messege = 'Hello World'
print(messege)
print(messege.lower())
print(messege.upper())
#in order to have multi line code- you can use 3 "
bla = """blablablabla
blablablab"""
print(bla)
print(len(bla))
print(bla.count('bla'))##counts how many times do we have bla in the text
print(bla.find('lab')) ###return the index where the word start
print(bla.replace('bla','kol')) ###somtime we need to assign it to a new variable, or defining again the same variable
print(bla.split())
print(bla.split('bla'))
greeting = "hello"
name = 'meytal'
new_messege = greeting +', ' +name +'. welcome'
print(new_messege)
messege_2= '{}, {}. welcome'.format(greeting, name)
print(messege_2)

### F strings functions (in python 3 and above) they help making string formating easy
messege_3= f'welcome {name[0].upper()}{name[1:]}' ###you use directly the words
print(messege_3)


person = {'name':'tsviki', 'age':'27'}
sentence =  'my name is {name} and I am {age} years old'.format(**person)
print(sentence)


for i in range(1,11):
    sentense_1 = 'the number is {}'.format(i)
    print (sentense_1)

pi= 3.14159265

sentence = 'pi is equal to {:.2f}'.format(pi) ##will only print 2 decimal places
print (sentence)

sentence = '1mb is equal to {:,}'.format(1000**2) ##will put , in the right places
print (sentence)

sentence = '1mb is equal to {:,.2f}'.format(1000**2) ##will put , in the right places
print (sentence)

##############################dates

import datetime
my_date = datetime.datetime(2018,1,31,7,45)
print (my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

list_1 = ["hello", "meytal", "how", "are", "you", "?"]
print(" ".join(list_1))

