class University:
    departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]

    def __init__(self, accept_num):
        self.accept_num = accept_num
        self.applicants = []
        self.departments_students = {}

    def get_applicants_list(self):
        with open("applicants.txt", "r") as applicants_file:
            applicants = applicants_file.readlines()
        self.applicants = [apt.strip("\n").split() for apt in applicants]
        self.applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

    def accept_students(self, rank):
        for x in self.applicants:
            if not self.departments_students.get(x[rank + 3]) or len(self.departments_students[x[rank + 3]]) < self.accept_num:
                self.departments_students.setdefault(x[rank + 3], []).append(x)
                self.applicants.remove(x)

    def display_admission(self):
        for dpt in self.departments:
            self.departments_students[dpt].sort(key=lambda x: (-float(x[2]), x[0], x[1]))
            print(dpt)
            for student in self.departments_students[dpt]:
                print(f"{student[0]} {student[1]} {student[2]}")


university = University(int(input()))
university.get_applicants_list()
for rk in range(3):
    university.accept_students(rk)
university.display_admission()
