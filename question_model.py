#from question_model import qustion_data

class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer
new_question = Question("2+3=5?","True")

