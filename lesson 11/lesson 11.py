fw = open('sample.txt', "w")  ### w - means that we will write in the file  IT IS A FILE OBJECT
fw.write ('now I am writing in my new MAT file that I created\n')
fw.write ('and it is working!!')
fw.close()

fr = open ('sample.txt', 'r')#to read a file, we need again to create another object,
text = fr.read() ##we need to store the data that is in the file that we read, we will store it to spesific variable
print(text)  ##now we can do what ever we want with the variable, it acts like a string variable
fr.close() ##don't forget to close, to be nice to the computer

#r - read
#w - write
#a - append
#r+
#rw+

file_name = 'example.txt'
example = open(file_name,'w') #w - will empty the file if there is something there, or create it if it is not exist
example.write("here i can write whatever I want\n")
example.write("in a different line I can write\n")
example.write("GOOD MORNING!!!")
example.close()


####you can use the with function with files, because it handles the file for you, and closes it at the end
with open(file_name, 'w') as example: ##open the file filen_name, and call it example
    lines = ["I am happy\n",
    "and I hope I will get it\n",
    'as I think opening files in python are important']

    example.write(lines[0])
    example.write(lines[1])
    example.write(lines[2])

    example.writelines(lines)  ###will run all the lines - do the interation for you


# with open(file_name, 'r') as reading_file: ##read file_name. you can read it with loops
#     text = reading_file.read()
#     print(text)


file_content = ''

with open(file_name, 'r') as reading_file:
    file_content = reading_file.read()
new_content = []
counter = 0

for character in file_content:
    if counter%2==0:
        new_content.append(character.upper())
    else:
        new_content.append(character.lower())
    counter +=1
# new_content = ''.join(new_content)
#
# with open (file_name, 'w') as writeble_file:
#     writeble_file.write(new_content)
#

with open (file_name, 'a') as appending_file:
    for char in new_content:
        appending_file.write(char)  ## since we are in the appending mode, it will append and not overwrite
