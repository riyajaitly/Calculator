'''
assignment: PA4: Calculator

author: Riya Jaitly

date: November 21, 2022

input: The program asks the user to enter in a mathematical expression.
If the user wishes to quit, they may enter "quit" or "q"

output: The program outputs the answer to the mathematical expression.
If the user enters in "quit" or "q", the program will print "Goodbye!".

'''

from stack import Stack
from tree import BinaryTree, ExpTree


def checkNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def infix_to_postfix(infix):
    prec = {}

    #precedence order of operations
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["^"] = 4
    prec["("] = 1


    opStack = Stack()
    postfixList = []

    #join infix together
    newInfix = ""
    for t in infix:
        if t.isnumeric() or t == ".":
            newInfix = newInfix + t
        else:
            newInfix = newInfix + " " + t + " "

    tokenList = newInfix.split()

    for token in tokenList:
        if checkNumber(token):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)




    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)



#calculates expression
def calculate(infix):
    postFixExpression = infix_to_postfix(infix)
    postfix = postFixExpression.split()
    tree = ExpTree.make_tree(postfix)
    result = ExpTree.evaluate(tree)
    return result

print("Welcome to Calculator Program!")

exitProgram = 0

#if user enters in "quit" or "q", exitProgram is set to 1 and the program stops running
#if the user enters an expression, it keeps running and exitProgram stays equal to 0 until "quit" or "q" is entered
while exitProgram == 0:
    expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
    if expression == "quit" or expression == "q":
        print("Goodbye!")
        exitProgram == 1
        break
    else:
        print(calculate(expression))
    

    

    