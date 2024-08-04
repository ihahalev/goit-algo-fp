from fractal import init_pythagoras_tree

def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
            if level <= 0:
                print("Рівень рекурсії повинен бути додатнім.")
            else:
                break
        except ValueError:
            print("Будь ласка, введіть коректне число.")

    init_pythagoras_tree(level)

if __name__ == "__main__":
    main()
