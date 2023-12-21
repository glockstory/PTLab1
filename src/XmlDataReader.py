import xml.etree.ElementTree as ET
from DataReader import DataReader
from Types import DataType

class XMLDataReader(DataReader):
    
    def read(self, file_path: str) -> DataType:        
        tree = ET.parse(file_path)
        root = tree.getroot()

        student_data: DataType = {}

        for student_element in root:
            student_name = student_element.tag
            subjects = []
            for subject_element in student_element:
                subject_name = subject_element.tag
                subject_score = float(subject_element.text)
                subjects.append((subject_name, subject_score))
            student_data[student_name] = subjects
        return student_data
    
    