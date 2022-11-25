topic = []
question = []

def ReadQU():
    f = open("ielts.txt", "r")
    while True:
        file_data = f.readline().rstrip()
        if not file_data:
            break
        topic.append(file_data)
        file_data = f.readline().rstrip()
        question.append(file_data)


ReadQU()

unique_topics = []
for i in range(len(topic)):
    if topic[i] not in unique_topics:
        unique_topics.append(topic[i])

import random

print(unique_topics)
chosen_topic = input("Choose a topic from the list above: ")

def select_question(chosen_topic):
    arrayindex_of_topic = []
    for i in range(len(topic)):
        if topic[i] == chosen_topic:
            arrayindex_of_topic.append(i)
    chosen_question = question[random.choice(arrayindex_of_topic)]
    calculate_time()
    print(chosen_question)

def calculate_time():
    time_now = input("Enter the current time in hh:mm format = ")
    minutes = int(time_now[3:]) + 40
    hours = int(time_now[:2])
    if minutes > 59:
        minutes = minutes - 60
        hours = hours + 1
    if minutes == 0:
        minutes = str(minutes) + "0"
    print("You have until", str(hours)+":"+str(minutes), "to complete this question.")

select_question((chosen_topic))

def random_question():
    this_question = random.choice(question)
    return this_question

for i in range(5):
    print(str(i+1)+".",random_question())
