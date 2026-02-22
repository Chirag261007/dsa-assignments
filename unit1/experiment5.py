total = 0

def toh(n, s, h, d):
    global total
    if n == 1:
        print("Move disk 1 from", s, "to", d)
        total = total + 1
        return
    toh(n - 1, s, d, h)
    print("Move disk", n, "from", s, "to", d)
    total = total + 1
    toh(n - 1, h, s, d)


n = int(input("Enter number of disks: "))
toh(n, "A", "B", "C")
print("Total moves:", total)