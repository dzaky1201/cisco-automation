import paramiko
import time
class Config:
    def __init__(self,address, username, password):
        self.address = address
        self.username = username
        self.password = password
    
    def start(self, conf):
        print(self.address, self.username, self.password)
        ip_address = self.address
        username = self.username
        password = self.password
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address, username=username, password=password)
        
        print("Berhasil login to {0}".format(ip_address))

        conn = ssh_client.invoke_shell()
        
        for index, item in enumerate(conf):
            conn.send(item + '\n')
            time.sleep(1)
            if index == len(conf) - 1 :
                output = conn.recv(65535)
                print(output)
                print('config selesai')
                ssh_client.close()
