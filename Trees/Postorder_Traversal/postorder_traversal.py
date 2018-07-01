def postOrder(root):
    #Write your code here
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root, end = " ")
