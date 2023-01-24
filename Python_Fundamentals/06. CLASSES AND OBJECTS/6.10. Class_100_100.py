class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        av_grade = round(sum(self.grades) / len(self.students), 2)
        return av_grade

    def __str__(self):
        result = f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
        return result
