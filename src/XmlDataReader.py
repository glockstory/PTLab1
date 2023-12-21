import xml.etree.ElementTree as ET
from DataReader import DataReader
from Types import DataType

class XMLDataReader(DataReader):
    def read(self, file_path: str) -> DataType:        
        #tree = ET.fromstring(file_path)
        #root = tree.getroot()
        with open(file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        
        tree = ET.fromstring(xml_content)
        students_with_debt = 0

        for student in tree.findall('student'):
            # Счетчик предметов с оценками меньше порога
            subjects_below_threshold = 0

            # Проходим по всем предметам у студента
            for subject_element in student.findall('subject'):
                subject_score = int(subject_element.text)
                
                # Проверяем, есть ли задолженность по предмету
                if subject_score < 2:
                    subjects_below_threshold += 1

            # Если задолженность есть ровно по двум предметам, увеличиваем счетчик студентов
            if subjects_below_threshold == 2:
                students_with_debt += 1

        print(f"Количество студентов с академическими задолженностями (меньше 61) по 2 предметам: {students_with_debt}")
