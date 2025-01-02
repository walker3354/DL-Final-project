import os

path = "..\\homeworks\\"
file_types = ["c"]


class HomeworkReader:
    def __init__(self):
        self.student_id_list = list()
        self.error_list = list()
        self.student_file_dict = dict()

        self.load_homeworks_title()
        self.load_students_code()

    def load_homeworks_title(self):
        if os.path.isdir(path):
            self.student_id_list = os.listdir(path)
        self.check_file_correctness()

    def check_file_correctness(self):
        for file in self.student_id_list:
            filename_extention = file.split(".")[1]
            if filename_extention != "c":
                self.student_id_list.remove(file)
                self.error_list.append(file)

    def load_students_code(self):
        for file_title in self.student_id_list:
            with open(path + "113368024.c", "r", encoding="utf-8") as file:
                self.student_file_dict[file_title.split(".")[0]] = file.read()

    def get_student_file_dict(self):
        return self.student_file_dict


if __name__ == "__main__":
    homework = HomeworkReader()
    print(homework.get_student_file_dict())
