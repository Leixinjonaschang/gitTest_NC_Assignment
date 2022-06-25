# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


from PyQt6.QtCore import QDateTime,Qt

now = QDate.currentDate()

print(now.toString(Qt.DateFormat.ISODate))

print('local time: ',now.toString(Qt.DateFormat.ISODate))
print('Universal datetime: ',now.toUTC().toString(Qt.DateFormat.ISODate))

print(f'The offset from UTC is: {now.offsetFromUtc()} seconds')