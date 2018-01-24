## functins with STR:
#isalnum
x='meytal'
print(x.isalnum())#checks whether the string consists of alphanumeric characters (no space).
y='meytal avgil'
print(y.isalnum()) ##there is a space

#split
print(y.split())#Split the argument into words

#replace
#returns a copy of the string in which the occurrences of old have been replaced with new
#str.replace(old, new[,max]) #if the max argument is givven, only the first count occurrences are replaced.

str = "this is string example....wow!!! this is really string"
print(str)
print (str.replace("is", "was")) ##replace all the "is" in "was"
print (str.replace("is", "was", 3))

#join
