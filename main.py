import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

random_questions = random.sample(question_data, 10)

question_bank = []

for question in random_questions:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")