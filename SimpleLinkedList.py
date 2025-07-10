class linkedListsNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedListsNode("1")
node2 = linkedListsNode("2")
node3 = linkedListsNode("3")
node4 = linkedListsNode("4")
node5 = linkedListsNode("5")
node6 = linkedListsNode("6")
node7 = linkedListsNode("7")
node8 = linkedListsNode("8")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8

currentNode = node1
while True:
    print(currentNode.value, ">>>", end= ' ')

    if currentNode.nextNode is None:
        print("None")
        break

    currentNode = currentNode.nextNode
