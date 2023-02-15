# Best time to buy and sell

def maxProfit(prices):
    sml_val = prices[0]
    profit = 0
    largest_val = 0
# find the smallest val  in the array's index
    for i in range(0,len(prices)):
        if prices[i] < sml_val:
            sml_val = i
    
# Find the largest val in the remainder
    for k in range(sml_val,len(prices)):
        if largest_val< prices[k]:
            largest_val = prices[k]
    
# calculate the profit (p = largest - smallest)
    profit = largest_val - prices[sml_val]
    return profit
   

a = [7,1,5,3,6,4]
print(maxProfit(a))

b = [7,6,4,3,1]
print(maxProfit(b))