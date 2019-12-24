# 16/12/2019
# this program demonstrates the difference between local and global scopes
# this program explores the interaction between local and global variables with
# the same name

def spam():
    eggs = 'spam local'
    #prints 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    #prints bacon local
    print(eggs)
    spam()
    #print 'bacon local'
    print(eggs)

eggs = 'global'
bacon()
#prints 'global'
print(eggs)


''' output
bacon local
spam local
bacon local
global 
'''
# there are actually 3 different variables in this program
# 1 - eggs in a local scope when spam() is called
# 2 - eggs in a local scope when bacon() is called
# 3 - eggs that exists in the global scope (inside the main)

# this is why its good practice to keep your variables as different names

