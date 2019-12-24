# 17/12/2019
# write a function that takes a list value as an argument and returns a string 
# with all the items separated by a comma and a space with 'and' inserted 
# before the last item

#function which takes in a list
def listfunc(someList):
    #declare a string called cheese with the first element in spam
    cheese = spam[0]

    #loop to cycle through the list
    for i in range(len(spam) - 2):
        #append comma with the next element
        cheese = cheese + ', ' + spam[i + 1]
    
    #append 'and' to the second last element and add last element
    cheese = cheese + ' and ' + spam[i + 2]

    #return value
    return cheese


#list i want to convert to a string
spam = ['apples', 'banana', 'tofu', 'cats']
result = listfunc(spam)
print(result)


