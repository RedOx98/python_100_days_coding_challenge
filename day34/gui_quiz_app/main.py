from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz = QuizBrain(question_data)
quiz_ui = QuizInterface(quiz)