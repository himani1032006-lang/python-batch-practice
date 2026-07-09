from abc import ABC, abstractmethod



class ReportFile(ABC):
    @abstractmethod
    def save(student_name,marks):
        pass 
    @abstractmethod
    def read(ABC):
        pass
class TextReport(ReportFile):
    def save():
    def read():
class CSVReport(ReportFile):
    def save(): 
    def read():


