#This section is to add quetions and their answers

question_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\questions.txt"
answer_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\answers.txt"

while True:

    f =  open(question_file, "a")
    print()
    question = input("Enter the question: ")
    f.write(question + "\n")
    f.close()

    f =  open(answer_file, "a")
    answer = input("Enter the answer: ")
    f.write(answer + "\n")
    f.close()

    print()
    again = input("Press 'y' to add another question: ")
    if again.upper() != 'Y':
        print("Thanks for adding the question")
        print()
        break