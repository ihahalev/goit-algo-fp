import random

def monte_carlo_dice_throws(num_throws: int):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    probabilities = {sum_val: count / num_throws * 100 for sum_val, count in sums_count.items()}
    return probabilities
