import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XMLDataReader
from StudentsWithDebts import StudentsWithDebts
def get_path_from_arguments(args) -> str:
  parser = argparse.ArgumentParser(description="Path to datafile")
  parser.add_argument("-p", dest="path", type=str, required=True,
                      help="Path to datafile")
  args = parser.parse_args(args)
  return args.path

def main():
  path = get_path_from_arguments(sys.argv[1:])  
  reader = XMLDataReader()
  students = reader.read(path)
  print("Students: ", students)
  rating = CalcRating(students).calc()
  print("Rating: ", rating)
  students_debts = StudentsWithDebts(students)
  students_debts.count_students_with_debts()
  
if __name__ == "__main__":
 main()
