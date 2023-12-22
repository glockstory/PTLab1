class StudentsWithDebts:

    def __init__(self, student_data):
        self.student_data = student_data

    def count_students_with_debts(self):
        students_with_debts = 0

        for student_name, subjects in self.student_data.items():
            # Count subjects with scores < 61
            subjects_below_threshold = sum(1 for _,
                                           score in subjects if score < 61)

            # Check if exactly two subjects have scores < 61
            if subjects_below_threshold == 2:
                students_with_debts += 1
        print(f'Студентов с двумя долгами: {students_with_debts}')
