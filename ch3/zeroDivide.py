# 16/12/2019
# this program demonstrates exception handling. In real world, you do not
# want your program to hang if there is an exception. You want the program to 
# handle it and keep running
# we accomplish this by using 'try' and 'except' statements

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

