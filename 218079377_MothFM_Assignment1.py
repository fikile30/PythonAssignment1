# problem 1
givenString = "fullstackslp"
# Use indexing to print the following
# 'f'
print(givenString[0])
# 'p'
print(givenString[-1])
# 'stack'
print(givenString[4:9])
# 'slp'
print(givenString[9:13])
# 'cks'
print(givenString[7:10])
# 'Bonus: use indexing to reverse the string'
reversedString = ''
index = len(givenString)
while index > 0:
    reversedString += givenString[index - 1]
    index = index - 1
print(reversedString)

## problem 2 [LISTS]

l = [3, 7, [5, [1, 4, "hello"]]]

## reassigning "hello" to be "goodbye"
l[2][1][2] = 'goodbye'
print(l)

## problem 3 Dictionaries

# using keys and indexing, grab the "hello" from the following dictionaries
d1 = {'simple_key': 'hello'}
d1['simple_key']
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
d2['k1']['k2']
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
d3['k1'][0]['nest_key'][1][0]
print(d3['k1'][0]['nest_key'][1][0])

###problem 4
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]

set_list = set(mylist)
print("The unique values of the input list using set()")
mylist = (list(set_list))

for item in mylist:
    print(item)

### problem 5 formatting

age = 45
name = "kyle"

print("hello my dog's name is  {} and he looks {} years old".format(name, age))
