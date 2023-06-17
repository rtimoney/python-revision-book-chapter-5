# catching errors

# try except blocks can be used where it is possible to anticipate errors - eg where

title = 'Coding for beginners in easy steps'

try :
    print(titel)

# except NameError as msg :
except (NameError, IndexError) as msg :
        print( msg )

day = 32
try :
    if day > 31 :
        raise ValueError('Invalid Day Number')
    # more statements to execute get added here

except ValueError as msg :
    print('The program found an ' , msg)

finally :
    print('But today is beautiful anyway.')

# loop

day = 29
for i in range(1,10) :

    day += 1
    
    try :
        if day > 31 :
            raise ValueError('Invalid Day Number')
        # more statements to execute get added here

    except ValueError as msg :
        print('The program found an ' , msg)

    finally :
        print('But today is beautiful anyway.')
