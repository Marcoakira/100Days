import data

class Question():
    def __init__(self, numero):
        self.text = data.question_data[numero]["text"]
        self.answer = data.question_data[numero]["answer"]

pontos = 0

questao_0 = Question(0)

def user_question(boleano):

    if boleano and questao_0.answer :
        pontos += 1

print(questao_0.text)

# print(questao_0.text)
# print(questao_0.answer)