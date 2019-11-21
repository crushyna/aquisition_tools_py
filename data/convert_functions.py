import pandas as pd
import openpyxl
import xlrd
import time
# from data.columns_templates import getColumnsNames
from data.filespec_extractor import FileSpecsFinder


class ConvertFunctions:

    @staticmethod
    def createExcelFile(filename, template):
        try:
            dataframe = pd.read_csv('input/{}'.format(filename), sep='|', na_filter=False, index_col=False, header=None)
            dataframe.columns = FileSpecsFinder.return_list_of_fieldnames(template)
        except ValueError as ValueErrorMessage:
            print("Transformation error: {}".format(ValueErrorMessage))
            time.sleep(3)
            return 0
        xlsx_file_name = input("Enter desired file name: ")
        dataframe.to_excel("output_xlsx/{}.xlsx".format(xlsx_file_name))

    @staticmethod
    def createTextFromExcelFile(filename):
        dataframe = pd.read_excel('output_xlsx/{}'.format(filename), index_col=0, na_filter=False)
        selected_text_filename = input("Enter requested text file name: ")
        dataframe.to_csv('output_txt/{}.txt'.format(selected_text_filename), sep='|', header=False, index=False)