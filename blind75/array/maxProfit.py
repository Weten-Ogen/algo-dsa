# def maxprofit(prices):
#     profit = 0
#     max_index = 0
#     min_index = 0
#     for i in range(len(prices)):
#         if prices[i] > prices[max_index]:
#             max_index = i
#         else: 
#             if prices[i] <= prices[min_index] :
#                 min_index = i
#                 if min_index > max_index:
#                     max_index = i
#     profit = prices[max_index] - prices[min_index]

#     return profit
    
        
# def maxprofit(prices):
#     minx = 0
#     manx = 0
#     profit = 0
#     for i in range(len(prices)):
#         if prices[i] <= prices[minx]:
#             minx = i
#     manx = max(prices[minx:])
#     profit = manx - prices[minx] 
#     return profit
    
def maxprofit(prices):
    minu = min(prices)
    minu_index =prices.index(minu)
    maxu = max(prices[minu_index:])
    profit = maxu - minu
    return profit


    
 





# Example 1

print(f"Ex 1")
print(maxprofit([7,1,5,3,6,4]))


# Example 2

print(f"Ex 2")

print(maxprofit([7,6,4,3,1]))



