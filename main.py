from config import Config

address = input('Masukan ip address : ')
username = input('masukan username : ')
password = input('masukan password : ')
syntax = input('masukan konfig : ')

conf = Config(address, username, password)
conf.start(syntax.split(', '))