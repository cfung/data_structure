# python3

import sys, threading
import queue
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

'''
Bredth-First:

if tree = nil: return
Queue q
q.Enqueue(tree)
while not q.Empty() :
    node ← q.Dequeue()
    Print(node)
    if node.left ̸= nil:
        q.Enqueue(node.left)
    if node.right ̸= nil:
        q.Enqueue(node.right)
'''

#  ParentDict = {0: [], 1: [], 2: [], 3:[], 4:[], 5:[]}
ParentDict = {}

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        root = 0
        # create a list
        q = []

        if root is None:
            return 0

        for child in range(self.n):
            ParentDict[child] = []

        for vertex in range(self.n):
            childList = []
            #nodeDict[vertex] = 
            #ParentDict[child].append(vertex)
            if (self.parent[vertex] == -1):
                # root
                root = vertex
            else:
                ParentDict[self.parent[vertex]].append(vertex)

            # this was the previous brute-force way to calculate tree height
            '''
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
            '''
        # add root to list
        q.append(root)

        while(True):

            nodeCount = len(q)
            #print ("what is nodeCount..: ", nodeCount)
            #print ("what is maxHeight (1st while): ", maxHeight)
            if nodeCount == 0:
                return maxHeight

            maxHeight += 1

            while nodeCount > 0:

                nodeIdx = q.pop(0)

                if (len(ParentDict[nodeIdx]) > 0):
                    for node in ParentDict[nodeIdx]:
                        q.append(node)
                
                nodeCount -= 1

        #return maxHeight;

def main():

    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
