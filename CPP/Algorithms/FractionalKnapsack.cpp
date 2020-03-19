#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int get_max_index(vector<float> arr, int n, vector<float> check_list)
{
    int max_value = -1, max_index = -1;
    for (int i = 0; i < n; i++)
    {
        if (max_value < arr[i] && check_list[i] == 0)
        {
            max_value = arr[i];
            max_index = i;
        }
    }
    return max_index;
}

vector<float> fractional_knapsack(vector<int> Weights, vector<int> Profits, int Max_weight)
{
    int n = Weights.size();
    float Total_profit = 0;
    vector<float> Final_list(n + 1, 0), Profit_per_weight(n);
    for (int i = 0; i < n; i++)
        Profit_per_weight[i] = Profits[i] / Weights[i];
    while (Max_weight > 0)
    {
        int max_index = get_max_index(Profit_per_weight, n, Final_list);
        if (Max_weight - Weights[max_index] >= 0)
        {
            Max_weight -= Weights[max_index];
            Total_profit += Profits[max_index];
            Final_list[max_index] = 1;
        }
        else
        {
            float Profit_ratio = Max_weight / Weights[max_index];
            Total_profit += Profit_ratio * Profits[max_index];
            Final_list[max_index] = Profit_ratio;
            break;
        }
    }
    Final_list[n + 1] = Total_profit;
    return Final_list;
}

// Test Code

int main()
{
    vector<int> Profits{1, 2, 3};
    vector<int> Weights{2, 4, 6};
    int Max_weight = 7;
    vector<float> final_list = fractional_knapsack(Weights, Profits, Max_weight);
    cout << "List : ";
    for (int i = 0; i < Weights.size(); i++)
        cout << final_list[i] << ' ';
    cout << endl
         << "Max Profit : " << final_list[Weights.size() + 1];
    return 0;
}