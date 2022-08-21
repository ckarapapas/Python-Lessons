import data, quiz_brain
from question_model import Question

question_bank = []

for i in range(0, len(data.question_data)):
    #print(i)
    new_q = Question(data.question_data[i]["text"], data.question_data[i]["answer"])
    question_bank.append(new_q)
quizb = quiz_brain.QuizBrain(question_bank)

while quizb.still_has_questions():
    quizb.next_question()

print("You completed the quiz!")
print(f"Final score is: {quizb.score/len(question_bank)}")