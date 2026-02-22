calls1 = 0

def fib(n):
    global calls1
    calls1 = calls1 + 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


calls2 = 0
store = {}

def fib2(n):
    global calls2
    calls2 = calls2 + 1
    if n in store:
        return store[n]
    if n <= 1:
        store[n] = n
    else:
        store[n] = fib2(n - 1) + fib2(n - 2)
    return store[n]


n = int(input("Enter n: "))

print("Naive answer:", fib(n))
print("Naive calls:", calls1)

print("Memo answer:", fib2(n))
print("Memo calls:", calls2)