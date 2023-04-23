def reorder(n):
    last = -1
    curr = 0
    l = list(n)
    # loop through
    for letter in l:
        if not letter.isalpha():
            continue
        else:
            l[curr],l[last] = l[last],l[curr]
    return ''.join(l)

            

            
    # if not alpha stop
    pass






# test 
n = 'ab-cd'
m = 'ab-ecf'
print(reorder(n))
print(reorder(m))