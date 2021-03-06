from pandas import read_csv, read_excel
import xlrd
import time
from data.filespec_extractor import FileSpecsFinder


class ConvertFunctions:

    @staticmethod
    def createExcelFile(filename: str, template: str):
        try:
            dataframe = read_csv('input/{}'.format(filename), sep='|', na_filter=False, index_col=False, header=None)
            dataframe.columns = FileSpecsFinder.return_list_of_fieldnames(template)
        except ValueError as ValueErrorMessage:
            print("Transformation error: {}".format(ValueErrorMessage))
            time.sleep(3)
            return 0
        xlsx_file_name = input("Enter desired file name: ")
        dataframe.to_excel("output_xlsx/{}.xlsx".format(xlsx_file_name))

    @staticmethod
    def createTextFromExcelFile(filename: str):
        dataframe = read_excel('output_xlsx/{}'.format(filename), index_col=0, na_filter=False)
        selected_text_filename = input("Enter requested text file name: ")
        dataframe.to_csv('output_txt/{}.txt'.format(selected_text_filename), sep='|', header=False, index=False)

    @staticmethod
    def returnValueFromTxt(filename: str) -> str:
        with open(filename) as file:
            line = file.readline()
            return line
