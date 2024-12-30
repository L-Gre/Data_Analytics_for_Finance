# Conditional logic

# Exercise

'''
1. Create three empty lists named buy_recommendations, hold_recommendations, and sell_recommendations
2. Write a for loop that cycles through all of the keys in roi_dict and completes the following actions:
• If the ROl is greater than 10% (0.10), append the key to buy_recommendations
• If the ROl is less than 10% (0.10) but greater than 5% (0.05), append the key to hold recommendations
• If the ROl is less than 5% (0.05), append the key to sell_recommendations
'''

roi_dict = {
'jnj' : 0.034,
'unh': 0.071,
'pfe': 0.002,
'abbv' : 0.123,
'amgn' : 0.027,
'abt': 0.039
}

buy_recommendations = []
hold_recommendations = []
sell_recommendations = []

for ticker in roi_dict.keys():
    if roi_dict[ticker] > 0.1 :
        buy_recommendations.append(ticker)
    elif roi_dict[ticker] > 0.05 :
        hold_recommendations.append(ticker)
    else : 
        sell_recommendations.append(ticker)
        
print(buy_recommendations)
print(hold_recommendations)
print(sell_recommendations)