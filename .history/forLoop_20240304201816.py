def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                print(e1,e2)
                matched = True
                break
        if not matched:
            print("not matched")
            return False
    return True
        
L1 = [1,2,3,4,5,6]
L2=[6,1,27,8,9,12]

print(isSubset(L1, L2))