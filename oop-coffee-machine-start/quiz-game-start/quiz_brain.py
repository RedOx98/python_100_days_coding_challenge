class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        try:
            current_question = self.question_list[self.question_number]
        except IndexError:
            print("No more questions.")
            return

        display_num = self.question_number + 1
        user_answer = input(f"{display_num}: {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        print(self.check_answer(user_answer, correct_answer))
        self.question_number += 1

    def still_has_quiz_left(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        current_question  = self.question_list[self.question_number]
        current_answer = current_question.answer
        # print(f"real answer: "+current_answer + " vs user answer: " + " vs " + correct_answer)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return "You got it right, ", f"Your current score is {self.score}/{self.question_number}"
        else:
            return f"You got it wrong", f"Your current score is {self.score}/{self.question_number}"
        print(f"The correct answer was {correct_answer}")