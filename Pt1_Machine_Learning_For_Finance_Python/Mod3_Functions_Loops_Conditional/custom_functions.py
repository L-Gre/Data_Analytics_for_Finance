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