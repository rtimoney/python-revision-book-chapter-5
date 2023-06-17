# Branching Choices

# input is read as a string value by default and therefore must be cast as an int for arithmetic comparison
num = int(input('Please enter a number: '))

if num > 5 :
    print('Numer exceeds 5')
elif num < 5 :
    print('Numer is less than 5')
else :
    print('Numer is 5')

if num >7 and num <9 :
    print('Numer is 8')


if num == 1 or num == 3 :
    print('Numer is 1 or 3')

# indentation is very important in Python - identifies code blocks to the interpreter
# if: elif: else: is equivalent to switch or case statements in other language 

