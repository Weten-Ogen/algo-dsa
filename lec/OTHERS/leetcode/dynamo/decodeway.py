def decode(n):
    code= ''
    for i in n:
        val = int(i) + 65  - 1
        code += chr(val) 
    return code
    

print(decode('12'))
print(decode('226'))
print(decode('06'))
