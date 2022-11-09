# Created by Axel Jon Bico
# Start
print("Hello Student. Welcome to the Quiz\n")
name = input("Please Enter your Name     : ")
student_id = input("Please Enter your ID no.   : ")
print("\nThank You! You Have successfully Registered.")
print("\nName   : " + name + "\nID no. : " + student_id)
# Loop For the Question 
def new_quiz():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("\n------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Please Enter your Answer(A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
# -------------------------
# Loop for the result in every questions
def check_answer(answer, guess):

    if answer == guess:
        print("You got the Correct Answer!")
        return 1
    else:
        print("Your Answer is Wrong!")
        return 0

# -------------------------
# Loop for the result
def display_score(correct_guesses, guesses):
    print("\n------------------------------------")
    print("RESULTS")
    print("--------------------------------------\n")

    print("Correct Answers : ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your Answers :    ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
# Loop for the user if He/she want to take the quiz
def take_again():

    response = input("\nDo you want to Take the Quiz again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------
# Set of Questions and Choices
questions = {
 "HTML means…: ": "A",
 "Fullstack Web Development is…: ": "D",
 "What is a Flowchart?: ": "A",
 "Who is the CEO of the Microsoft?: ": "B",
 "Is the Earth round?: ": "A"
}

options = [["A. HyperText Markup Language", "B. HyperLoop Markup Language", "C. Hypertext Preprocessor", "D. None of above"],
          ["A. Web Design", "B. Back-end Development only", "C. Front-end Development only", "D. Front-end and Back-end Development"],
          ["A. Combination of lines and Shapes of a program", "B. Represents Shapes", "C. Graphical representation of an Algorithm", "D. None of the Above"],
          ["A. Barack Obama", "B. Bill Gates", "C. Elon Musk", "D. LeBron James"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
new_quiz()

while take_again():
    new_quiz()

print("Thank You for taking the Quiz!")

# End
# -------------------------