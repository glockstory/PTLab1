import argparse
import sys
import os

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XMLDataReader
from StudentsWithDebts import StudentsWithDebts
from DataReader import DataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def get_current_reader(path: str) -> DataReader:
    root, file_extension = os.path.splitext(path)
    match file_extension:
        case ".txt":
            return TextDataReader()
        case ".xml":
            return XMLDataReader()
        case _:
            raise ValueError("Неподдерживаемый формат")


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_current_reader(path)
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    students_debts = StudentsWithDebts(students)
    students_debts.count_students_with_debts()


if __name__ == "__main__":
    main()
