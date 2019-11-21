import xml.etree.ElementTree as ET
from os import listdir


class FileSpecsFinder:
    """
    testing purposes only
    not a working version
    """

    @staticmethod
    def get_list_of_filespec_files():
        filespecs_file_list = listdir(r'data/filespecs')
        return filespecs_file_list

    @staticmethod
    def get_dict_of_templates():
        templates_list = []
        # templates_dict = {}
        for each_filespec_object in filespecs_objects:
            templates_list.append(each_filespec_object.return_filespec_name())

        templates_dict = dict(zip(range(0, len(templates_list)), templates_list))

        return templates_dict

    @staticmethod
    def return_list_of_fieldnames(template_name):
        for each_filespec_object in filespecs_objects:
            if each_filespec_object.filespec_name == template_name:
                # print(each_filespec_object.return_list_of_fieldnames())
                return each_filespec_object.return_list_of_fieldnames()


class FileSpecParser:
    """
    Creates an object out of every filespec file in filespecs folder
    Each object then carries data regarding:
    - original xml filename
    - distinct filespec name
    - list of fieldnames (used as columns to export)
    """

    def __init__(self, xml_filename: str):
        self.xml_filename = xml_filename
        self.filespec_name = str(xml_filename[9:-4])
        self.fieldnames_list = []

    def return_filespec_name(self):
        return self.filespec_name

    def return_list_of_fieldnames(self):
        return self.fieldnames_list

    def get_list_of_fieldnames(self):
        tree = ET.parse(f'data/filespecs/{self.xml_filename}')
        root = tree.getroot()

        for each_rfrecordspec in root.iter('rfrecordspec'):
            self.fieldnames_list.append(each_rfrecordspec.attrib['fieldname'])

        return self.fieldnames_list


# initialization commands
filespecs_list = FileSpecsFinder.get_list_of_filespec_files()
filespecs_objects = []
for each_filespec_file in filespecs_list:
    filespecs_objects.append(FileSpecParser(xml_filename=each_filespec_file))

for each_filespec_object in filespecs_objects:
    each_filespec_object.get_list_of_fieldnames()
