n = int(input())
l = [] # for main list/stack
m = [] # for maximum element list/stack

for _ in range(n):
    a = input()
    if len(a)>1:
        a,b = map(int,a.split())
    else:
        a = int(a)
    if a ==1:
        l.append(b)
        if m:
            if m[-1]<=b:
                m.append(b)
        else:
            m.append(b)
    if a ==2:
        c = l.pop()
        if m[-1] == c:
            m.pop()
    if a ==3:
        print(m[-1])
