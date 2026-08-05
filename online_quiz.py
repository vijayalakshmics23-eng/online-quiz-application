questions = [
    "What is the capital of India?",
    "Which language is commonly used for AI?",
    "What is 10 + 5?",
    "Which keyword is used to define a function in Python?",
    "What is the extension of a Python file?"
]
options = [
    ["A. Chennai", "B. Delhi", "C. Mumbai", "D. Kolkata"],
    ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    ["A. 10", "B. 15", "C. 20", "D. 25"],
    ["A. function", "B. define", "C. def", "D. fun"],
    ["A. .java", "B. .html", "C. .py", "D. .cpp"]
]
answers = ["B", "A", "B", "C", "C"]
def display_question(question, option_list):
    print("\n" + question)
    for option in option_list:
        print(option)
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False
def run_quiz():
    score = 0
    print("===== ONLINE QUIZ APPLICATION =====")

    for i in range(len(questions)):
        display_question(questions[i], options[i])

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if check_answer(user_answer, answers[i]):
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer:", answers[i])
    print("\n===== QUIZ RESULT =====")
    print("Your Score:", score, "/", len(questions))
    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")
    if percentage >= 50:
        print("Result: Passed")
    else:
        print("Result: Failed")
run_quiz()