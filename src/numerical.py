def fibonacci_sum(n):
    """
    This function takes a number n, generates the fibonacci sequence that is n long, 
    and returns the sum of those numbers.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return sum(fib_sequence)
    

if __name__ == "__main__":
    print(fibonacci_sum(0))
    print(fibonacci_sum(1))
    print(fibonacci_sum(2))
    print(fibonacci_sum(5))
    print(fibonacci_sum(10))