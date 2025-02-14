from logo import quiz_logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print(quiz_logo)
print("\n")

question_bank = []
for question in question_data:
    question_text = question["text"]    # variable to keep "text" from quesiton_data dictionary
    question_answer = question["answer"]     # variable to keep "answer" from quesiton_data dictionary
    new_question = Question(q_text=question_text, q_answer=question_answer)      # object to pass text & answer from question_data
    question_bank.append(new_question)       # questions loop through

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")