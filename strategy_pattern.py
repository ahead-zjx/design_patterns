from abc import abstractmethod, ABC

"""
策略模式：适用于同一件事用不同的方式去做的场景，将每一个策略包装成一个单独的类，这些类拥有相同的接口，可以进行统一调用
"""


# 为了让策略类有相同的接口，首先要定义一个基类，让所有的策略类都继承这个类，达到规范接口的目的
# 并且约束基类不能被实例化，因此需要引入ABC(abstract base class)，基类继承ABC，如果这个类中有被@abstarctmethod修饰的方法，就不能被实例化
class ProcessStrategy(ABC):

    # 引入abstractmethod装饰器，约束子类必须实现基类的process_file方法
    @abstractmethod
    def process_file(self, filepath):
        # 基类的方法中不需要定义具体的功能
        pass


class ExcelProcessStrategy(ProcessStrategy):
    def process_file(self, filepath):
        print("Processing excel file")


class CsvProcessStrategy(ProcessStrategy):
    def process_file(self, filepath):
        print("Processing csv file")


class TxtProcessStrategy(ProcessStrategy):
    def process_file(self, filepath):
        print("Processing txt file")


class FileProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_type = file_path.split('.')[-1]

    def process_file(self):
        if self.file_type == 'xlsx':
            ExcelProcessStrategy().process_file(self.file_path)
        elif self.file_type == 'csv':
            CsvProcessStrategy().process_file(self.file_path)
        elif self.file_type == 'txt':
            TxtProcessStrategy().process_file(self.file_path)


if __name__ == "__main__":
    file_processor = FileProcessor('file.xlsx')
    file_processor.process_file()
    file_processor = FileProcessor('file.csv')
    file_processor.process_file()
    file_processor = FileProcessor('file.txt')
    file_processor.process_file()
