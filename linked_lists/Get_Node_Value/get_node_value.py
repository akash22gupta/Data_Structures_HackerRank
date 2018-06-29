def getNode(head, positionFromTail):
    l1= head
    l2 = head
    for i in range(positionFromTail+1):
        l1=l1.next
    while l1!=None:
        l1=l1.next
        l2=l2.next
    return l2.data
