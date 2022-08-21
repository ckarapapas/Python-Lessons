import data, random

number_of_questions = len(data.question_data)


class Question:
    def __init__(self):
        rand = random.randint(0, number_of_questions)
        self.text = data.question_data[rand]["text"]
        self.answer = data.question_data[rand]["answer"]
