import pyfiglet
import sys
import bext
import os
import keyboard
import requests
import re
import time

print('Booting up...')
time.sleep(1)
bext.bg('blue')
bext.fg('white')
bext.clear()
print(f'Welcome to\n{pyfiglet.figlet_format("Very Good OS")}\nPress CTRL to continue')
while not keyboard.is_pressed('ctrl'):
    pass

if sys.platform.startswith('linux'):
    os.system('clear')
else:
    os.system('cls')
# declare some variables here
version = 1.0
if sys.platform.startswith('linux'):
    real_os = 'linux'
else:
    real_os = 'window'


def main_menu():
    command = input('>')
    if command == 'help':
        print('Very Good OS Help:\echo, showdir, duckduckgo')
    elif command == 'showdir':
        for i in range(len(os.listdir(os.path.dirname(os.path.realpath(__file__))))):
            print(os.listdir(os.path.dirname(os.path.realpath(__file__)))[i])
    elif re.compile('echo (.*)').match(command):
        print(re.findall('echo (.*)', command)[0])
    elif command == 'duckduckgo':
        print(f'Welcome to', end='')
        bext.fg('green')
        print(f'\n{pyfiglet.figlet_format("DuckDuckGo")}')
        bext.fg('white')
        print('Powered by the DuckDuckGo API. (https://api.duckduckgo.com/api)\n')
        query = input('Please enter your search query.\n')
        with open('logs.txt', 'a') as history:
            history.write(f'{query}\n')
        results = requests.get(f'https://api.duckduckgo.com/?q={query}&format=json&pretty=1&t=verygoodos').json()
        print(results['AbstractText'])
    else:
        print('Invalid command.')
    main_menu()


main_menu()
