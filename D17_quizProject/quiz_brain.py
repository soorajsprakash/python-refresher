class QuizBrain:
    def __init__(self, qList):
        self.qNum = 0
        self.qList = qList
        self.score = 0

    def nextQuestion(self):
        currentQues = self.qList[self.qNum]
        self.qNum += 1
        uAnswer = input(f"Q.{self.qNum}: {currentQues.text}. (True/False)?: ").lower()
        currentAns = currentQues.answer
        self.checkAnswer(uAnswer, currentAns)

    def stillHasQuestions(self):
        return self.qNum < len(self.qList)

    def checkAnswer(self, userAnswer, currentAnswer):
        if userAnswer == currentAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {currentAnswer}")
        print(f"Your current score is {self.score}/{self.qNum}")
        print("\n")
