# For loops

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
    calculate_return_on_investment(entry)


# Exercise 

'''
1. Write a for loop that calculates ROl for each list in companies and appends that ROl to each list
        * After this step, each list in companies should contain three objects in the format 
        [current_price, target_price, roi_calculation], which you can check by 
        printing each list and comparing to the prior example
2. Create three new empty lists named current prices, target prices, and roi calculations
3. Write one for loop that iterates through each list in companies and performs the following three actions:
• Append the first object in each list to current_prices
• Append the second object in each list to target_prices
• Append the third object in each list to roi_calculations
4. Print current prices, target prices, and roi calculations
'''

# 1. calc ROI

for entry in companies:
    roi = calculate_return_on_investment(entry)
    entry.append(roi)

for entry in companies:
    print(entry)


# 2. create lists

current_prices = []
target_prices = []
roi_calculations = []


# 3. append ROI to existing lists

for entry in companies:
    current_prices.append(entry[0])
    target_prices.append(entry[1])
    roi_calculations.append(entry[2])
    

# 4. print results

print(current_prices)
print(target_prices)
print(roi_calculations)