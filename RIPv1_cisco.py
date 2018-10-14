import paramiko
import time
import sys

username = "klim"
password = "klim123"
port = "22"

####################################################################################################################
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect('192.168.100.2', port=port, username=username, password=password)

print('Berhasil Login ke 192.168.100.2 \n')

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print output
remote_conn.send("enable\n")
remote_conn.send("klim123\n")
remote_conn.send("configure terminal \n")
remote_conn.send("router rip \n")
remote_conn.send("network 192.168.1.0\n")
remote_conn.send("network 192.168.10.0 \n")
remote_conn.send("end \n")
remote_conn.send("write \n")
time.sleep(1)

remote_conn.send("show ip route \n")
time.sleep(1)

output = remote_conn.recv(65535)
print output

remote_conn_pre.close()
