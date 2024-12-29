## Creating custom functions

# Exercise
'''
Create a custom Python function that returns Future Value (FV). 
Use the values below:

    Investment      100
    Growth Rate     0.1
    Years           3 
    FV              133.1

Future Value = Investment * (1 + Growth Rate) ** Years
'''

def future_value(investment, growth_rate, years):
    return round(investment * (1 + growth_rate) ** years, ndigits=1)

future_value(100, 0.1, 3)


# pass list to function

investment_1 = [100, 0.1, 3]

def new_future_value(investment_name):
    return round(investment_name[0] * (1 + investment_name[1]) ** investment_name[2], ndigits=1)

new_future_value(investment_1)


# for loops

# Exercise

jnj = [139.49, 144.20]
unh = [265.31, 284.14]
pfe = [42.96, 43.06]
abbv = [95.68, 107.44]
amgn = [200.58, 205.9]
abt = [68.42, 71.06]

'''
1. Define a new function called calculate_return_on_investment
        The function should accept one argument named price_list
2. The function should return the result of the following formula:
        (target_price - current_price) / current_price
3. Create a list called companies that contains all of the price lists defined
4. Write a for loop that performs the following actions:
        * Iterates through all objects in companies
        * Applies the calculate_return_on_investment function to each object
        * Rounds the result of each calculation to 3 decimal places
        * Prints the rounded result of each calculation
'''

# from decimal import Decimal

def calculate_return_on_investment(price_list) :
    return round((price_list[1] - price_list[0]) / price_list[0], ndigits=3)
    # to calculate % using 'Decimal'
    # return round((Decimal(price_list[1]) - Decimal(price_list[0])) / Decimal(price_list[0]), ndigits=3)*100
    
# test_list = [139.49, 144.2]
# calculate_return_on_investment(test_list)

companies = [jnj,unh,pfe,abbv,amgn,abt]

for entry in companies:
    print(calculate_return_on_investment(entry))