# Looping Conditions

# a loop is a block of code which automaticall repeats as long as a given condition remains true and terminates once the given condition becomes false
# the while keyword creates a loop in this format

i = 1
while i < 4 :
    print('Outer loop iteration :' , i)
    i += 1
    
    j = 1
    while j < 4 :
        print('\tInner loop iteration :' , j)
        j += 1
