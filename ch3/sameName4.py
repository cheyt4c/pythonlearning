# 16/12/2019
# this program demonstrates the error you receive when you attempt
# to use a local variable before declaring it

def spam():
    # ERROR
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()
