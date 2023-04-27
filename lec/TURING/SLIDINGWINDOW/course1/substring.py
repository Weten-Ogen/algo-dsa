def sub(n):
    arr = []
    count=m=0
    for i in range(len(n)):
        for j in range(3):
            count += n[i + j]
            if i + 3 - 1  >= len(n):
              
        
        m = max(m,count)
            

    return m

        
          


print(sub([3,4,5,7,8,10,9]))
print(sub([12,34,5,6,9]))
print(sub([3,6,8,9,10]))