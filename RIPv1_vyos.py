import paramiko
import time
import sys


username = "klim"
password = "klim123"
port = "22"

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect("192.168.100.5", port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.5 \n')

connection = session.invoke_shell(term='vt100', width=250, height=100)

# Send a command to the channel
connection.send("configure\n")
connection.send("set protocols rip network 192.168.30.0/24\n")
time.sleep(1)

connection.send("set protocols rip network 192.168.4.0/24\n")
time.sleep(1)

connection.send("set protocols rip redistribute connected\n")
time.sleep(1)

connection.send("commit\n")
time.sleep(1)

connection.send("save\n")
time.sleep(1)

connection.send("run show ip route\n")
time.sleep(1)

cmd_output = connection.recv(65535)
print cmd_output

session.close()
