# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position == 0: return head.next
    count = 0
    cur = head
    while cur:
        if count == position-1:
            cur.next = cur.next.next
            break
        cur = cur.next
        count+=1
    return head
