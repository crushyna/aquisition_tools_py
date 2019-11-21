import base64
import paramiko

host_address = '10.227.7.120'
key_file = r'data/axagc-openssh'

k = paramiko.RSAKey.from_private_key_file(key_file, password='norkom098')
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting...")
c.connect( hostname=host_address, username="centos", pkey=key_file)
print("Connected!")
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
    print("Executing {}".format(command))
    stdin , stdout, stderr = c.exec_command(command)
    print(stdout.read())
    print("Errors")
    print(stderr.read())
c.close()