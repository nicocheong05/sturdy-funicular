class TreasureChest:
    def __init__(self, question, answer, points):
        self.question = question     #question = STRING
        self.answer = answer        #answer = INTEGER
        self.points = points        #points = INTEGER

    def __repr__(self):
        return self.question

    def getQuestion(self):
        return self.question

    def checkAnswer(self, attempt):
        if attempt == self.answer:
            return True
        else:
            return False

    def getPoints(self, count):
        if count == 1:
            return self.points
        elif count == 2:
            return int(self.points/2)
        elif count == 3 or count == 4:
            return int(self.points/4)
        else:
            return 0

arrayTreasure = []

def readData():
    try:
        f = open("TreasureChestData.txt","r")
        while True:
            this_question = f.readline()
            if not this_question:
                break
            this_answer = f.readline()
            this_points = f.readline()
            question = this_question
            answer = this_answer
            points = this_points
            arrayTreasure.append(TreasureChest(question, answer, points))
    except FileNotFoundError:
        print("File cannot be found.")

readData()
print(arrayTreasure)
question_choice = int(input("Choose a question. Enter a number from 1 to 5"))
array_index = question_choice - 1
print(arrayTreasure[array_index])
