#This program shows the highest score of the quiz game

with open ("C:\\Users\\charc\\Desktop\\Python\\Project - Quiz\\score.txt") as f:

    read_score = f.read()

    print()
    print(f"The highest score is: {read_score}")
    print()