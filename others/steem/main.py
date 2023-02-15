x =[3,3]

def twoSum(arr, x):
    y = []
    for i in range(0 , len(arr)):
        for j in range(1,len(arr)):
            sum = arr[i] + arr[j]
            if sum == x:
                y.append(i)
                y.append(j)
        return y
        

    
        
          
                

    
print(twoSum(x,6))
