def recur_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = recur_sum(n) + recur_sum(n-1)

# well i tried...

print(recur_sum(3))
