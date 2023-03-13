def anagram(s,t):
    if len(s) != len(t):
        return False
    else:
        s = sorted(s)
        t = sorted(t)
        if s == t :
            return True
        else:
            return False

   

s = "anagram"
t = "nagaram"
print(anagram(s,t))

s = "rat"
t = "car"
print(anagram(s,t))


s = "madam"
t = "madam"
print(anagram(s,t))