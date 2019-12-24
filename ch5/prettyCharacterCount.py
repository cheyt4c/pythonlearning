# 23/12/2019
# This program uses a dictionary to count up the occurence of letters 
# within a string
# it also uses the 'setdefault function'
# the pretty print module is used and makes reading the output easier

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count ={}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)