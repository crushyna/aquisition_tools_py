from paramiko import Transport, SFTPClient, RSAKey
from datetime import date, datetime, timedelta
import os
import time
import errno
import logging

from data.filespec_extractor import FileSpecsFinder

logging.basicConfig(format='%(levelname)s : %(message)s',
                    level=logging.INFO)

# HAVE NO IDEA HOW TO INPUT THIS OTHER WAY (where to get from), SO IT'S HARDCODED FOR NOW
acquisition_order = {1: ['PARTY_ROLE', 'POLICY_STATUS'],
                     2: ['INTERMEDIARIES', 'INTERMEDIARY_TYPE'],
                     3: ['CUSTOMER_CATEGORY', 'CUSTOMER_STATUS'],
                     4: ['CUSTOMER_TYPE'],
                     5: ['COUNTRY'],
                     6: ['CUSTOMERS'],
                     7: ['PRODUCT'],
                     8: ['PRODUCT_SOURCE_TYPE'],
                     9: ['POLICIES]'],
                     10: ['CUSTOMER_POLICY_LINK', 'INTERMEDIARY_POLICY_LINK'],
                     11: ['OPERATIONS']}


class SftpClient:
    _connection = None

    def __init__(self, host, port, username, password, key_file):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.key_file = key_file

        self.create_connection(self.host, self.port,
                               self.username, self.password, self.key_file)

    @classmethod
    def create_connection(cls, host, port, username, password, key_file):

        RSA_key = RSAKey.from_private_key_file(key_file, password=password)
        transport = Transport(sock=(host, port))
        transport.connect(username=username, password=password, pkey=RSA_key)
        cls._connection = SFTPClient.from_transport(transport)

    @staticmethod
    def uploading_info(uploaded_file_size, total_file_size):

        logging.info('uploaded_file_size : {} total_file_size : {}'.
                     format(uploaded_file_size, total_file_size))

    def upload(self, local_path, remote_path):

        self._connection.put(localpath=local_path,
                             remotepath=remote_path,
                             callback=self.uploading_info,
                             confirm=True)

    def file_exists(self, remote_path):

        try:
            print('remote path : ', remote_path)
            self._connection.stat(remote_path)
        except IOError as e:
            if e.errno == errno.ENOENT:
                return False
            raise
        else:
            return True

    def download(self, remote_path, local_path, retry=5):

        if self.file_exists(remote_path) or retry == 0:
            self._connection.get(remote_path, local_path,
                                 callback=None)
        elif retry > 0:
            time.sleep(5)
            retry = retry - 1
            self.download(remote_path, local_path, retry=retry)

    def close(self):
        self._connection.close()


class DataUploader:

    @staticmethod
    def check_file_names(file_list: list, files_number: int):
        control_sum = 0
        filespecs_list_named = FileSpecsFinder.get_list_of_filespec_files_NAMES()
        print(f"Names accepted: {filespecs_list_named}")
        for each_filename in file_list:
            print(f"Filename check: {each_filename[:-13]}")
            if each_filename[:-13] in filespecs_list_named:
                control_sum += 1
            else:
                pass
        if control_sum == files_number:
            print("All files are OK!")
            time.sleep(1)
            return 1
        else:
            return 0

    @staticmethod
    def mass_uploader(file_list: list, temp_current_day: str, temp_end_of_day: str, upload_folder):
        current_date = datetime(year=int(temp_current_day[0:4]),    # they do return as INT
                                month=int(temp_current_day[4:6]),
                                day=int(temp_current_day[6:8]))

        for each_key, each_list in acquisition_order.items():

            for each_filename in file_list:
                file_to_upload = each_filename[:-13]
                # print(file_to_upload)
                # print(each_list)
                if file_to_upload in each_list:
                    print(f"Matched: {file_to_upload} with list {each_list}")
                    current_date += timedelta(days=1)
                    string_date = current_date.strftime("%Y%m%d")
                    new_filename = str(f"{file_to_upload}_{string_date}.txt")
                    os.rename(f'{upload_folder}/{each_filename}', f'{upload_folder}/{new_filename}')
                    time.sleep(1)
                    # TODO: its not recognizing POLICIES file somehow, fix that!
                    continue
                else:
                    continue


if __name__ == '__main__':
    host = '10.227.7.120'
    port = 22
    username = 'centos'
    password = 'norkom098'
    key_file = r'data/axagc-openssh'

    download_remote_path = r'data'
    download_local_path = r'test.txt'

    upload_local_path = r'data/test.txt'
    upload_remote_path = r'/opt/netrevealHome/data/acquisition'

    client = SftpClient(host, port,
                        username, password, key_file)

    client.upload(upload_local_path,
                  upload_remote_path)

    client.download(download_remote_path,
                    download_local_path)
    client.close()
