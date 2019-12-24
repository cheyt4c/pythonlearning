#this program demonstrates the use of break, continue functions within 
#a while loop.
#these functions also work in for loops -- need to verify

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')