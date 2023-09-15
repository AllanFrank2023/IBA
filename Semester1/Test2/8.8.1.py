#The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, . . .. 
# Each number in the se­ quence (after the first two) is the sum of the previous two. Write a pro­ gram that computes and outputs the nth Fibonacci number, where n is a
#value entered by the user.

# Funktion til at finde Fibonacci number - det nummer som indtastede
def fibonacci(n):
    if n <= 0:
        return "Ikke gyldigt tal- Indtast et positivt tal"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib = [1, 1]
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[-1]

# Input n fra brugeren
n = int(input("Enter the value of n to find the nth Fibonacci number: "))

# Resultatet nth Fibonacci nummer
result = fibonacci(n)
print("Det", n,".th Fibonacci nummer er: ", result)



def generate_fibonacci(limit):
    fibonacci_numbers = [1, 1]
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fib <= limit:
            fibonacci_numbers.append(next_fib)
        else:
            break
    return fibonacci_numbers

# Input the limit from the user
limit = int(input("Enter the limit for Fibonacci numbers: "))

# Generate and print Fibonacci numbers up to the limit
fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci numbers up to", limit, "are:")
print(fibonacci_sequence)