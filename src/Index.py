from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from widgets.App import Ui_MainWindow as App
from widgets.Task import Ui_Form as TaskWidget
from widgets.Form import Ui_Form as Form
from dialog.submit import Ui_Dialog as Dialog
from PySide6.QtWidgets import *
from PySide6.QtCore import QRect,Signal, QSize
from dao.database import Task
task = Task('localhost','root','123456')
class App(QMainWindow, App):
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTask)
        self.pushButton_2.clicked.connect(self.editTask)
        self.pushButton_3.clicked.connect(self.deleteTask)
        self.task_names = set()
        self.selected = False
        self.fill()

    def addTask(self):
        self.form = Form()
        self.form.task_added.connect(self.fill)
        self.form.show()
    def editTask(self):
        if self.selected == False:
            self.label_6.setText("Una Tarea selecionada Obligatoriamente")
        else:
            self.label_6.setText('')
    def deleteTask(self):
        selecteds = self.getDeleteTask()
        if len(selecteds) == 0:
            self.label_6.setText('Seleciona una Tarea')
        else:
            self.label_6.setText('')
            for i in selecteds:
                    task.eliminar_tarea(i.label.text().replace('  ',''))
                    self.verticalLayout.removeWidget(i)
                    i.deleteLater()
            self.actualizar_tareas
            w = self.verticalLayoutWidget.size().width()
            h = self.verticalLayoutWidget.size().height()-24
            self.verticalLayoutWidget.setGeometry(QRect(10, 120, w, h))
    def actualizar_tareas(self):
        for i in reversed(range(self.verticalLayout.count())): 
            self.verticalLayout.itemAt(i).widget().setParent(None)
        self.fill()
    def fill(self):
        tareas = task.obtener_tareas()
        if tareas is not None:
            for i in tareas:
                if i[0] not in self.task_names:  
                    widget = Taskwidget(i[0],i[1],i[2],i[3],self.revisar_radiobuttons)
                    self.verticalLayout.addWidget(widget)
                    self.task_names.add(i[0])
                    w = self.verticalLayoutWidget.size().width()
                    h = self.verticalLayoutWidget.size().height()+24
                    self.verticalLayoutWidget.setGeometry(QRect(10, 120, w, h))
    def revisar_radiobuttons(self):
        seleccionados = 0
        selecteds = list()
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if isinstance(widget.radioButton, QRadioButton) and widget.radioButton.isChecked():
                seleccionados += 1
                selecteds.append(widget)
            if seleccionados > 1:
                self.selected = False
                return selecteds
        self.selected = True
        return selecteds
    def getDeleteTask(self):
        selecteds = list()
        for i in range(self.verticalLayout.count()):
            widget = self.verticalLayout.itemAt(i).widget()
            if isinstance(widget.radioButton, QRadioButton) and widget.radioButton.isChecked():
                selecteds.append(widget)
        return selecteds
class Taskwidget(QWidget, TaskWidget):
    def __init__(self, Nombre, Descripcion, Fecha, hora,revisar):
        super(Taskwidget, self).__init__()
        self.setupUi(self)
        if Nombre is not None and Descripcion is not None and Fecha is not None and hora is not None:
            self.label.setText('  '+str(Nombre))
            self.label_2.setText('  '+str(Descripcion))
            self.label_3.setText('  '+str(Fecha))
            self.label_4.setText('  '+str(hora))
        self.radioButton.clicked.connect(revisar)
class Form(QWidget, Form):
    task_added = Signal()
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.submit)
    def submit(self):
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '0000-00-00' and self.lineEdit_3 != '00:00' and self.lineEdit_4 != '':
            name = self.lineEdit.text()
            desc = self.lineEdit_4.text()
            fecha = self.lineEdit_2.text()
            horas = self.lineEdit_3.text()+':00'
            insert = task.añadir_tarea(name,desc,fecha,horas)
            if insert == 1:
                self.task_added.emit()
                self.close()
        else:
            self.dialog = Dialog()
            self.dialog.show()
class Dialog(QDialog, Dialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
app = QApplication()
window = App()
window.show()
app.exec()