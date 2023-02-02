MyNumbers = [1,2,3,4,5,6,7,0,0]
HeadIndex = 0
TailIndex = 7
NumberInQueue = 7


def Enqueue(DataToInsert):
    if NumberInQueue > 9:
        return False
    else:
        MyNumbers[TailIndex] = DataToInsert
        TailIndex = TailIndex + 1
        if TailIndex > 9:
            TailIndex = 0
        NumberInQueue = NumberInQueue + 1
        return True


def Dequeue():
    if HeadIndex == 0:
        return -1
    else:
        return MyNumbers[HeadIndex]


MyNumbers = [8,12,13,6,1,50,25,33,11]

def CheckPosition():
    DataToFind = int(input("Enter the number you would like to find:"))
    FoundFlag = False
    i = 0
    while FoundFlag == False and i < 9:
        if MyNumbers[i] == DataToFind:
            FoundFlag = True
        else:
            i = i + 1
    if FoundFlag == False:
        return -1
    elif FoundFlag == True:
        return i + 1


print(CheckPosition())
