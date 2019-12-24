# 16/12/2019# 16/12/2019
# this program demonstrates the declaration of a global varibale within 
# a function

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)



'''
eggs is declared a gloab at the top of spam, when eggs is set to spam, the 
assignment is done globally scoped eggs. No local variable 'eggs' is created
'''
