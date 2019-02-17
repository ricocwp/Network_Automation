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

stdin, stdout, stderr = ssh_client1.exec_command('routing rip interface add interface=ether1')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('routing rip interface add interface=ether2')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('routing rip interface add interface=ether3')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('routing rip network add network=192.168.10.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('routing rip network add network=192.168.2.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('routing rip network add network=192.168.20.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client1.exec_command('ip route print \n')
time.sleep(1)

output1 = stdout.readlines()

print('\n'.join(output1))

ssh_client1.close()

####################################################################################################################

ssh_client2 = paramiko.SSHClient()
ssh_client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client2.connect('192.168.100.4', port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.4 \n')

stdin, stdout, stderr = ssh_client2.exec_command('routing rip interface add interface=ether1')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('routing rip interface add interface=ether2')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('routing rip interface add interface=ether3')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('routing rip network add network=192.168.20.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('routing rip network add network=192.168.3.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('routing rip network add network=192.168.30.0/24')
time.sleep(1)

stdin, stdout, stderr = ssh_client2.exec_command('ip route print \n')
time.sleep(1)

output2 = stdout.readlines()

print('\n'.join(output2))

ssh_client2.close()
