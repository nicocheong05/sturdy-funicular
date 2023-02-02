import random

MyArray = [[0 for i in range(10)]for i in range(10)]

for i in range(10):
    for j in range(10):
        MyArray[i][j] = random.randint(1,100)

def OutputArray():
    for n in range(10):
        print(MyArray[n])

OutputArray()

ArrayLength = 10

for x in range(0, ArrayLength):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if MyArray[x][z] > MyArray[x][z+1]:
                TempValue = MyArray[x][z]
                MyArray[x][z] = MyArray[x][z+1]
                MyArray[x][z+1] = TempValue

print("\n")

OutputArray()


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = int((Lower + (Upper - 1))/2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


print(BinarySearch(MyArray, 0, 10, 77))
