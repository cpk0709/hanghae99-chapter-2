class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def createNode(self,node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def printLinkedList(self):
        string = ""
        cur = self.head

        while cur:
            string += str(cur.data)
            if cur.next != None:
                string += '->'
            cur = cur.next
        print(string)


def mergeLinkedList(a,b):
    aFin = a.head
    # string = ""
    bCur = b.head
    while aFin:
        # string += str(aCur.data)
        # if aCur.next:
        #     # aCur = aCur.next
        #     string += "=>"
        aFin = aFin.next
    # print(string)

    aFin = bCur
    print(aFin.data)

    # while bCur:





link1 = LinkedList()
link1.createNode(Node(1))
link1.createNode(Node(2))
link1.createNode(Node(4))
# link1.printLinkedList()

link2 = LinkedList()
link2.createNode(Node(1))
link2.createNode(Node(3))
link2.createNode(Node(4))
# link2.printLinkedList()

mergeLinkedList(link1,link2)