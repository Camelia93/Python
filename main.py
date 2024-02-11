from question_model import Question
from data import question_data


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

class NextQuestion:
    def __init__(self, q_number, q_lista):
        self.number = q_number
        self.lista = q_lista
    number = 0
    check_answer = ["True" or "False"]
    final_score = 0
    for q_number in range(0, 11):
        number += 1
        print(" ".join(question_bank[number].text))
        user_answer = input("Write your answer True or False:\n").lower()
        if user_answer == question["answer"].lower():
            final_score += 1
            print(f"This is correct! Your score is {final_score}")
        else:
            print("This is not correct!")

    print(question_bank[number].text)
    print(f"Your final score is {final_score}")