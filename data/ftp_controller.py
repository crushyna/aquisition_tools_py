from pprint import pprint
import paramiko


class FtpController:

    def __init__(self):
        self.host_address = '10.227.7.120'
        self.key_file = r'data/axagc-openssh'
        self.PASSWORD = 'norkom098'
        self.USERNAME = 'centos'
        self.command_currentday = "sudo cat /opt/netrevealHome/data/acquisition/currentday.txt"
        self.command_endofday = "sudo cat /opt/netrevealHome/data/acquisition/endofday.txt"

    def set_server_ip(self, ip_address):
        self.host_address = ip_address

    def set_keyfile_location(self, keyfile_location):
        self.key_file = keyfile_location

    def set_user_password(self, password):
        self.PASSWORD = password

    def set_user_login(self, *login):
        self.USERNAME = login

    def connect_to_server(self):
        k = paramiko.RSAKey.from_private_key_file(self.key_file, password=self.PASSWORD)
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting...")
        c.connect(hostname=self.host_address, username=self.USERNAME, pkey=k)
        print("Connected!")

    def return_current_and_endofday(self):
        k = paramiko.RSAKey.from_private_key_file(self.key_file, password=self.PASSWORD)
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting...")
        c.connect(hostname=self.host_address, username=self.USERNAME, pkey=k)
        print("Connected!")

        commands = [self.command_currentday, self.command_endofday]
        days_info = []

        for command in commands:
            # print("Executing {}".format(command))
            stdin, stdout, stderr = c.exec_command(command)
            answer = stdout.read().decode('ascii').strip("\n")
            pprint(answer)
            days_info.append(answer)
            # print("Errors")
            # print(stderr.read())
        c.close()
        return days_info

    def upload_file_to_server(self):
        k = paramiko.RSAKey.from_private_key_file(self.key_file, password=self.PASSWORD)
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting...")
        c.connect(hostname=self.host_address, username=self.USERNAME, pkey=k)
        print("Connected!")

        sftp = paramiko.SFTP

        c.close()
        return days_info

connection1 = FtpController()
