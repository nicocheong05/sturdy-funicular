class Card:
    def __init__(self, NewTerm, NewDefinition, NewTopic):
        self.__term = NewTerm     # string
        self.__definition = NewDefinition     # string
        self.__topic = NewTopic     # string

    def GetDefinition(self):
        return self.__definition

    def GetTopic(self):
        return self.__topic

    def GetDetails(self):
        return self.__definition, self.__topic

    def GetTerm(self):    # additional Get method that I added
        return self.__term

glossary = []


try:
    f = open("aleveldefinitions.txt", "r")
    while True:
        ThisTerm = f.readline().rstrip()
        if ThisTerm == "":
            break
        ThisDefinition = f.readline().rstrip()
        ThisTopic = f.readline().rstrip()
        glossary.append(Card(ThisTerm, ThisDefinition, ThisTopic))
    f.close()
except FileNotFoundError:
    print("Sorry, your file could not be found.")


TopicsAvailable = []     # 1d array

def OutputTopics():
    for i in range(len(glossary)):
        ThisCard = glossary[i]
        if ThisCard.GetTopic() not in TopicsAvailable:
            TopicsAvailable.append(ThisCard.GetTopic())

OutputTopics()

print("All topics: ")
for i in range(len(TopicsAvailable)):
    print(TopicsAvailable[i])

def FindTerms():
    TopicWanted = input("\nEnter topic: ")
    for x in range(len(glossary)):
        if TopicWanted == glossary[x].GetTopic():
            print(glossary[x].GetTerm())

import random

def GuessTheTerm():
    RandomIndex = random.randint(0,len(glossary)-1)
    GuessDefinition = glossary[RandomIndex].GetDefinition()
    print("\n")
    print(GuessDefinition)
    UserGuess = input("Guess the term: ")
    if UserGuess == glossary[RandomIndex].GetTerm():
        return True
    else:
        return False


def Game():
    lives = 3
    points = 0
    while lives > 0:
        Correct = GuessTheTerm()
        if Correct == True:
            points = points + 10
            print("Correct! 10 points to Ravenclaw!")
        else:
            lives = lives - 1
            print("Incorrect! You lose a life :(")
        print("Current number of points: " + str(points))
        print("Current number of lives: " + str(lives))
    print("Game Over. You have 0 lives left.")

Game()
