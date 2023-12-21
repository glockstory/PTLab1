import pytest
from XmlDataReader import XMLDataReader
from Types import DataType

class TestXMLDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml_content = """
        <root>
            <Ivanov_Ivan_Ivanovich>
                <math>90</math>
                <literature>80</literature>
            </Ivanov_Ivan_Ivanovich>
            <Petrov_Petr_Petrovich>
                <math>75</math>
                <literature>95</literature>
            </Petrov_Petr_Petrovich>
        </root>
        """
        data = {
            "Ivanov_Ivan_Ivanovich": [("math", 90), ("literature", 80)],
            "Petrov_Petr_Petrovich": [("math", 75), ("literature", 95)],
        }
        return xml_content, data

    @pytest.fixture()
    def file_path_and_data(self,
                           file_and_data_content: tuple[str, DataType],
                           tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, file_path_and_data: tuple[str, DataType]) -> None:
        xml_reader = XMLDataReader()
        file_content = xml_reader.read(file_path_and_data[0])
        assert file_content == file_path_and_data[1]

# If using this script as a standalone, you can run the tests with:
# pytest -v your_test_file.py
