
import json
from math import sqrt
import random
import os
from collections import OrderedDict
import time

n_questions = int(input("Enter the number of questions: "))
score_to_pass = int(input("Enter the score to pass (out of 100): "))
time_to_pass = int(input("Enter the time to pass (in minutes): "))
input("Press Enter to start ...")
start_time = time.time()
os.system('cls')
current_question = 0
with open('test.json') as f:
    data = json.load(f)

def printReview():
    k = int(sqrt(n_questions))
    line = ""
    print("Review Questions : ")
    print("+ : Question Answered")
    print("- : Question Not Answered")
    print("* : Question to be reviewed")
    for i in range(n_questions):
        symbol = ''
        if 'review_later' in processed_data[i].keys() and processed_data[i]['review_later']:
            symbol = "*"
        elif 'response' in processed_data[i].keys() and processed_data[i]['response'] != "":
            symbol = "+"
        else:
            symbol = "-"

        a = f"{symbol}{i+1}\t"
        line += a
        if (i+1)%k==0:
            print(line)
            line = ""
            
    print(line)
    question_number = int(input("Enter the question number to review: "))
    os.system('cls')
    return question_number
    
        
            
    

def printOptions():
    if current_question == 0:
        print("")
        print(" -- 1. Next")
        print(" -- 2. Review")
        print(" -- 3. Submit")
        print(" -- 4. Add to Review Later and Go Next")
        print(" -- 5. Remove from Review Later and Go Next")
        choice = input("    Enter your choice: ")
        options = ['1', '2', '3', '4','5']
        while choice not in options:
            choice = input("    Enter your choice: ")
        os.system('cls')
        return choice
    else:
        print("")
        print(" -- 0. Previous")
        print(" -- 1. Next")
        print(" -- 2. Review")
        print(" -- 3. Submit")
        print(" -- 4. Add to Review Later and Go Next")
        print(" -- 5. Remove from Review Later and Go Next")
        choice = input("    Enter your choice: ")
        options = ['0', '1', '2', '3', '4','5'] 
        while choice not in options:
            choice = input("    Enter your choice: ")
        os.system('cls')
        return choice

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




# Convert to list of dictionaries
processed_data = [OrderedDict(q) for q in questions]

random.shuffle(processed_data)




answers = []

def PoseQuestions(cu): 
    # for i in range(n_questions):
    print(f"Questions left: {n_questions - (cu+1)}")
    duration = time_to_pass*60-(time.time() - start_time)
    hours, remainder =  divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time left: {int(hours)}:{int(minutes)}:{int(seconds)}")
    if len(processed_data[cu]['answers'].split('|'))>1:
        print(f"{cu+1}. {processed_data[cu]['question']} (Multiple Choice Question ...)")
    else:
        print(f"{cu+1}. {processed_data[cu]['question']}")

    for j in processed_data[cu]['options'].split('|'):
        print(f"\t{j.strip()}")

    response = input("Enter your answer: ").split(' ')
    response = '|'.join(sorted(response)).upper()
    
    processed_data[cu]['response'] = response
    
    return printOptions()    
        


        
        
a = 0

while a != '3':
    a = PoseQuestions(cu=current_question)
    if a == '1':
        current_question += 1
    elif a == '0':
        current_question -= 1
    elif a == '2':
        current_question = printReview()-1
    elif a == '4':
        processed_data[current_question]['review_later'] = True
        current_question += 1
    elif a == '5':
        processed_data[current_question]['review_later'] = False
        current_question -= 1
    

end_time = time.time()
total_time = (end_time - start_time)/60

correct = 0
for i in range(n_questions):
    if 'response' in processed_data[i].keys() and processed_data[i]['response'] == processed_data[i]['answers']:
        correct += 1
print(f"Result: {correct}/{n_questions}")
print(f"Time Spent: total_time")
if total_time > time_to_pass:
    print("You failed the test. Time limit exceeded.")
else:  
    if correct < score_to_pass:
        
        print("You failed the test.")
    else:
        print("You passed the test.")



response = input("Press Enter to continue to Review the Questions ...")
os.system('cls')


for i in range(n_questions):
    print(f"Question {i+1}:")
    print(processed_data[i]['question'])

    for j in processed_data[i]['options'].split('|'):
        print(j.strip())
    if not 'response' in processed_data[i].keys():
        processed_data[i]['response'] = None
    print(f"Your response : {processed_data[i]['response']}")
    print(f"Correct answer : {processed_data[i]['answers']}")
    print(f"Explanation : {processed_data[i]['explanation']}")
    response = input("Press Enter to continue ...")
    os.system('cls')
    