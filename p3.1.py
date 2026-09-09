def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    a = 0
    b = 1
    
    for _ in range(n - 2):
        c = a + b # c is the new Fibonacci number
        # Perform the shift: a becomes b, b becomes c
        a, b = b, c
        sequence.append(b)
        
    return sequence

# Example usage:
print(fib(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
