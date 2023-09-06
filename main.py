from config import Config

address = input('Masukan ip address : ')
username = input('masukan username : ')
password = input('masukan password : ')
syntax = input('masukan konfig : ')

config = [
    'conf t',
    'int e1/0',
    'no sh',
    'ip addr 10.10.10.1 255.255.255.252'
]

conf = Config(address, username, password)
conf.start(syntax)