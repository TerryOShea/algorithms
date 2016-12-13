def stock_picker(stock_prices):
    if len(stock_prices) < 2: return 0
    lowest_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for i in range(1, len(stock_prices)): 
        lowest_price = min(lowest_price, stock_prices[i])
        max_profit = max(max_profit, stock_prices[i] - lowest_price)
    
    return max_profit

print(stock_picker([10, 7, 5, 8, 11, 9]))