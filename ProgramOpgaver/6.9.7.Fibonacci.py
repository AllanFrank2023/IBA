#Write a function to compute the nth Fibonacci number. 
# Use your function to solve Programming Exercise 16 from 
# Chapter 3.
#






# Funktion til at finde det Fibonacci tal nummer ?? - Bruger indtastede
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
n = int(input("Indtast det nummer på Fabonacci tal du ønsker: "))

# Resultatet nth Fibonacci nummer
result = fibonacci(n)
print("Det", n,".th Fibonacci nummer er: ", result)

##########################################################
#### Indtast X tal og få fremvist underliggende fabonacci tal

def generate_fibonacci(limit):
    fibonacci_numbers = [1,1]
    while True:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fib <= limit:
            fibonacci_numbers.append(next_fib)
        else:
            break
    return fibonacci_numbers

# Input the limit from the user
limit = int(input("Indtast det ønskede tal og få fremvist de underliggende Fabonacci tal: "))

# Generate and print Fibonacci numbers up to the limit
fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci op til tal", limit, "er:")
print(fibonacci_sequence)

############Færdig