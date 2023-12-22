import pytest
from src.StudentsWithDebts import StudentsWithDebts
from src.Types import DataType


class TestStudentsWithDebts:
    @pytest.fixture
    def student_data(self) -> tuple[DataType]:
        # Тестовые данные для студентов
        data: DataType = {
            "Student1": [("Математика", 55), ("История", 70)],
            "Student2": [("Математика", 40), ("Английский", 90)],
            "Student3": [("Химия", 75), ("Физика", 80)],
            "Student4": [("Биология", 30), ("География", 50)],
        }
        return data

    def test_count_students_with_debts(self,
                                       student_data: DataType, capsys) -> None:
        # Создаем экземпляр класса StudentsWithDebts с тестовыми данными
        students_with_debts_counter = StudentsWithDebts(student_data)

        # Вызываем метод count_students_with_debts, который выводит результат
        students_with_debts_counter.count_students_with_debts()

        # Захватываем выведенный текст с помощью capsys
        captured = capsys.readouterr()

        assert (
            "Студентов с двумя долгами: 1"
            in captured.out
        )
