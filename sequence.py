import numpy as np
import matplotlib.pyplot as graph  

# Function to generate Fibonacci sequence using binary representation
def fibonacci_binary(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Function to check if a number is a Fibonacci number using Binet's formula
def is_fibonacci_number(n):
    x1 = 5 * (n ** 2) + 4
    x2 = 5 * (n ** 2) - 4
    return int(x1 ** 0.5) ** 2 == x1 or int(x2 ** 0.5) ** 2 == x2

# Function to find the closest Fibonacci number to a given number
def closest_fibonacci(n):
    if n < 0:
        return 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a if (n - a) < (b - n) else b

# Function to express a number as a sum of non-consecutive Fibonacci numbers (Zeckendorf’s theorem)
def fibonacci_sum_representation(n):
    sequence = fibonacci_binary(50)[::-1]  # Generate and reverse Fibonacci sequence
    result = []
    for num in sequence:
        if num <= n:
            n -= num
            result.append(num)
        if n == 0:
            break
    return result

# Function to plot Fibonacci sequence in logarithmic scale
def plot_fibonacci_log(n):
    sequence = fibonacci_binary(n)
    graph.plot(range(n), sequence, marker='o', linestyle='-', color='blue', markersize=6, label="Fibonacci")
    
    graph.xscale("log")
    graph.yscale("log")
    
    graph.title("Fibonacci Sequence in Logarithmic Scale")
    graph.xlabel("Index (log scale)")
    graph.ylabel("Value (log scale)")
    graph.legend()
    graph.grid(True)
    graph.show()

# Main function
def main():
    n = 30  # Number of Fibonacci numbers to generate

    # Generate Fibonacci sequence
    sequence = fibonacci_binary(n)
    print("Fibonacci Sequence:", sequence)

    # Check if a number is a Fibonacci number
    num_to_check = 34
    print(f"Is {num_to_check} a Fibonacci number?", is_fibonacci_number(num_to_check))

    # Find closest Fibonacci number
    num = 50
    closest = closest_fibonacci(num)
    print(f"Closest Fibonacci number to {num}: {closest}")

    # Fibonacci sum representation
    num_to_represent = 45
    representation = fibonacci_sum_representation(num_to_represent)
    print(f"Zeckendorf Representation of {num_to_represent}: {representation}")

    # Plot Fibonacci in log scale
    plot_fibonacci_log(n)

if __name__ == "__main__":
    main()