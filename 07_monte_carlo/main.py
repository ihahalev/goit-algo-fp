import matplotlib.pyplot as plt
from monte_carlo import monte_carlo_dice_throws
from print import print_table

# Аналітичні ймовірності
analytical_data = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

def main():
    num_rolls = 1000000  # Кількість кидків
    expectancy = monte_carlo_dice_throws(num_rolls)

    sums = list(range(2, 13))
    # Вивід результатів в таблиці
    print_table(sums, expectancy, analytical_data)

    # Побудова графіку
    plt.figure(figsize=(10, 6))
    plt.plot(sums, [analytical_data[sum] - expectancy[sum] for sum in sums])

    plt.xlabel('Сума на кубиках')
    plt.ylabel('Різниця ймовірностей %')
    plt.title('Різниця ймовірностей аналітичних даних та за методом Монте-Карло')  
    plt.grid(True)  

    plt.show()

if __name__ == "__main__":
    main()
