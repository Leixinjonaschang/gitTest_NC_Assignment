
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget

# def main():
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250,200)
#     w.move(300,300)
#
#     w.setWindowTitle('simple')
#
#     w.show()
#
#     sys.exit(app.exec()) # 推出

# -----
# import sys
# from PyQt6.QtWidgets import (QWidget,QToolTip,QPushButton,QApplication)
#
# from PyQt6.QtGui import QFont
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         QToolTip.setFont(QFont('SansSerif',10)) # 设置字体
#
#         self.setToolTip('This is a <b>QWidget</b> widget') #使用setToolTip() 设置富文本内容（即鼠标悬停时出现的内容）
#
#         btn = QPushButton('Button', self) # 添加按钮
#         btn.setToolTip('This is a <b>QPushButton</b> widget') # 富文本
#         btn.resize(btn.sizeHint()) # 系统建议尺寸
#         btn.move(50,10) # 移动按钮位置
#
#         # 添加推出按钮
#
#         qbtn = QPushButton('Quit',self)
#         qbtn.clicked.connect(QApplication.instance().quit)
#         qbtn.resize((qbtn.sizeHint()))
#         qbtn.move(200,200)
#
#
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('Tooltips')
#         self.show()
#
#
# def main():
#
#     app = QApplication(sys.argv)
#     ex = Example()
#
#     sys.exit(app.exec())
#
# if __name__ == '__main__': # 代码入口
#     main()

# -----
# 弹窗

# import sys
# from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication

# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('Message Box')
#         self.show()
#
#     def closeEvent(self, event):
#
#         reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.StandardButton.Yes |
#                                      QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
#
#         if reply == QMessageBox.StandardButton.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# def main():
#     app = QApplication(sys.argv)
#     test13 = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()

# ------
# 窗口初始居中
# import sys
# from PyQt6.QtWidgets import QWidget, QApplication
#
# class Example(QWidget): # 继承QWidget
#     def __init__(self): # 初始化父类属性
#         super().__init__() # super()将父类和子类关联起来，让子类Example调用父类QWidget的初始化函数，包含父类所有属性（父类也称超类 superclass）
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.resize(350,250)
#         self.center()
#
#         self.setWindowTitle('the centering of window')
#         self.show()
#
#     def center(self):
#
#         qr = self.frameGeometry()
#         cp = self.screen().availableGeometry().center()
#
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# def main():
#
#     app = QApplication(sys.argv)
#     ex8 = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()


# ----
# 状态栏
#
# import sys
# from PyQt6.QtWidgets import QMainWindow, QApplication
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self): # 这个方法在初始化方法中定为属性，可以把对窗口的初始化全部写在initUI()中
#
#         self.statusBar().showMessage('Ready2'+' '+'ready1')
#
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('Statusbar')
#         self.show()
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()


#-------
# 菜单栏

# import sys
# from PyQt6.QtWidgets import QMainWindow, QApplication
# from PyQt6.QtGui import QIcon, QAction
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#
#         exitAct = QAction(QIcon('exit.png'),'&Exit',self)
#         exitAct.setShortcut('Ctrl+Q')
#         exitAct.setStatusTip('Exit Application')
#         exitAct.triggered.connect(QApplication.instance().quit)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAct)
#
#
#
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('Menubar')
#         self.show()
#
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()

# file: simple_menu.py
#!/usr/bin/python

#--------
# 子菜单
# import sys
# from PyQt6.QtWidgets import QMainWindow,QMenu,QApplication
# from PyQt6.QtGui import QAction
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('File')
#
#         impMenu = QMenu('import',self)
#         impAct = QAction('import mail',self)
#         impMenu.addAction(impAct)
#
#         newAct = QAction('new',self)
#
#         fileMenu.addAction(newAct)
#         fileMenu.addMenu(impMenu)
#
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('Submenu')
#         self.show()
#
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()

#------
# 勾选菜单

# import sys
# from PyQt6.QtWidgets import QMainWindow, QApplication
# from PyQt6.QtGui import QAction
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.statusbar = self.statusBar()
#         self.statusbar.showMessage('Ready')
#
#         menubar = self.menuBar()
#         viewMenu = menubar.addMenu('View')
#         viewStatAct = QAction('View statusbar', self, checkable=True)
#
#         self.setGeometry(300,300,300)
#         self.setWindowTitle("勾选菜单")
#         self.show()


# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()


# file: check_menu.py
#!/usr/bin/python

