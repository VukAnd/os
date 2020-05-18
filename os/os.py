# license!
"""
MIT License

Copyright (c) 2020 hellogoose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
version = 1.2
if sys.platform.startswith('linux'):
    real_os = 'linux'
else:
    real_os = 'windows'


def main_menu():
    command = input('>')
    if command == 'help':
        print('Very Good OS Help:\necho, showdir, duckduckgo, cat, delete [file], run [file]')
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
    elif re.compile('cat (.*)').match(command):
        data = re.findall('cat (.*)', command)[0]
        if data[0] == '>':
            data2 = []
            for i in range(len(data)):
                data2.append(data[i])
            del data2[0]
            data = ''
            for i in range(len(data2)):
                data += data2[i]
            contents = input('Enter content of file.\n')
            open(data, 'w').close()
            with open(data, 'w') as file:
                file.write(contents)
        else:
            with open(data, 'r') as file:
                print(file.read())
    elif re.compile('delete (.*)').match(command):
        os.remove(re.findall('delete (.*)', command)[0])
    elif re.compile('run (.*)').match(command):
        os.system(f'py {re.findall("run (.*)", command)[0]}')
    else:
        print('Invalid command.')
    main_menu()


main_menu()
