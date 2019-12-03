import json
from dataclasses import dataclass


@dataclass
class JSONController:

    def __init__(self, connection_file):
        self.connection_filename = connection_file
        self.connection_details = self.extract_connection_info(self.connection_filename)
        self.server_ip = self.connection_details['host_ip']
        self.port = self.connection_details['port']
        self.username = self.connection_details['username']
        self.password = self.connection_details['password']
        self.key_filename = self.connection_details['key_file']
        self.remote_currentday = self.connection_details['remote_currentday']
        self.remote_endofday = self.connection_details['remote_endofday']
        self.remote_acquisition_waiting = self.connection_details['remote_acquisition']

    @staticmethod
    def extract_connection_info(connection_filename):
        with open(connection_filename, 'r') as json_file:
            connection_details = json.loads(json_file.read())
            return connection_details


