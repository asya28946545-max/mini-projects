mn = [2, 6, 10, 1364, 100000]
mn1 = min(mn)
mn2 = min(elem for elem in mn if elem > min(mn))
print(mn1, mn2)