from .student import Student
from .file_io import FileIO

class Repository:
    
    FILE_PATH = "student.txt"
    
    @classmethod
    def load_all(cls) -> list:
        data = FileIO.read_file(cls.FILE_PATH)
        return [
            Student(name, int(kor), int(math))
            for line in data.strip().split("\n")
            for name, kor, math in [line.split(",")]
        ]
    
    @classmethod
    def save_all(cls, students: list):
        data ="\n".join([
            student.to_string()
            for student in students
        ])
        FileIO.write_file(cls.FILE_PATH, data)