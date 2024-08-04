def dynamic_programming(items:dict, budget:int):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    
    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [item]

    total_cost = sum(items[item]['cost'] for item in selected_items[budget])

    return selected_items[budget], dp[budget], total_cost
