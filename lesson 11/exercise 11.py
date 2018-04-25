#### open a folder, named new_folder in a write mode and write into the folder

file_11 = open ("new_folder.txt", "w")
file_11.write("one\n")
file_11.write("two\n")
file_11.write("three\n")
file_11.write("four\n")
file_11.write("five\n")
file_11.write("six\n")
file_11.write("seven\n")
file_11.write("eight\n")
file_11.write("nine\n")
file_11.write("ten\n")
file_11.write("eleven\n")
file_11.write("twelve\n")
file_11.write("thirdteen\n")
file_11.write("fourteen\n")
file_11.write("fiftheen\n")

file_11.close()


###open the writen folder in a read mode
file_11 = open("new_folder.txt", "r")

###read all the lines in the folder, and reverse each line seperatly. will do it by creating a list and appending it
file_11_a = file_11.readlines()
reversed_text = []
for line in file_11_a:
    #print (line)
    reversed_text.append(line[::-1])
    # reversed_text = "".join()

print(reversed_text)

file_11.close

####in order to write an argument in a file, we need to change it to a string (now, it is a list)
reversed_text_str = ''.join(reversed_text)
print(reversed_text_str)


### now we need to write the new string in a new file.
reversed = open("reverse.txt", "w")
reversed.write(reversed_text_str)
reversed.close()


#####read from the original file
original = open("new_folder.txt", "r")
to_join_1 = original.readlines()
original.close()

###change it to a str
to_join_1=''.join(to_join_1)
# print(to_join_1)


#####read from the reversed file
reversed_1 = open("reverse.txt", "r")
to_join_2 = reversed_1.readlines()
reversed.close()

###change it to a str
to_join_2=''.join(to_join_2)
# print(to_join_2)


####create a new folder to hold both lists of words
join_folder = open("joined.txt", "w")
join_folder.write(to_join_1)
join_folder.write(to_join_2)

