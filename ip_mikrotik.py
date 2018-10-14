import paramiko
import time
import sys

username = "klim"
password = "klim123"
port = "22"

ssh_client1 = paramiko.SSHClient()
ssh_client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client1.connect('192.168.100.3', port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.3 \n')

stdin, stdout, stderr = ssh_client1.exec_command('system identity set name=CHR1 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('ip address add address=192.168.10.2/24 interface=ether1 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('ip address add address=192.168.20.1/24 interface=ether2 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('ip address add address=192.168.2.1/24 interface=ether3 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('ip address print \n')
time.sleep(1)

output1 = stdout.readlines()

print('\n'.join(output1))

ssh_client1.close()

####################################################################################################################

ssh_client2 = paramiko.SSHClient()
ssh_client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client2.connect('192.168.100.4', port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.4 \n')

stdin, stdout, stderr = ssh_client2.exec_command('system identity set name=CHR2 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('ip address add address=192.168.20.2/24 interface=ether1 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('ip address add address=192.168.30.1/24 interface=ether2 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('ip address add address=192.168.3.1/24 interface=ether3 \n')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('ip address print \n')
time.sleep(1)

output2 = stdout.readlines()

print('\n'.join(output2))

ssh_client2.close()
