import sys
from data.convert_functions import ConvertFunctions
from data.filespec_extractor import *
from data.ftp_controller_2 import *
from data.json_controller import JSONController
import time
import openpyxl
import xlrd


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


PROGRAM_VERSION = '0.7'

templates = FileSpecsFinder.get_dict_of_templates()
connection_template = 'connection_data.json'
connection1 = JSONController(connection_template)

local_input = r'input/'
local_output_txt = r'output_txt'
local_output_xlsx = r'output_xlsx'
temp_local_currentday = r'data/temp/currentday.txt'
temp_local_endofday = r'data/temp/endofday.txt'
upload_local_dir = r'upload_dir/'

currentFile = 'none'
fileTemplate = 'none'

main_menu = 1
while main_menu:
    print(f"""
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
            client = SftpClient(connection1.server_ip, connection1.port,
                                connection1.username, connection1.password, connection1.key_filename)

            # download currentday and endofday files
            client.download(connection1.remote_currentday, temp_local_currentday)
            client.download(connection1.remote_endofday, temp_local_endofday)

            # turn currentday and endofday into strings
            temp_currentday = ConvertFunctions.returnValueFromTxt(temp_local_currentday)
            temp_endofday = ConvertFunctions.returnValueFromTxt(temp_local_endofday)

            answer = str(input(f"Found {uploadFilesNumber} files. Proceed? [Y/n] "))
            if answer in ('Y', 'y', 'yes'):

                # fun starts here
                result = DataUploader.check_file_names(uploadFilesList, uploadFilesNumber)
                if result == 1:
                    new_end_date = DataUploader.cook_upload_files(uploadFilesList, temp_currentday, upload_local_dir)
                    cooked_files = listdir(upload_local_dir)

                    for each_file in cooked_files:
                        source = f'{upload_local_dir}/{each_file}'
                        # destination = f'{remote_acquisition}/{each_file}' TEST DESTINATION
                        destination = f'{connection1.remote_acquisition_waiting}/{each_file}'
                        client.upload(source, destination)

                    # upload cooked files
                    with open(temp_local_endofday, 'w+') as new_endofday:
                        new_endofday.write(new_end_date)

                    # upload new endofday.txt
                    client.upload(temp_local_endofday, connection1.remote_endofday)


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
