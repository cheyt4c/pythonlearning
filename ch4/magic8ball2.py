# 17/12/2019
# this program is an improved version of the program found in the previous
# chapter
# this program uses a list

#import random module
import random

#declares a list with the following strings
messages= ['It is certain' , 
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# generates a random number between 0 and the message number
print(messages[random.randint(0, len(messages) -1)])