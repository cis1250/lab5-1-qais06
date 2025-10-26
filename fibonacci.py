#!/usr/bin/env python3

# Fibonacci sequence with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
    """Ask the user for a positive integer and validate it."""
    while True:
        try:
            n = int(input("Enter how many Fibonacci terms you want: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def print_fibonacci(seq):
    """Print the Fibonacci sequence neatly."""
    print("Fibonacci sequence:")
    print(", ".join(str(num) for num in seq))


def main():
    n = get_user_input()
    sequence = generate_fibonacci(n)
    print_fibonacci(sequence)


if __name__ == "__main__":
    main()
