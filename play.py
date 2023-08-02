#This program runs the quiz game

import random


question_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\questions.txt"
answer_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\answers.txt"

f1 = open(question_file, "r")
total_question_lines = f1.readlines()
f1.close()

f2 = open(answer_file, "r")
total_answer_lines = f2.readlines()
f2.close()

used_question = set()

score = 0

while len(used_question) < len(total_question_lines):

    choosen_question_line = random.randint(0, len(total_question_lines) - 1)    

    if choosen_question_line not in used_question:
        used_question.add(choosen_question_line)

        choosen_question = total_question_lines[choosen_question_line]
        choosen_answer = total_answer_lines[choosen_question_line]

        print()
        print(f"Your question is:\n {choosen_question}")
        user_input = input("Enter your answer ('q' to quit): ")

        if user_input.lower() == 'q':
            break

        if user_input.strip().lower() == choosen_answer.strip().lower():
            print("Your answer is correct")
            score += 1
            print()

        else:
            print(f"Wrong answer. The correct answer is: {choosen_answer}")
            print()

else:
    print(f"All questions answered. Your score is: {score}")
    print()


#Section that opens the 'score' file and compares the old score with new score
f = open("C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\score.txt",'r')
old_score = f.read()

if old_score == '':
    old_score = 0

if score > int(old_score) :
    print(f"Congratulations. You set a new high score of {score}")
    print()
    
    with open("C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\score.txt",'w') as file:
        file.write(str(score))

elif score == int(old_score):
    print(f"Your score equals the high score which is {score}")
    print()

else:
    print(f"Sorry! You coudldn't set a high score. The high score is: {old_score}")
    print()

f.close()