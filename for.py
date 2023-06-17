#  Counting Loops

# a for loop iterates over the items of any list or string in the order that they appear in the sequence
# Python for loops do not allow step size (size of the iteration step) and end (halting condition) to be specified

# anything that contains multiple items that can be looped over is described as "iterable"

# range() funtion can ne used to iterate over a sequence of numbers which will continue up ro but not including the specified end value 
# The range() function can generate a sequence that decreases, counting down as well as those that count upwards
# eg range(5) generates 0,1,2,3,4


# list
chars = ['A','B','C']
# fixed tuple list
fruit = ('Apple','Banana','Cherry')
# associative dictionary list  
info = {'name':'Mike','ref':'Python','sys':'Win'}


print('Elements :\t', end = '')
for item in chars :
    print (item, end = '')

print('\n')
 
print('Enumerated :\t', end = '')
for item in enumerate(chars):
    print (item, end = '')

print('\n')
 
print('Zipped :\t', end = '')
for item in zip(chars,fruit):
    print (item, end = '')


print('\n')
 
print('Paired :')
for key , value in info.items():
    print (key , '=' , value)
