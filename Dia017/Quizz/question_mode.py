import data
class Question():
    def __init__(self, numero):
        self.text = data.question_data[numero]["text"]
        self.answer = data.question_data[numero]["answer"]


questao_0 = Question(0)

print(questao_0.text)
print(questao_0.answer)