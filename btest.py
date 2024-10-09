import paramiko
import datetime

# Time Stamp
now = datetime.datetime.now()
login = ['192.168.76.180', 2024, 'dika', 'dika989']

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname=login[0],port=login[1],username=login[2],password=login[3])
print('\n' +\
    f"Success Login to '{login[0]}' {now}")
print(
    "\n" +\
    "=" * 30 +\
    "Direction" +\
    "=" * 30
    )
print("a.transmit")
print("b.receive")
direction=input("Choose a/b ? ")

def transmit():
    getData = (f"tool bandwidth-test address={login[0]} protocol=tcp direction=transmit user={login[2]} \
                password={login[3]} local-tx-speed=100M connection-count=2 duration=100s")                                                              

    stdin,stdout,stderr = ssh_client.exec_command(getData)
    while True:
        line = stdout.readline()
        if not line:
            break
        print(line, end="")

def receive():
    getData = (f"tool bandwidth-test address={login[0]} protocol=tcp direction=receive user={login[2]} \
                password={login[3]} remote-tx-speed=100M connection-count=2 duration=100s")
    stdin,stdout,stderr = ssh_client.exec_command(getData)
    while True:
        line = stdout.readline()
        if not line:
            break
        print(line, end="")

if direction == 'a':
    transmit()
if direction == 'b':
    receive()
ssh_client.close()


