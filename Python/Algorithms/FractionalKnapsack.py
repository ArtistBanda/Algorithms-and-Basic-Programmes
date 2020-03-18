""" 
In Fractional Knapsack, we can break items for maximizing the total value of knapsack.
This problem in which we can break an item is also called the fractional knapsack problem.

(Greedy Approach)
"""


def get_max_val(arr, n, check_list):
    max_val = max_index = -1
    for x in range(1, n):
        if max_val < arr[x] and check_list[x] == 0:
            max_val = arr[x]
            max_index = x
    return max_index


def max_profit(Weights, Profits, Max_weight):
    Profit_per_weight = [
        weight / profit for (weight, profit) in zip(Weights, Profits)]
    n = len(Weights)
    Total_profit = 0
    Final_list = [0] * n
    while Max_weight > 0:
        max_index = get_max_val(Profit_per_weight, n, Final_list)
        if Max_weight - Weights[max_index] >= 0:
            Max_weight -= Weights[max_index]
            Total_profit += Profits[max_index]
            Final_list[max_index] = 1
        else:
            Profit_ratio = Max_weight / Weights[max_index]
            Total_profit += Profit_ratio * Profits[max_index]
            Final_list[max_index] = Profit_ratio
            break
    return (Total_profit, Final_list)


# Test Code

Weights = list(map(int, input("Enter the weights\n").split()))
Profits = list(map(int, input("Enter the Profits\n").split()))
Max_weight = int(input("Enter the max weight\n"))
Profit, Final_list = max_profit(Weights, Profits, Max_weight)
print("Profit : " + str(Profit))
print("List : " + str(Final_list))
