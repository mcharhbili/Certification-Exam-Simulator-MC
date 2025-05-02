
import json
import random
import os

n_questions = int(input("Enter the number of questions: "))
score_to_pass = int(input("Enter the score to pass (out of 100): "))


with open('test.json') as f:
    data = json.load(f)


from collections import OrderedDict

def remove_duplicates(questions):
    seen = set()
    unique_questions = []
    for q in questions:
        if q['question'] not in seen:
            seen.add(q['question'])
            unique_questions.append(q)
    return unique_questions

# Process the data
questions = data['data']
questions = remove_duplicates(questions)

# Replace commas in answers with |
for q in questions:
    q['answers'] = q['answers'].replace(',', '|')

# Print shape
print(f"({len(questions)}, {len(questions[0]) if questions else 0})")



# Convert to list of dictionaries
processed_data = [OrderedDict(q) for q in questions]

random.shuffle(processed_data)






answers = []

def PoseQuestions(start): 

for i in range(n_questions):
    print(f"Question {i+1}:")
    print(processed_data[i]['question'])
    if len(processed_data[i]['answers'].split('|'))>1:
        print("Multiple Choice Question ...")
        

    for j in processed_data[i]['options'].split('|'):
        print(j.strip())

    response = input("Enter your answer: ").split(' ')
    response = '|'.join(sorted(response)).upper()
    
    answers.append(response)
    print("")
    os.system('cls')
    
    print(f"Questions left: {n_questions - (i+1)}")
    
correct = 0
for i in range(n_questions):
    if answers[i] == processed_data[i]['answers']:
        correct += 1




print(f"Correct answers: {correct}/{n_questions}\n")
response = input("Press Enter to continue ...")



for i in range(n_questions):
    print(f"Question {i+1}:")
    print(processed_data[i]['question'])

    for j in processed_data[i]['options'].split('|'):
        print(j.strip())

    print(f"Your response : {answers[i]}")
    print(f"Correct answer : {processed_data[i]['answers']}")
    print(f"Explanation : {processed_data[i]['explanation']}")
    response = input("Press Enter to continue ...")
    os.system('cls')
    
    print(f"Questions left: {n_questions - (i+1)}")


print(f"Correct answers: {correct}/{n_questions}\n")
