# Skipping Loops

# the break keyword can be used to prematurely terminate a loop when a specified condition is met

# range() funtion can ne used to iterate over a sequence of numbers which will continue up ro but not including the specified end value 
# The range() function can generate a sequence that decreases, counting down as well as those that count upwards
# eg range(5) generates 0,1,2,3,4

for i in range ( 1 , 4 ) :
    for j in range ( 1 , 4 ) :
        print('Running i = ' , i , 'j = ' , j)


print('\n\n')

# the break keyword can be used to prematurely terminate a loop when a specified condition is met
 
for i in range ( 1 , 4 ) :
    for j in range ( 1 , 4 ) :
        if i == 2 and j == 1 :
            print('Breaks inner loop at i = 2 j = 1')
            break
        print('Running i = ' , i , 'j = ' , j)

print('\n\n')

# the continue keyword can be used to skip a single iteration of a loop when a specified condition is met
 
for i in range ( 1 , 4 ) :
    for j in range ( 1 , 4 ) :
        if i == 1 and j == 1 :
            print('Continues inner loop at i = 1 j = 1')
            continue
        print('Running i = ' , i , 'j = ' , j)
