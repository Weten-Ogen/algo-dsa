def maxprofit(prices):
    profit = 0
    max_index = 0
    min_index = 0
    for i in range(len(prices)):
        # update max if needed
        if prices[i] > prices[max_index]:
            max_index = i
        # update min if needed
        else: 
            if prices[i] <= prices[min_index] :
                min_index = i
                if min_index > max_index:
                    max_index = i
    profit = prices[max_index] - prices[min_index]
    return profit
        







# Example 1

print(f"Ex 1")
print(maxprofit([7,1,5,3,6,4]))

print()

# Example 2

print(f"Ex 2")
print()

print(maxprofit([7,6,4,3,1]))
