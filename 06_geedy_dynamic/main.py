from greedy import greedy_algorithm
from dynamic import dynamic_programming

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Виведення результатів для різних бюджетів
for budget in [70, 110, 160]:
    print(f"Бюджет: {budget}")

    chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
    print(f"Жадібний алгоритм")
    print(f"Обрані страви: {chosen_items}")
    print(f"Сума калорій: {total_calories}")
    print(f"Витрати з бюджету: {total_cost}")


    chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
    print(f"Динамічне програмування")
    print(f"Обрані страви: {chosen_items}")
    print(f"Сума калорій: {total_calories}")
    print(f"Витрати з бюджету: {total_cost}\n")
