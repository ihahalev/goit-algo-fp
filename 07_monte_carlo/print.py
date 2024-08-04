def print_table(sums, probabilities, analytical_probabilities):
    header = ["Сума", "Монте-Карло %", "Аналітична %"]
    width = 52
    print("┌" + "─" * (width - 2) + "┐")
    print_row(header)
    print("├" + "─" * (width - 2) + "┤")

    for sum_value in sums:
        row = [sum_value, f"{probabilities[sum_value]:.2f}", f"{analytical_probabilities[sum_value]:.2f}"]
        print_row(row)

    print("└" + "─" * (width - 2) + "┘")

def print_row(values):
    print("│", end='')
    for value in values:
        print(f"{value:^16}", end='│')
    print()