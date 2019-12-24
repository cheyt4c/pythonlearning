#this program demonstrates the use of if,elif statements for 
#program control and basic logic

# ask for name of individual
print('What is your name?')
name = input()

# find age of individual
print('What is your age?')
age = input()

if name == 'Alice':
    print('Hi, Alice')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif int(age) > 100:
    print('You are not Alice, grannie')
elif name != 'Alice':
    print("You are an imposter")

