import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QMessageBox
from PyQt5.QtCore import Qt

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class HomeworkList:
    def __init__(self):
        self.hw_list = []

    def add_homework(self, homework):
        self.hw_list.append(homework)

    def all_completed(self):
        completed = True
        for homework in self.hw_list:
            if not homework.completed:
                completed = False
                print(homework.name)
        if completed:
            print("All finished")

class HomeworkDialog(QWidget):
    def __init__(self, hw_list):
        super().__init__()
        self.setWindowTitle("Homework List")
        self.resize(400, 300)

        self.hw_list = hw_list

        self.layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        for homework in self.hw_list.hw_list:
            self.list_widget.addItem(homework.name)

        self.export_button = QPushButton("Export Data")
        self.export_button.clicked.connect(self.export_data)
        self.layout.addWidget(self.export_button)

        self.setLayout(self.layout)

    def export_data(self):
        data = {"homeworks": []}
        for homework in self.hw_list.hw_list:
            data["homeworks"].append({"name": homework.name, "priority": homework.priority, "completed": homework.completed})

        with open("new_data.json", "w") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(self, "Export Successful", "Data exported to new_data.json")

if __name__ == '__main__':
    hw_list = HomeworkList()
    hw_list.add_homework(Homework("Lap trinh App Producer", 3))
    hw_list.add_homework(Homework("Lam van", 2, True))
    hw_list.add_homework(Homework("Lap trinh GameMaker", 3))

    app = QApplication(sys.argv)
    dialog = HomeworkDialog(hw_list)
    dialog.show()
    sys.exit(app.exec_())