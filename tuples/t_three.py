quiz = {
    "What is the capital of India?": {
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    "Which language is used for web development?": {
        "options": ["A. Python", "B. HTML", "C. Java", "D. C"],
        "answer": "B"
    },
    "Which number is even?": {
        "options": ["A. 3", "B. 7", "C. 10", "D. 9"],
        "answer": "C"
    }
}
score = 0
for question, data in quiz.items():
    print("\n", question)
    for option in data["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D), S to skip, Q to quit: ").upper()

    if user_answer == "Q":
        print("You quit the quiz.")
        break
    elif user_answer == "S":
        print("Question skipped.")
        continue
    elif user_answer == data["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        score -= 1
print("\n")
print("Final Score:", score)