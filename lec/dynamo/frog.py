def frog(arr,pos):
    ans =[-1] * len(arr)
    if(pos == 0) : return 1
    if(ans[pos] != -1) : return arr[pos]

    cur = 0
    if pos - 1 >= 0  :cur += frog(pos -1)
    if pos - 2 >= 0 :cur += frog(pos - 2)
    ans[pos] = cur
    return ans


print(frog([1,2,3,4],3))
