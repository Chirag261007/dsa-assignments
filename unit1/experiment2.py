n = int(input("Enter n: "))

count = 0
for i in range(n):
    count = count + 1
print("Single loop count:", count)

count2 = 0
for i in range(n):
    for j in range(n):
        count2 = count2 + 1
print("Nested loop count:", count2)

count3 = 0
for i in range(n):
    for j in range(i):
        count3 = count3 + 1
print("Triangular loop count:", count3)

count4 = 0
x = n
while x > 0:
    count4 = count4 + 1
    x = x // 2
print("Halving loop count:", count4)