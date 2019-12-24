# 16/12/2019
# similar to zeroDivide.py
# this program demonstrates exception handling. In real world, you do not
# want your program to hang if there is an exception. You want the program to 
# handle it and keep running
# we accomplish this by using 'try' and 'except' statements

def spam(divideBy):
    return 42 / divideBy


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

except ZeroDivisionError:
    print('Error: Invalid argument')

#this output differs to the previous program because it does not continue to
# evaluate spam(1) because once it jumps to the except clause, it does not
# go back into the try clause
