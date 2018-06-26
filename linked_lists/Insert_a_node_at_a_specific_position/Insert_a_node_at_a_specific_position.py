# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    if position == 0:
        node = SinglyLinkedListNode(data)
        node.next = head
        return node
    cur = head
    count = 0
    while cur:
        if count == position-1:
            node = SinglyLinkedListNode(data)
            node.next=cur.next
            cur.next = node
            node.next = cur.next.next
        count +=1
        cur = cur.next
    return head
