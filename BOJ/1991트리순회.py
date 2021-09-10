import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    print(node.data, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end = '')
    if node.right != '.':
        inorder(tree[node.right])
        
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.data, end='')
    
n = int(input())
tree = {}

for _ in range(n):
    node, left, right = map(str,input().split())
    tree[node] = Node(data=node,left=left, right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])


"""
def preorder(node):
    left, right = tree[node]
    print(node, end='')
    if left != '.':
        preorder(left)
    if right !=  '.':
        preorder(right)
    
def inorder(node):
    left, right = tree[node]
    if left != '.':
        inorder(left)
    print(node, end='')
    if right !=  '.':
        inorder(right)

def postorder(node):
    left, right = tree[node]
    if left != '.':
        postorder(left)
    if right !=  '.':
        postorder(right)
    print(node, end='')
 
n = int(input())
tree = {}

for _ in range(n):
    node, left, right = map(str,input().split())
    tree[node] = [left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

"""