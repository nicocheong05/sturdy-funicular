class node:
    def __init__(self, newData, newNode):
        self.data = newData
        self.nextNode = newNode

linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1),
              node(2,2), node(0,6), node(0,8), node(56,3),
              node(0,9), node(0,-1)]

startPointer = 0
emptyList = 5

def outputNodes():
    index = startPointer
    while index != -1:
        print(linkedList[index].data)
        index = linkedList[index].nextNode


def addNode(linkedList, startPointer, emptyList):
    if emptyList < 0 or emptyList > 9:
        return False, linkedList, startPointer, emptyList
    dataToAdd = input("Data: ")
    thisIndex = startPointer
    nextIndex = linkedList[startPointer].nextNode
    while nextIndex != -1:
        temp = nextIndex
        nextIndex = linkedList[thisIndex].nextNode
        thisIndex = temp
    linkedList[thisIndex].nextNode = emptyList
    nextIndex = emptyList
    linkedList[nextIndex].data = dataToAdd
    emptyList = linkedList[nextIndex].nextNode
    linkedList[nextIndex].nextNode = -1
    return True, linkedList, startPointer, emptyList

outputNodes()

State, linkedList, startPointer, emptyList = addNode(linkedList, startPointer, emptyList)

outputNodes()

if State == True:
    print("Data successfully added.")
else:
    print("Unsuccessful, please try again.")

