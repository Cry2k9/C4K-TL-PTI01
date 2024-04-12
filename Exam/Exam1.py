class Homework:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False

class Homeworklist:
    def __init__(self):
        self.homeworks = []
    
    def add_homework(self, homework):
        self.homeworks.append(homework)
    
    def all_finished(self):
        unfinished_homeworks = [homework.name for homework in self.homeworks if not homework.completed]
        
        if unfinished_homeworks:
            print("Các bài tập chưa hoàn thành:")
            for homework_name in unfinished_homeworks:
                print(homework_name)
        else:
            print("Tất cả các bài tập đã hoàn thành.")

homework1 = Homework("Lập trình AppProducer", "3")
homework2 = Homework("Làm Văn", "2")
homework3 = Homework("Lập trình GameMaker", "1")

homework_list = Homeworklist()
homework_list.add_homework(homework1)
homework_list.add_homework(homework2)
homework_list.add_homework(homework3)

homework2.completed = True

homework_list.all_finished()