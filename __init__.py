import os
import configparser
from spotdl import Spotdl

if not os.path.exists('download-list.txt'):
  with open('download-list.txt', 'x') as file:
    file.write('')

if not os.path.exists('config.ini'):
  config = configparser.ConfigParser()
  config['API'] = {'client_id': ' ', 'client_secret': ' '}
  with open('config.ini', 'w') as configfile:
    config.write(configfile)
    print('Created config.ini')
    exit()

config = configparser.ConfigParser()
config.read('config.ini')
spotdl = Spotdl(
  output = './output/',
  # log_level='DEBUG',
  client_id = config['API']['client_id'],
  client_secret = config['API']['client_secret']
)

with open('download-list.txt') as file:
  lines = file.readlines()
  spotdl.download_songs(spotdl.search(lines))
