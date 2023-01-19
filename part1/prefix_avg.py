def prefix_avg(S):
    n = len(S)
    A = [0] * n 
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)
    return A

a = [1,2,3,4]
print(prefix_avg(a))

