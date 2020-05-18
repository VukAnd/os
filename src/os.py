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
import sys
import random
import datetime
print('Booting up...')
time.sleep(1)
with open('logs.txt', 'w'):
    pass
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
_fg = 'white'
_bg = 'blue'
invader_count = 15


def main_menu():
    global _fg, _bg, invader_count
    command = input('>')
    if command == 'help':
        print('Very Good OS Help:\necho, showdir, duckduckgo, cat, delete [file], run [file], settings, rockpaperscissors, shutdown')
    elif command == 'showdir':
        for i in range(len(os.listdir(os.path.dirname(os.path.realpath(__file__))))):
            print(os.listdir(os.path.dirname(os.path.realpath(__file__)))[i])
    elif re.compile('echo (.*)').match(command):
        print(re.findall('echo (.*)', command)[0])
    elif command == 'duckduckgo':
        print(f'Welcome to', end='')
        bext.fg('green')
        print(f'\n{pyfiglet.figlet_format("DuckDuckGo")}')
        bext.fg(_fg)
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
    elif command == 'settings':
        print('Welcome to the Settings. Input the corresponding number for what you want.\n1 - Text Color/Colour\n2 - Background Color/Colour\n3 - System Info\n4- Game-related\n5 - Exit')
        choice = input()
        if choice == '1':
            choice = input('Please input your choice:\nblack\nred\ngreen\nyellow\nblue\npurple\ncyan\nwhite\nrandom\n')
            try:
                bext.fg(choice)
                _fg = choice
            except KeyError:
                print('Invalid color/colour.')
        elif choice == '2':
            choice = input('Please input your choice:\nblack\nred\ngreen\nyellow\nblue\npurple\ncyan\nwhite\nrandom\n')
            try:
                bext.bg(choice)
                _bg = choice
            except KeyError:
                print('Invalid color/colour.')
        elif choice == '3':
            print(f'System Info:\nVersion: {version}')
            latest_version = requests.get('https://raw.githubusercontent.com/hellogoose/os/master/version.txt')
            if latest_version > version:
                print('A new update is available!')
        elif choice == '4':  # todo
            choice = input('Game Settings:\n1 - Change Invader Count\n2 - Exit')
            if choice == '1':
                invader_count = input(f'Current: {invader_count}\nNew: ')
                print('Changed.')
            elif choice == '2':
                print('Thank you. Have a nice day!')
        elif choice == '5':
            print('Thank you. Have a nice day!')
    elif command == 'shutdown':
        if real_os == 'linux':
            os.system('clear')
        else:
            os.system('cls')
        bext.fg('reset')
        bext.bg('reset')
        bext.clear()
        print('Thank you for using Very Good OS! Have a nice day!')
        sys.exit()
    elif command == 'rockpaperscissors':
        # variables
        ai_score = 0
        player_score = 0
        round = 0
        # end variables
        bext.bg('black')
        bext.clear()
        bext.fg('red')
        print('Rock', end='')
        bext.fg('yellow')
        print('Paper', end='')
        bext.fg('green')
        print('Scissors')
        bext.fg('white')
        print('Type EXIT to exit.')
        while True:
            bext.bg('black')
            bext.clear()
            bext.fg('red')
            print('Rock', end='')
            bext.fg('yellow')
            print('Paper', end='')
            bext.fg('green')
            print('Scissors')
            bext.fg('white')
            print(f'Round {round}\nYou: {player_score}\nAI: {ai_score}')
            player_choice = input('Pick a move. (R/P/S)\n')
            ai_choice = random.choice(['Rock', 'Paper', 'Scissors'])
            print(f'AI picks {ai_choice}')
            if player_choice == 'R':
                if ai_choice == 'Paper':
                    print('AI wins!')
                    ai_score += 1
                elif ai_choice == 'Scissors':
                    print('You win!')
                    player_score += 1
                else:
                    print('Tie.')
            elif player_choice == 'P':
                if ai_choice == 'Scissors':
                    print('AI wins!')
                    ai_score += 1
                elif ai_choice == 'Rock':
                    print('You win!')
                    player_score += 1
                else:
                    print('Tie.')
            elif player_choice == 'S':
                if ai_choice == 'Paper':
                    print('You win!')
                    player_score += 1
                elif ai_choice == 'Rock':
                    print('AI wins!')
                    ai_score += 1
                else:
                    print('Tie.')
            elif player_choice == 'EXIT':
                break
            else:
                print('Invalid choice.')
            time.sleep(0.5)
            if real_os == 'linux':
                os.system('clear')
            else:
                os.system('cls')
            round += 1
        print('Thank you for playing. Have a nice day!')
        time.sleep(0.5)
        bext.bg(_bg)
        bext.fg(_fg)
        bext.clear()
        if real_os == 'linux':
            os.system('clear')
        else:
            os.system('cls')
    else:
        print('Invalid command.')
    main_menu()


main_menu()
