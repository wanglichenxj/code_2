"""Sum integers from 1 to 100, printing the running total after each step."""

def main() -> None:
    total = 0
    for n in range(1, 101):
        total += n
        print(f"After adding {n}: sum = {total}")


if __name__ == "__main__":
    main()
