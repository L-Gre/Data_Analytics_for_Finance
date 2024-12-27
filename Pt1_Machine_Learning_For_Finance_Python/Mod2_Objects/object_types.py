## Object Types

# check type of object

print(type(5))
print(type(5.0))
print(type('5'))


## Lists

# access elements in a list

list_1 = [1, 2, 3, 4, 5]

# access one element
print (list_1[0])

# access multiple elements
print (list_1[1:3])

# calculations using list elements
print (list_1[3] + list_1[4])

# Exercise
'''
1. Create a list called list_1 containing the integers 1, 2, 3, 4, and 5
2. Create a list called list_2 containing the integers 6, 7, 8, 9, and 10
3. Print the sum of the 4th object in list 1 and the 1st object in list 2
4. Print the last two objects (as a range) in list_1 and the first three objects (as a range) in list_2
5. Create a list called list_3 containing the objects from Step 4 in numerical order and print the result
'''

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

print("The sum is {}".format(list_1[3]+list_2[0]))
print(list_1[3:], list_2[:3])

list_3 = list_1[3:] + list_2[:3]
print(list_3)

# set new value for list item
tech_portfolio = ['AAPL', 'AMZN', 'MSFT', 'tbd', 'GOOGL']
tech_portfolio[3] = 'CSCO'
print(tech_portfolio)

# add list value
tech_portfolio.append('NVDA')
print(tech_portfolio)

# remove list value
tech_portfolio.remove('AMZN')
print(tech_portfolio)

# tuples
# sets
# dictionaries