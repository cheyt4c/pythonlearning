# 16/12/2019
# this program is to demonstrate the use of the 4 rules to help determine whether
# a variable is global or local variable
'''
# the 4 rules are as follows
    1 - if a variable is used in global scope (outside of all functions), it
        global
    2 - if there is a 'global' statement for that variable in a function, it 
        is a global
    3 - if the variable is unused in an assignment statement in a function, it 
        is a local variable
    4 - but if the variable is not used in an assignment statement, it is 
        a global variable

'''
def spam():
    global eggs
    #global variable
    eggs = 'spam'

def bacon():
    #local variable
    eggs = 'bacon'
    print(eggs) 

def ham():
    #this is the global
    print(eggs)

#global variable
eggs = 42
spam()
bacon()
print(eggs)