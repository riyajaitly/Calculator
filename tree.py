#
# DO NOT FORGET TO ADD COMMENTS
#
from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    #inserting left
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    #inserting right
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        return self.key == obj

    def getRootVal(self):
        return self.key
    
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s
        
class ExpTree(BinaryTree):  
  
    def treeBuild(postfix):
        s = Stack()
        OperatorList = '+/*-^'
        #goes through input 
        for char in postfix:
            #push into stack
            if char not in OperatorList:
                x = BinaryTree(char)
                s.elements.append(x)
            else:
                #pop top 2 nodes
                x = BinaryTree(char)
                x1 = s.pop()
                x2 = s.pop()

                # make children
                x.rightChild = x1
                x.leftChild = x2

                s.elements.append(x)

        #only element root of expression tree
        return x
            

    #traverse from the root to the left subtree then to the right subtree
    def preorder(tree):
        s = ''
        preorderList = []
        
        ExpTree.preorderUtil(tree, preorderList)
        for i in preorderList:
            s = s + str(i)

        return s

    def preorderUtil(tree, preorderList):
        if tree is None:
            return 

        preorderList.append(tree.key)

        ExpTree.preorderUtil(tree.leftChild, preorderList)

        ExpTree.preorderUtil(tree.rightChild, preorderList)

        return

    #traverse from left subtree to the root then to the right subtree
    def inorder(tree):
        s = ''
        inorderList = []

        ExpTree.inorderUtil(tree, inorderList)

        for i in inorderList:
            s = s + str(i)
        return s


    def inorderUtil(tree, inorderList):

        if tree is None:
            return

        
        ExpTree.inorderUtil(tree.leftChild, inorderList)
        inorderList.append(tree.key)
        ExpTree.inorderUtil(tree.rightChild, inorderList)
        return
      
    #traverse from the left subtree to the right subtree then to the root
    def postorder(tree):
        s = ''
        postorderList = []

        ExpTree.postorderUtil(tree, postorderList)
        for i in postorderList:
            s = s + str(i)
        return s

    def postorderUtil(tree, postorderList):

        if tree is None:
            return

        ExpTree.postorderUtil(tree.leftChild, postorderList)

        ExpTree.postorderUtil(tree.rightChild, postorderList)

        postorderList.append(tree.key)

        return

    #evaluates solution using operations
    def solving(tree):
        #tree is empty
        if tree is None:
            return 0
    
        #leaf node
        if tree.leftChild is None and tree.rightChild is None:
            return float(tree.key)
    
        #left tree
        left_sum = ExpTree.evaluate(tree.leftChild)
    
        #right tree
        right_sum = ExpTree.evaluate(tree.rightChild)
    
        #applies operation
        if tree.key == '+':
            return left_sum + right_sum
    
        elif tree.key == '-':
            return left_sum - right_sum
    
        elif tree.key == '*':
            return left_sum * right_sum
    
        elif tree.key == "/":
            return left_sum / right_sum

        else:
            return left_sum ** right_sum

 
            
    def __str__(self):
        return ExpTree.inorder(self)

