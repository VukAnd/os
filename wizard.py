import os
import urllib.request
import time
print('Welcome to the setup wizard. This will install the required packages and the OS on your computer. The OS will be installed in the folder of this wizard.')
proceed = input('Proceed? (Y/N)\n')
if proceed == 'Y' or proceed == 'y':
    print('Okay. Do you accept the disclaimer below?\nThe developer is not responsible for any losses this program may be responsible for.')
    proceed = input('(Y/N)\n')
    if proceed == 'Y' or proceed == 'y':
        os.system('pip install keyboard')
        os.system('pip install bext')
        os.system('pip install pyfiglet')
        os.system('pip install requests')
        print('Required modules installed. Installing OS...')
        urllib.request.urlopen('https://github.com/hellogoose/os/releases/download/v1.3/os.zip')
        print('Finished. Please unzip the file. Welcome to the new age of operating systems!')
        time.sleep(1)
    else:
        print('Cancelled. Have a nice day!')
else:
    print('Cancelled. Have a nice day!')
