def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res=[]
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res


        
L1 = [1,3,2,6,27,56,6,6]
L2=[6,1,27,8,9,12,2]

print(intersect(L1, L2))