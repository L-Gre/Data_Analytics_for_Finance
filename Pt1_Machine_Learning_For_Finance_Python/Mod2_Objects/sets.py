## sets

list_1 = ['a', 'a', 'b', 'b', 'c', 'c']
set_1 = {'a', 'a', 'b', 'b', 'c', 'c'}

print(list_1)
print(set_1)

list_1 = ['IT', 'Consumer', 'IT', 'IT', 'Financials']
set_1 = {'IT', 'Consumer', 'IT', 'IT', 'Financials'}

print(list_1)
print(set_1)

set(list_1)

mkt_cap_over_500 = {'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'BRK/A'}
Aaa_rated = {'MSFT', 'JNJ', 'XOM'}

# Combine sets with union() - order doesn't matter
print (mkt_cap_over_500.union (Aaa_rated))
print (Aaa_rated.union(mkt_cap_over_500))

# Find common elements with intersection() - order doesn't matter
# in a venn diagram of two circles, it's the area inside both circles
print (mkt_cap_over_500.intersection(Aaa_rated))

# Find different elements with .difference() - order matters
# in venn diagram of two circles, it's the outside area of the LEFT circle
# how is THIS different from THAT
print(mkt_cap_over_500.difference(Aaa_rated))

# Exercise

'''
# Healthcare Companies: 'JNJ', 'UNH', 'PFE', 'ABBV', 'AMGN', 'ABT'
# Companies with Beta > 1: 'ABBV', 'AMGN', 'ABT', 'NFLX', 'NVDA'

First, create a set for each group of companies. 

Then, using .union( ), intersection( ), and .difference( ), answer the following questions:
    1. What are all of the companies included in both sets?
    2. Which healthcare companies have a beta > 12
    3. Which healthcare companies have a beta < 1?
'''

healthcare_companies = {'JNJ', 'UNH', 'PFE', 'ABBV', 'AMGN', 'ABT'}
beta_min1 = {'ABBV', 'AMGN', 'ABT', 'NFLX', 'NVDA'}

print(healthcare_companies.union(beta_min1))
print(healthcare_companies.intersection(beta_min1))
print(healthcare_companies.difference(beta_min1))