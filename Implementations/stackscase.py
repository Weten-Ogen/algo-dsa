from myarray import ArrayStack
s = ArrayStack()

# Parenthesis matching

def matching(expr):
    lefty = '({['
    righty = ")}]"
    s = ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if not righty.index(c) == lefty.index(s.pop()):
                return False
    return s.is_empty()
print(matching('{[()]}'))