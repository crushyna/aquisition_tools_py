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

host = '10.227.7.120'
port = 22
username = 'centos'
password = 'norkom098'
key_file = r'data/axagc-openssh'
local_input = r'input'
local_output_txt = r'output_txt'
local_output_xlsx = r'output_xlsx'
temp_local_currentday = r'data/temp/currentday.txt'
temp_local_endofday = r'data/temp/endofday.txt'
remote_currentday = r'/opt/netrevealHome/data/acquisition/currentday.txt'
remote_endofday = r'/opt/netrevealHome/data/acquisition/endofday.txt'
remote_acquisition = r'/opt/netrevealHome/data/acquisition/waiting'
upload_local_dir = r'upload_dir'


templates = FileSpecsFinder.get_dict_of_templates()

currentFile = 'none'
fileTemplate = 'none'

main_menu = 1
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
        excelFilesList = listdir(local_output_xlsx)
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

        # check if files even exist and then connect
        uploadFilesList = listdir(upload_local_dir)
        uploadFilesNumber = len(uploadFilesList)
        if uploadFilesNumber > 0:

            # connect to server
            client = SftpClient(host, port,
                                username, password, key_file)

            # download currentday and endofday files
            client.download(remote_currentday, temp_local_currentday)
            client.download(remote_endofday, temp_local_endofday)

            temp_currentday = ConvertFunctions.returnValueFromTxt(temp_local_currentday)
            # print(temp_currentday)
            temp_endofday = ConvertFunctions.returnValueFromTxt(temp_local_endofday)
            # print(temp_endofday)

            answer = str(input(f"Found {uploadFilesNumber} files. Proceed? [Y/n] "))
            if answer in ('Y', 'y', 'yes'):

                # fun starts here
                result = DataUploader.check_file_names(uploadFilesList, uploadFilesNumber)
                if result == 1:
                    DataUploader.mass_uploader(uploadFilesList, temp_currentday, temp_endofday, upload_local_dir)
                else:
                    print("Files not named properly! Please fix their names before using uploader!")
                    pass

            else:
                pass

        else:
            print("No files to upload!")
            time.sleep(2)
            pass

    elif ans == "5":
        print("\n Goodbye!")
        main_menu = None
        time.sleep(2)

    else:
        print("\n Not valid choice, try again!")
        time.sleep(2)
