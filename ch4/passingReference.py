# 17/12/2019
# this program demonstrates how lists are stored by reference.
# notice how the function does not have a function call

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)