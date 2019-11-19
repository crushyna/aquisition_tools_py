import pandas as pd
import openpyxl
import xlrd
import time
from data.templateColumns import getColumnsNames

def createExcelFile(filename, template):
    try:
        dataframe = pd.read_csv('input/{}'.format(filename), sep='|', na_filter=False, index_col=False, header=None)
        dataframe.columns = getColumnsNames(template)
    except ValueError as ValueErrorMessage:
        print("Transformation error: {}".format(ValueErrorMessage))
        time.sleep(3)
        return 0
    xlsxFileName = input("Enter desired file name: ")
    dataframe.to_excel("output_xlsx/{}.xlsx".format(xlsxFileName))
    #print(dataframe)

def createTextFromExcelFile(filename):
    dataframe = pd.read_excel('output_xlsx/{}'.format(filename), index_col=0, na_filter=False)
    selectedTextFileName = input("Enter requested text file name: ")
    csvDataframe = dataframe.to_csv('output_txt/{}.txt'.format(selectedTextFileName), sep='|', header=False, index=False)