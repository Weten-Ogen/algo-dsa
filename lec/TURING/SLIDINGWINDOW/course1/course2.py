# DYNAMIC SIZE SLIDING WINDOW
from collections import defaultdict

def fruits(trees):
    treeTypesMap = {}
    m = start = 0
    for end,treeType in enumerate(trees):
        if len(trees) < 2 and not (treeTypesMap[treeType]):
            treeTypesMap[treeType] = True
            m = max(m, end - start + 1 )
        elif treeTypesMap[treeType]:
           m = max(m,end- start + 1) 
        else:
            treeTypesMap = {}
            treeTypesMap[trees[end - 1]] = True
            treeTypesMap[treeType] = True
            start = end - 1

            
