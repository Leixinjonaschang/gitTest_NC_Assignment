
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

import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    test12 = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()