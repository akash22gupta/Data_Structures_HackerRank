n = int(input())

l =[]   #main list as stack
tt=[]   #list as stack for opeartions 1 and 2
t = []  #list for storing deleted items in main list(stack)

for _ in range(n):          # loop to take inputs n times(n operations)
    a = input()             # whole input as string in a
    if len(a)>1:            # if two arguments then split it
        a,b = a.split()
    if a == '1':            # checking if operation 1
        tup=(1,len(b))      # storing the opeation number and length of input string in a tuple
        tt.append(tup)      # pushing/appending the tuple in stack/list tt
        for i in b:         # pushing/appending the string W at the end of stack/list
            l.append(i)
    elif a == '2':          # checking if operation 2
        for _ in range(int(b)):
            t.append(l.pop()) # deleting/poping the last k characters of S from list/stack and  also storing the deleted string in another temp list
        tup = (2,t[:])        # storing the opeation number and list t in a tuple
        t.clear()             # emptying the list t
        tt.append(tup)        # pushing/appending the tuple in stack/list tt
        # print(l)
        # print(t)
    elif a == '3':          # checking if operation 3
        print(l[int(b)-1])  # printing the Kth char
    elif a == '4':          # checking if operation 4
        p = tt.pop()        # poping the last tuple and storing in p
        if p[0] == 1:       # checking the last opeartion
            # print(lb)
            # print(l)
            for _ in range(p[1]):   # since the last operation is append then we undo it by poping last elements
                l.pop()
        else:
            for _ in range(len(p[1])): # if the last operation is deletion then we append the main list by poping the elemnts from temp list
                l.append(p[1].pop())



        
