#Question
class Question:
 def__init__(self,text,choices,answer)
 self.text=text
 self.choices=Choices
 self.answer=answer
 
 def checkAnswer(self,answer):
  return self.answer== answer
 q1=Question('en iyi programlama dili hangisidir?',['C#','python','javascript','java'],'python')
 q2=Question('en popiler programlama dili hangisidir?',['C#','python','javascript','java'],'pyton')
 q3=Question('en çok kazandıran programlama dili hangisidir?',['C#','python','javascript','java'],'python')
Question=[q1,q2,q3]
print(q1.checkAnswer('python'))

 #Quiz
class Quiz:
 def__init__(self,questions):
 self.questions=questions
 self.score=0
 self.questionIndex=0
 q1=Question('en iyi programlama dili hangisidir?',['C#','python','javascript','java'],'python')
 q2=Question('en popiler programlama dili hangisidir?',['C#','python','javascript','java'],'pyton')
 q3=Question('en çok kazandıran programlama dili hangisidir?',['C#','python','javascript','java'],'python')
Question=[q1,q2,q3]

quiz=Quiz(questions)
question=quiz.questions[quiz.questionIndex]
print(question.text)
