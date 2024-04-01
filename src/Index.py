from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from widgets.App import Ui_MainWindow as App
from widgets.Task import Ui_Form as TaskWidget
from widgets.Form import Ui_Form as Form
from widgets.Gpt import Ui_Dialog as Ai
from PySide6.QtWidgets import *
from PySide6.QtCore import QRect,Signal, QSize, QTimer
from dao.Repository.TaskRepo import TaskRepository as Task
from openaiApi.main import AiGenerator
task = Task()
class App(QMainWindow, App):
    """App Class Inherited

    Args:
        QMainWindow (QMainWindow, App): Main Class to show the Main Window.
        App (QMainWindow): Main Class of Task Flow App.
    """
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTask)
        self.pushButton_2.clicked.connect(self.editTask)
        self.pushButton_3.clicked.connect(self.deleteTask)
        self.pushButton_4.clicked.connect(self.GptCreator)
        self.fill()
    def addTask(self):
        """addTask

        Class to add a new Task
        """
        self.form = Form('s',None)
        self.form.task_added.connect(self.actualizar_tareas)
        self.form.show()
    def editTask(self):
        """editTask

        Method to Update a Task.
        """
        selected = self.getDeleteTask()
        if len(selected) == 0 or len(selected)>1:
            self.label_6.setText('Seleciona una tarea Obligatoriamente')
        else:
            self.label_6.setText('')
            self.task_names.clear()
            self.label_6.setText('')
            self.form = Form('u',selected[0])
            self.form.task_edited.connect(self.actualizar_tareas)
            self.form.show()
    def deleteTask(self):
        """deleteTask()

        Method to remove a Task.
        """
        selecteds = self.getDeleteTask()
        if len(selecteds) == 0:
            self.label_6.setText('Seleciona una Tarea')
        else:
            self.label_6.setText('')
            for i in selecteds:
                    task.eliminar_tarea(i.label.text().replace('  ',''))
                    self.verticalLayout.removeWidget(i)
                    i.deleteLater()
                    w = self.verticalLayoutWidget.size().width()
                    h = self.verticalLayoutWidget.size().height()-30
                    self.verticalLayoutWidget.setGeometry(QRect(10, 120, w, h))
            self.actualizar_tareas
    def actualizar_tareas(self):
        """actualizar_tareas()

        Method to delete all Tasks and fill in again.
        """
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        self.verticalLayoutWidget.setGeometry(QRect(10, 120, 711, 0))
        self.fill()
    def fill(self):
        """fill()
        
        Method to fill all Tasks from DataBase.
        """
        tareas = task.obtener_tareas()
        if tareas is not None:
            for i in tareas:
                horas = str(i[3]).split(':')
                hora = horas[0]+':'+horas[1]
                widget = Taskwidget(i[0],i[1],i[2],hora)
                self.verticalLayout.addWidget(widget)
                w = self.verticalLayoutWidget.size().width()
                h = self.verticalLayoutWidget.size().height()+30
                self.verticalLayoutWidget.setGeometry(QRect(10, 120, w, h))
    def getDeleteTask(self):
        """getDeleteTask
        
        Returns:
            list: Returns a list with all selecteds Tasks.
        """
        selecteds = list()
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if isinstance(widget.radioButton, QRadioButton) and widget.radioButton.isChecked():
                selecteds.append(widget)
        return selecteds
    def GptCreator(self):
        self.gpt = Gpt()
        self.gpt.buttonBox.accepted.connect(self.generateTask)
        self.gpt.show()
    def generateTask(self):
        """generateTask
        
        Method to generate a Task making a Get Request from GPT API.
        """
        if self.gpt.textEdit.toPlainText():
            self.gpt.label_gpt.setText('>GPT: Generando...')
            self.gpt.label_gpt.setStyleSheet('color: cyan;')
            result = AiGenerator(self.gpt.textEdit.toPlainText())
            tarea = result.split('_')
            hora = tarea[3]+':00'
            ins = task.añadir_tarea(tarea[0],tarea[1],tarea[2],hora.replace('.',''))
            if ins == 1:
                self.gpt.close()
                self.actualizar_tareas()
            else:
                self.gpt.label_gpt.setText('>GPT:...')
                self.gpt.label_gpt.setStyleSheet('color: red;')
                self.gpt.textEdit.setText('Fecha y Hora ocupadas')
class Taskwidget(QWidget, TaskWidget):
    """Task Class Inherited

    Args:
        QWidget (QWidget): Object from PySide6.QWidgets
        TaskWidget (QWidget): Task class from widgets.Task to show each Task in Main Window
    """
    def __init__(self, Nombre, Descripcion, Fecha, hora):
        super(Taskwidget, self).__init__()
        self.setupUi(self)
        if Nombre is not None and Descripcion is not None and Fecha is not None and hora is not None:
            self.label.setText('  '+str(Nombre))
            self.label_2.setText('  '+str(Descripcion))
            self.label_3.setText('  '+str(Fecha))
            self.label_4.setText('  '+str(hora))
class Form(QWidget, Form):
    """Form Class Inherited

    Args:
        QWidget (Qidget): Object QWidget from PySide6.QWidgets
        Form (QForm): Form class from widgets.Form to Create and Update Tasks.
    """
    task_added = Signal()
    task_edited = Signal()
    def __init__(self,op,selected):
        super(Form, self).__init__()
        self.setupUi(self)
        if op == 's':
            self.pushButton.clicked.connect(self.submit)
        elif op == 'u':
            if selected is None:
                self.pushButton.clicked.connect(self.submit)
            else:
                self.lineEdit.setText(selected.label.text().replace('  ',''))
                self.lineEdit_4.setText(selected.label_2.text().replace('  ',''))
                self.lineEdit_2.setText(selected.label_3.text().replace('  ',''))
                self.lineEdit_3.setText(selected.label_4.text().replace('  ',''))
                self.pushButton.setText('Guardar')
                self.lineEdit.setReadOnly(True)
                self.pushButton.clicked.connect(self.Actualizar)                
    def submit(self):
        """submit
        
        Main and default Method to Insert a new Task on Database.
        """
        if self.lineEdit.text() != '' and self.lineEdit_4 != '':
            self.label_6.setText('')
            name = self.lineEdit.text()
            desc = self.lineEdit_4.text()
            fecha = self.lineEdit_2.text()
            horas = self.lineEdit_3.text()+':00'
            insert = task.añadir_tarea(name,desc,fecha,horas)
            if insert == 1:
                self.task_added.emit()
                self.close()
            else:
                self.label_6.setText('Fecha y Hora ocupadas')
                self.label_6.setStyleSheet('color: red')
        else:
            self.label_6.setText('  Rellena los campos')
            self.label_6.setStyleSheet('color: red')
    def Actualizar(self):
        """Actualizar
        
        Main Method to Update a Task from Database.
        """
        name = self.lineEdit.text()
        desc = self.lineEdit_4.text()
        fecha = self.lineEdit_2.text()
        horas = self.lineEdit_3.text()
        edited = task.editar_tarea(name,desc,fecha,horas)
        if edited == 1:
            self.task_edited.emit()
            self.close()
        else:
            self.label_6.setText('Fecha y Hora ocupadas')
            self.label_6.setStyleSheet('color: red')

class Gpt(QDialog, Ai):
    """Gpt Class

    Args:
        QDialog (QDialog): Object from PySide6.QWisgets
        Ai (QDialog): Dialog to show a Window with Gpt inplementation
    """
    def __init__(self):
        super(Gpt, self).__init__()
        self.setupUi(self)
        self.buttonBox.rejected.connect(self.close)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.txt)
        self.Saludo = 'Hola! En que puedo ayudarte?'
        self.text = self.label_gpt.text()
        self.timer.start(40)
        self.index = 0
    def txt(self):
        """txt
        
        Method to make a short Writing Animation.
        """
        if len(self.text) < len('>GPT: Hola! En que puedo ayudarte?'):
            self.text += self.Saludo[self.index]
            self.index+=1
            self.label_gpt.setText(self.text)
        else:
            self.textEdit.setFocus()
            self.textEdit.setPlaceholderText('Escribe algo...')
            self.timer.stop()
app = QApplication()
window = App()
window.show()
app.exec()