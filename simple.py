# file: line_edit.py
#!/usr/bin/python

# file: combobox.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows how to use
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys

from PyQt6.QtWidgets import (QWidget, QLabel,
        QComboBox, QApplication, QLineEdit, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # -------
        # 按钮（Button）区
        # -------
        self.btn_confirm = QPushButton("确定", self) # 创建"确定"按钮
        self.btn_confirm.move(50, 90) # 设置"确定"按钮位置
        self.btn_confirm.resize(60, 30) # 设置"确定"按钮的尺寸

        self.btn_reset = QPushButton("重设", self) # 创建重设按钮
        self.btn_reset.move(125, 90)
        self.btn_reset.resize(45,30)

        # self.btn_confirm.clicked.connect(self.function) # 绑定"传入参数"的操作 先留着坑位
        # self.btn_reset.clicked.connect(self.function) # 绑定"传入参数"的操作 先留着坑位

        # ------------
        # 输入框（QlineEdit）区
        # -----------
        self.le_R = QLineEdit(self) # 曲线段数N 半径输入框
        self.le_R.move(90, 10)
        self.le_R = QLineEdit(self) # 基圆R 半径输入框
        self.le_R.move(90, 40)
        self.le_H = QLineEdit(self) # 升程H 输入框
        self.le_H.move(90, 70)


        # ---------
        # 文字标签区
        # ---------
        self.lbl_le_N = QLabel(self) # 设置"基圆半径"文字标签
        self.lbl_le_N.setText("曲线段数 N")
        self.lbl_le_N.move(0,10)

        self.lbl_le_R = QLabel(self) # 设置"基圆半径"文字标签
        self.lbl_le_R.setText("基圆半径 R")
        self.lbl_le_R.move(0,40)

        self.lbl_le_H = QLabel(self)  #
        self.lbl_le_H.setText("升程 R")
        self.lbl_le_H.move(0, 70)


        # -------
        # 窗口参数区
        # --------
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("主界面")
        self.show()




    # git test 2push 333



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
