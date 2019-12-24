# 17/12/2019
# this program demonstrates the use of the copy and deepcopy function
# this is used when you haee a function which modifies the list, however
# you do not want it to manipulate the real/original list. Hence, you 
# take a copy of that list before modifying the copied list

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

#cannot run for some reason, will troubleshoot later

