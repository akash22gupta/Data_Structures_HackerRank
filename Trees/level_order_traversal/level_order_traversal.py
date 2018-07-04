"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    q = [root]
    while (q):
        if q[0].left:
            q.append(q[0].left)
        if q[0].right:
            q.append(q[0].right)
        print(q[0].info, end = " ")
        q.pop(0)
