def generate_fibonacci(n_terms):
    # Validate input
    if n_terms <= 0:
        return "Number of terms must be a positive integer."
    
    if n_terms == 1:
        return [0]
    if n_terms == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    

    while len(fib_sequence) < n_terms:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        sequence = generate_fibonacci(num_terms)
        print("Fibonacci sequence:")
        print(sequence)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
