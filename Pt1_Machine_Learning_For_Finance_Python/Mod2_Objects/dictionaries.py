## dictionaries

# Exercise

'''
1. Define 6 lists using the data table
• Use company tickers for variable names (NOT A STRING)
• The first object in each list should be the company's current price, and the second object in each list should be the price target
2. Create a dictionary called price_dict with 6 items
The key for each item should be a string of the company ticker
• The value for each item should be the list defined in Step 1
3. Print the entire value for PFE
4. Print only the price target for AMGN

# Company Ticker
# Current Price
# 1-Year Price Target
      
JNJ                 139.49    144.20
UNH                 265.31    284.14    
PEE                  42.96     43.06
ABBV                 95.68    107.44
AMGN                200.58    205.90
ABT                  68.42     71.06
'''

JNJ = [139.49, 144.20]
UNH = [265.31, 284.14]
PFE = [42.96, 43.06]
ABBV = [95.68, 107.44]
AMGN = [200.58, 205.90]
ABT = [68.42, 71.06]

price_dict = {'JNJ':JNJ, 'UNH':UNH, 'PFE':PFE, 'ABBV':ABBV, 'AMGN':AMGN, 'ABT':ABT}
price_dict['PFE']
price_dict['AMGN'][1]

# Exercise
'''
1. Create a new item called 'MRK' with current price 69.98 and target price 74.53, and then print the entire value of 'MRK'
2. Remove 'JNJ' and print the dictionary keys
'''

price_dict['MRK'] = [69.98, 74.53]
price_dict['MRK']

del price_dict['JNJ']
price_dict.keys()