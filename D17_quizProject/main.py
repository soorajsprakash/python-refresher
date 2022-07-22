from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for each in question_data:
    questionTxt = each['question']
    questionAns = each['correct_answer']
    newSet = Question(questionTxt, questionAns)
    question_bank.append(newSet)

quiz = QuizBrain(question_bank)
quiz.nextQuestion()

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
