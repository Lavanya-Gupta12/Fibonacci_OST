# Function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    # Handle edge cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Start with first two terms
    fib_series = [0, 1]

    # Generate remaining terms
    for i in range(2, n):
        next_value = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_value)

    return fib_series


# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert number to string and compare with its reverse
    return str(number) == str(number)[::-1]


# ---- Main Program ----

# Take input for Fibonacci series
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Generate Fibonacci series
fib_series = fibonacci_series(num_terms)

# Display result
print("Fibonacci Series:", fib_series)


# Take input for palindrome check
num_to_check = int(input("Enter a number to check if it is a palindrome: "))

# Check and display result
if is_palindrome(num_to_check):
    print(f"{num_to_check} is a palindrome number.")
else:
    print(f"{num_to_check} is not a palindrome number.")
