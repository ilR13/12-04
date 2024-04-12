from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout,QGroupBox
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo card')
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3




def ask(q: Question):
    text.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)





text = QLabel('деревня')
btn_answer1 = QRadioButton('wilena')
btn_answer2 = QRadioButton('woisko')
btn_answer3 = QRadioButton('woinstva')
btn_answer4 = QRadioButton('wioska')
group = QGroupBox('Варианты ответа')
otv = QPushButton('Ответить')
newgroup = QGroupBox('Результат теста')
newgroup.hide()
tekst = QLabel('прав ты или нет?')
tkt = QLabel('ответ будет тут!')






l1 = QVBoxLayout()
l2 = QHBoxLayout()
l3 = QVBoxLayout()
l4 = QVBoxLayout()
l5 = QVBoxLayout()
l6 = QHBoxLayout()
l7 = QHBoxLayout()




l1.addWidget(text, alignment=Qt.AlignCenter)
l1.addWidget(group)
l1.addWidget(newgroup)
l1.addWidget(otv, alignment=Qt.AlignCenter, )

l1.stretch(3)

l3.addWidget(btn_answer1, alignment=Qt.AlignCenter)
l3.addWidget(btn_answer2, alignment=Qt.AlignCenter)
l4.addWidget(btn_answer3, alignment=Qt.AlignCenter)
l4.addWidget(btn_answer4,alignment=Qt.AlignCenter)
l2.addLayout(l3)
l2.addLayout(l4)

l6.addWidget(tekst, alignment=Qt.AlignLeft)
l7.addWidget(tkt, alignment=Qt.AlignCenter)
l5.addLayout(l6)
l5.addLayout(l7)

def show_question():
    newgroup.hide()
    group.show()
    otv.setText('Ответить')
def show_resut():
    group.hide()
    newgroup.show()
    otv.setText('Следующий вопрос')
def start_test():
    if otv.text() == 'Ответить':
        show_resut()
        check_answer()
    elif otv.text() == 'Следующий вопрос':
        next_question()
        print(0)
        show_question()


answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
shuffle(answers)

question_list = []

q1 = Question('Какой периметр у квадрата со стороной 4' , '16', '3', '12', '1')
q2 = Question('Столица России', 'Москва', 'Казань', 'Нижний - Новгород', 'Обнинск')
q3 = Question('Кто нашел песочек', 'Беляш', 'Даня', 'Ваня', 'Незнаю')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
main_win.score = 0
main_win.total = 0

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        show_correct('Прав')

    elif answers[1] or answers[2] or answers[3]:

        main_win.total += 1

        show_correct('Неправ')











def next_question():
    main_win.chet = randint(0,len(question_list)-1)
    q = question_list[main_win.chet]
    ask(q)




next_question()


def show_correct(res):
    tekst.setText(res)
    tkt.setText(answers[0].text())



group.setLayout(l2)
newgroup.setLayout(l5)
otv.clicked.connect(start_test)




print('Правильные ответы:', main_win.score)
print('Неправильные ответы', main_win.total)




main_win.setLayout(l1)
main_win.show()
app.exec_()
