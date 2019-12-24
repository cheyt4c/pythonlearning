# 17/12/2019
# this program is a practice program to execute the collatz sequence
# additionally, it builds upon the previous program, where it will continuously
# poll the user until it gets a valid value (int) 

# the previous program would exit when it did not get an int

import sys

def collatz(number):
    #if number is even -> print number//2, then return value 
    check = number%2
    if check == 0:
        number = number//2
        print(number)
        return number

    #else (number is odd) -> print 3*number+1, then return value
    else:
        number = 3*number + 1
        print(number)
        return number

def getInput():
    #prompt user for input. We expect an int
    print('Enter a value:')

    #try to get an input
    try:
        input_num = int(input())

    #if there is an error, set an error message and return, this will exit
    #function. 
    except ValueError:
        print('Error: Invalid argument. Please enter an Integer')
        flag = 'error'
        return flag

    #if everything is well, return the input_num
    return input_num

# main 
# prompt user to type in an integer that keeps calling collatz 
# on that number until the function returns the value 1

#ask for user input
user_input = getInput()

#if the function returns an error, it means the input was not an int
if user_input == 'error':
    user_input = getInput()

#print out what integer the user has input and begin collatz
print('The integer you have input is ' + str(user_input))
print('Collatz will now begin...')

output_num = collatz(user_input)

#keep iterating through collatz function until 1 is hit, which it will then exit
while output_num != 1:
    numb = output_num
    output_num = collatz(numb)

sys.exit()


