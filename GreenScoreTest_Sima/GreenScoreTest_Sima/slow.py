def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def triple_loop(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                print(i, j, k)