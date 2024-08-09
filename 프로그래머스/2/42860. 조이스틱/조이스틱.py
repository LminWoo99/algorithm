def solution(name):
    a=0
    b=len(name)-1
    for idx, spell in enumerate(name):
        a += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        next=idx+1
        while next<len(name) and  name[next]=='A':
            next+=1
        b=min(b,2*idx+len(name)-next, idx+2*(len(name)-next))
    return a+b