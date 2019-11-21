import sys
from os import listdir
from data.convert_functions import ConvertFunctions
from data.filespec_extractor import *
from data.ftp_controller_2 import *
import time
import os
import openpyxl
import xlrd

PROGRAM_VERSION = '0.5'

templates = FileSpecsFinder.get_dict_of_templates()

currentFile = 'none'
fileTemplate = 'none'

main_menu = True
while main_menu:
    print("""
    *** Acquisition Tool v{PROGRAM_VERSION} ***
    Select one of options below:
    1.  Load TXT file
    2.  Generate XLSX file
    3.  Generate fixed TXT file
    4.  Upload data
    5.  Exit/Quit
    """)
    ans = input("What would you like to do? ")

    if ans == "1":
        print("\n Load TXT file:")
        menu_1 = True

        txtFilesList = listdir('input')
        txtFilesNumber = len(txtFilesList)
        txtFilesDict = dict(zip(txtFilesList, range(txtFilesNumber)))
        txtFilesDictFixed = {v: k for k, v in txtFilesDict.items()}
        for key, value in txtFilesDictFixed.items():
            print(key, ": ", value)

        selectedFileId = int(input("Enter requested file ID: "))
        if selectedFileId < txtFilesNumber:
            currentFile = txtFilesDictFixed.get(selectedFileId)
            print("File loaded!\n")
            time.sleep(1)
            for key, value in templates.items():
                print(key, ": ", value)
            selectedTemplateKey = int(input("Select template: "))
            if int(selectedTemplateKey) <= len(templates):
                print("Selected template: ")
                print(templates.get(selectedTemplateKey))
                time.sleep(1)
                fileTemplate = templates.get(selectedTemplateKey)
            else:
                print("Improper selection, try again!")
                time.sleep(2)
        else:
            print("Improper file name. Try again!")
            time.sleep(2)

    elif ans == "2":
        print("\n Generate XLSX file: ")
        menu_2 = True
        print("Selected filename: " + currentFile)
        print("Selected template: " + fileTemplate)
        time.sleep(1)
        ConvertFunctions.createExcelFile(currentFile, fileTemplate)

    elif ans == "3":
        print("\n Generate fixed TXT file:")
        menu_3 = True
        excelFilesList = listdir('output_xlsx')
        excelFilesNumber = len(excelFilesList)
        excelFilesDict = dict(zip(excelFilesList, range(excelFilesNumber)))
        excelFilesDictFixed = {v: k for k, v in excelFilesDict.items()}
        for key, value in excelFilesDictFixed.items():
            print(key, ": ", value)

        selectedFileId = int(input("Enter requested file ID: "))
        if selectedFileId < excelFilesNumber:
            currentExcelFile = excelFilesDictFixed.get(selectedFileId)
            ConvertFunctions.createTextFromExcelFile(currentExcelFile)
        else:
            print("Improper file ID. Try again!")
            time.sleep(2)

    elif ans == "4":
        print("\n Upload data:")
        menu_4 = True
        client = SftpClient(host, port,
                            username, password, key_file)
        client.download('/opt/netrevealHome/data/acquisition/currentday.txt', 'data')

    elif ans == "5":
        print("\n Goodbye!")
        main_menu = None
        time.sleep(2)

    else:
        print("\n Not valid choice, try again!")
        time.sleep(2)
