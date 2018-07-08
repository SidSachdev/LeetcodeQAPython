# Fibonacci

"""
Using Recursion
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))


"""
Using Dynamic Programming
"""

def fibonacci2(n):
    # Taking 1st two fibonacci nubers as 0 and 1
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

        FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
        return FibArray[n]


print(fibonacci2(4))