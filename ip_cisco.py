import paramiko
import time
import getpass

username = "klim"
password = "klim123"
port = "22"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.100.2',port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.2 \n')
conn = ssh_client.invoke_shell()

conn.send("enable\n")
conn.send("klim123\n")
conn.send("configure terminal\n")
conn.send("int fa0/0\n")
conn.send("ip address 192.168.10.1 255.255.255.0\n")
conn.send("no shut\n")
conn.send("exit\n")
conn.send("int fa0/1\n")
conn.send("ip address 192.168.1.1 255.255.255.0\n")
conn.send("no shut\n")
conn.send("end\n")
conn.send("write\n")
conn.send("show ip int br | i up\n")
time.sleep(1)

output = conn.recv(65535)
print output

ssh_client.close()
