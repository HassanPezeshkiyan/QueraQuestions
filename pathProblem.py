def subset(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)


data = input().split(' ')
print(subset((int(data[0])+int(data[1])), int(data[0])))
