from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
     
class MainWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # старт:
       self.show()


   def initUI(self):
       ''' создаёт графические элементы '''
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
  
   def next_click(self):
       self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


app = QApplication([])
mw = MainWin()
app.exec_()

from instr import *
from final_win import *


class TestWin(QWidget):
   def __init__(self):
       ''' окно, в котором проводится опрос '''
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()
      
       # старт:
       self.show()
  
   def next_click(self):
       self.tw = TestWin()
       self.hide()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


   def initUI(self):
       ''' создаёт графические элементы '''
       #self.questionnary = AllQuestions()
       self.btn_next = QPushButton(txt_sendresults, self)
       self.btn_test1 = QPushButton(txt_starttest1, self)
       self.btn_test2 = QPushButton(txt_starttest2, self)
       self.btn_test3 = QPushButton(txt_starttest3, self)




       self.text_name = QLabel(txt_name)
       self.text_age = QLabel(txt_age)
       self.text_test1 = QLabel(txt_test1)
       self.text_test2 = QLabel(txt_test2)
       self.text_test3 = QLabel(txt_test3)
       self.text_timer = QLabel(txt_timer)


       self.line_name = QLineEdit(txt_hintname)


       self.line_age = QLineEdit(txt_hintage)


       self.line_test1 = QLineEdit(txt_hinttest1)


       self.line_test2 = QLineEdit(txt_hinttest2)


       self.line_test3 = QLineEdit(txt_hinttest3)


       self.l_line = QVBoxLayout()
       self.r_line = QVBoxLayout()
       self.h_line = QHBoxLayout()
       self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
       self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
       self.h_line.addLayout(self.l_line) 
       self.h_line.addLayout(self.r_line)       
       self.setLayout(self.h_line)
  
   def next_click(self):
       self.hide()
       self.fw = FinalWin()


   def connects(self):
       self.btn_next.clicked.connect(self.next_click)


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

class FinalWin(QWidget):
   def __init__(self):
       ''' окно, в котором проводится опрос '''
       super().__init__()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()
      
       # старт:
       self.show()


   def initUI(self):
       ''' создаёт графические элементы '''
       self.workh_text = QLabel(txt_workheart)
       self.index_text = QLabel(txt_index)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout_line)


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_finalwin)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


win_x, win_y = 200, 100
win_width, win_height = 1000, 600


txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )
txt_title = 'Здоровье'
txt_name = 'Введите Ф.И.О.:'
txt_hintname = "Ф.И.О."
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.'
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.'
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
txt_timer = ''


txt_age = 'Полных лет:'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье: '
txt_workheart = 'Работоспособность сердца: '
