import sys
def check(target, a):
    for i in range(0, len(a), 3):
        if all(tmp==target for tmp in a[i:i+3]):
            return True
    for i in range(0,3):
        if all(tmp==target for tmp in a[i:i+7:3]):
            return True
    if all(tmp==target for tmp in a[0:9:4]):
            return True
    if all(tmp==target for tmp in a[2:7:2]):
            return True
    return False
while True:
    a=input().rstrip()
    if a=='end':
        break
    x_count=a.count('X')
    o_count=a.count('O')
    if x_count-1==o_count:
        if check('X', a) and not check('O', a):
            print("valid")
        elif not check('X', a) and not check('O', a) and a.count('.')==0:
            print("valid")
        else:
            print("invalid")
    elif x_count==o_count:
        if not check('X', a) and check('O', a):
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")