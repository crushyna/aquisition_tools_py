from paramiko import Transport, SFTPClient, RSAKey
import time
import errno
import logging

logging.basicConfig(format='%(levelname)s : %(message)s',
                    level=logging.INFO)


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
