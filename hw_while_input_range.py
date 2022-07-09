start_n = int(input())
n = start_n
end_n   = int(input())
if n <= end_n:
    while n <= end_n:
        print(n)
        n += 1
else:
    while n >= end_n:
        print(n)
        n -= 1
