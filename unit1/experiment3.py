def fact(n):
    if n < 0:
        print("Invalid")
        return None
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


num = int(input("Enter number: "))
ans = fact(num)
print("Factorial is:", ans)