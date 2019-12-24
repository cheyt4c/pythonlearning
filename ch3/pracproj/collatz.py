# 17/12/2019
# this program is a practice program to execute the collatz sequence

import sys

def collatz(number):
    #if number is even -> print number//2, then return value 
    check = number%2
    if check == 0:
        number = number//2
        print(number)
        return number
    else:
        number = 3*number + 1
        print(number)
        return number
    #else (number is odd) -> print 3*number+1, then return value


# main 
# prompt user to type in an integer that keeps calling collatz 
# on that number until the function returns the value 1

print('Enter a value:')
try:
    input_num = int(input())

except ValueError:
    print('Error: Invalid argument.')
    sys.exit()

output_num = collatz(input_num)

while output_num != 1:
    input_num = output_num
    output_num = collatz(input_num)

sys.exit()


