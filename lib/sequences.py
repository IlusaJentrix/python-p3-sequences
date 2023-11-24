#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(f"Fibonacci sequence up to length {length}:")
    print(fibonacci_sequence[:length])

# Example: Print Fibonacci sequence up to length 9
print_fibonacci(0)


