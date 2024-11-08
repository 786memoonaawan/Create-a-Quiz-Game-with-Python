# Python Quiz Game

questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest eggs?:",
             "What is the most abundant gas in the Earth's atmosphere?:",
             "How many bones in the human body?:",
             "Which planet in the solar system is the hottest?:",
             "What is the chemical formula for Gold?:",
             "In what year was the first iPhone released?:",
             "What is sushi traditionally wrapped in?:",
             "Who is the CEO of Tesla?:",
             "What is the capital city of Canada?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Gd", "B. Go", "C. Ag", "D. Au"),
           ("A. 2005", "B. 2007", "C. 2008", "D. 2010"),
           ("A. Rice Paper", "B. Seaweed", "C. Bamboo", "D. Lettuce"),
           ("A. Jeff Bezos", "B. Mark Zuckerberg", "C. Tim Cook", "D. Elon Musk"),
           ("A. Vancouver", "B. Toronto", "C. Quebec City", "D. Ottawa"))

answers = ("C", "D", "A", "A", "B", "D", "B", "B", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

Score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

    