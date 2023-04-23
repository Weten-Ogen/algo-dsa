def frog(arr,pos):
    ans =[-1] * len(arr)
    if(pos == 0) : return 1
    if(ans[pos] != -1) : return arr[pos]
    
    


print(frog([1,2,3,4],3))
