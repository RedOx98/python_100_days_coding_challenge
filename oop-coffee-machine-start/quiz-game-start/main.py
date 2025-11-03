from question_model import Quiz
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Quiz(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_left = True

# # while there are still questions in the list
# while quiz_left == True:
#     for i in range(0, len(question_bank)):
#         quiz.next_question()
#         print("_____")
#         if i == len(question_bank):
#             print("question ends")

while quiz.still_has_quiz_left():
    quiz.next_question()
    # print(quiz.score)



print("You've completed the quiz")
print(f"You got {quiz.score}/{quiz.question_number}")
