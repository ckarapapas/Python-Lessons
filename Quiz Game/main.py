import data
from question_model import Question

question_bank = []

for i in range(0,len(data.question_data)):
    new_q = Question(data.question_data[i]["text"], data.question_data[i]["answer"])
    question_bank.append(new_q)
print(question_bank)

