from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


new_quiz = QuizBrain(question_bank)



while new_quiz.still_has_questions():
    new_quiz.next_question()




# final_game = ""
# while final_game != "fim":
#     final_game = new_quiz.next_question()

# questao = Question(question_data[a_questao]["text"],question_data[a_questao]["answer"])
# question_bank.append(questao)
# question_bank.append([Question(question_data[_]["text"],question_data[_]["answer"])])
