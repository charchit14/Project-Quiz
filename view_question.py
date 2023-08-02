#This section is to view the questions and answers

#Listing the files that we need to print
question_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\questions.txt"
answer_file = "C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\answers.txt"

#Accessing the file that contains the questions
f = open(question_file, "r")
read_question = f.readlines()
f.close()

#Accessing the file that contains the answers
f = open(answer_file, "r")
read_answer = f.readlines()
f.close()

#Printing the questions
print()
print("The Questions are: ")
for i in read_question:
    print(i.strip())

print()

#Printing the answers
print("The Answers are: ")
for i in read_answer:
    print(i.strip())

print()

'''Here 'readlines()' reads multiple lines of our file 
And it stores those lines in a list
So, to access and print the elements i.e. lines in the list
we use 'for loop' '''