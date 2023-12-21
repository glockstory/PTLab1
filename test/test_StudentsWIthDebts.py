import pytest
from StudentsWithDebts import StudentsWithDebts
from Types import DataType

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

    def test_count_students_with_debts(self, student_data: DataType, capsys) -> None:
        # Создаем экземпляр класса StudentsWithDebts с тестовыми данными
        students_with_debts_counter = StudentsWithDebts(student_data)
        
        # Вызываем метод count_students_with_debts, который выводит результат
        students_with_debts_counter.count_students_with_debts()

        # Захватываем выведенный текст с помощью capsys
        captured = capsys.readouterr()

        # Проверяем, содержится ли ожидаемая строка в захваченном выводе
        assert "Студентов, имеющих академические задолжности ровно по двум предметам" in captured.out
