# creating a node class
class node:
    def __init__ (self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val 

root = node (1)
root.childleft = node(2)
root.childright = node(3)
root.childleft.childleft = node(4)
root.childleft.childright = node(5) 

print("Inorder Traversal")
# Formula for Inorder - [left,root,right]
def inOrder(root):
    if root:
        inOrder(root.childleft)
        print(root.nodedata)
        inOrder(root.childright) 

inOrder(root) 

print("Preorder Traversal")
# For Preorder - [root,left,right]
def preOrder(root):
    if root:
        print(root.nodedata)
        preOrder(root.childleft)
        preOrder(root.childright) 

preOrder(root) 

print("Postorder Traversal")
# For Postorder - [left,root,right]
def postOrder(root):
    if root:
        postOrder(root.childleft)
        postOrder(root.childright)
        print(root.nodedata)

postOrder(root) 