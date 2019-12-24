# 17/12/2019
# this program checks if a name is inside a petlist

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')

name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
    