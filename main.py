#This is the home section of the quiz game

import subprocess   #To call another program from this program
import os           #To put the text in the center of the terminal

while True:
    
    def center_text(any_string):
        terminal_width = os.get_terminal_size().columns             #This calculates the total size of our terminal
        padding_width = (terminal_width - len(any_string)) // 2     #This will get us the remaining size after putting the message 
        padding = " " * int(padding_width)                          #This tells to put spaces " " in either side of the text
        return f"{padding}{any_string}"                             #Finally, message is put after the spaces

    message1 = "*** THIS IS A QUIZ GAME ***"
    message2 =  "Choose from the available options"

    print()
    print(center_text(message1))
    print()
    print(center_text(message2))
    print("1. Play Quiz\n2. View High Score\n3. Add Question\n4. View Questions\n5. Exit")
    print()
    
    #This is the main section of code i.e. to get input and take actions accordingly
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        subprocess.run(["python", "play.py"])

    elif user_choice == 2:
        subprocess.run(["python", "view_score.py"])

    elif user_choice == 3:
        subprocess.run(["python", "add.py"])

    elif user_choice == 4:
        subprocess.run(["python", "view_question.py"])

    elif user_choice == 5:
        print("Thank You! Visit Again.")
        print()
        exit()

    else:
        print("Invalid Input")

    #Section to re-run the program
    print()
    again = input("Press 'y' to run the program again: ")
    if again.upper() != 'Y':
        print("Thank You! Visit Again.")
        print()
        break