def paly(s):
    if len(s) == 0 or len(s) == 1: return True
 
    if s[0] == s[(len(s) - 1)] : return paly(s[1:len(s)-1])
    return False

print(paly('madam'))