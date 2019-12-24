# 17/12/2019
# this program demonstrates why lists are useful

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
        ' (or enter nothing to stop.):')
    
    name = input()
    if name == '':
        break
    
    #list concatenation
    catNames = catNames + [name] 

print('The cat names are:')
for name in catNames:
    print(' ' + name)