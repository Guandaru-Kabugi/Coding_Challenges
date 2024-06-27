from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer) #created objects of all questions
    question_bank.append(new_question) #added the objects into a list

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): #do not forget the brackets for methods
    quiz.next_question()
# quiz.final_score()
print("You have completed the challenge!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
    