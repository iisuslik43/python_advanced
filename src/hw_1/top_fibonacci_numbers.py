def top_fibonacci_numbers(n):
    numbers = [0, 1]
    for _ in range(n - 2):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers[:n]
