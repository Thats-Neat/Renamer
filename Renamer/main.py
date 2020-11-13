import time
import os
from os import system
import ctypes



HOST_FOLDER_LOC = '' # change to nothing later
HOST_FOLDER_NAME = 'Host Folder' # change to nothing later
#HOST_FOLDER_TYPE = 'txt' # change to nothing later

NUMBER_OF_FILES = 0

FILE_NUM = 1
FILE_NAME = 0
FILE_TYPE = 0


# default settings could be on a txt file for keeping
# have for all inputs be able to use the number or text
# replace all avaible spaces with \n
# speed up time between lines being printed
# possibly change input symbol

#root.iconbitmap(default='icon.ico')

def titleScreen():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Renamer | ThatsNeat | Main Menu")
    print('')
    print('   ██████╗░███████╗███╗░░██╗░█████╗░███╗░░░███╗███████╗██████╗░')
    time.sleep(0.1)
    print('   ██╔══██╗██╔════╝████╗░██║██╔══██╗████╗░████║██╔════╝██╔══██╗')
    time.sleep(0.1)
    print('   ██████╔╝█████╗░░██╔██╗██║███████║██╔████╔██║█████╗░░██████╔╝')
    time.sleep(0.1)
    print('   ██╔══██╗██╔══╝░░██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗')
    time.sleep(0.1)
    print('   ██║░░██║███████╗██║░╚███║██║░░██║██║░╚═╝░██║███████╗██║░░██║')
    time.sleep(0.1)
    print('   ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝')
    print('')
    print('[1] Setup')
    time.sleep(0.1)
    print('[2] Rename')
    time.sleep(0.1)
    print('[3] Help')
    time.sleep(0.1)
    print('[4] Settings')
    time.sleep(0.1)
    print('[5] Error Guide')
    time.sleep(0.1)
    print('')

def setup():
    ctypes.windll.kernel32.SetConsoleTitleW("Renamer | ThatsNeat | Setup")
    global NUMBER_OF_FILES
    NUMBER_OF_FILES = 0
    print('')
    print('   ░██████╗███████╗████████╗██╗░░░██╗██████╗░')
    time.sleep(0.1)
    print('   ██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗')
    time.sleep(0.1)
    print('   ╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝')
    time.sleep(0.1)
    print('   ░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░')
    time.sleep(0.1)
    print('   ██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░')
    time.sleep(0.1)
    print('   ╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░')
    print('')
    print('[1] Create Host Folder')
    time.sleep(0.1)
    print('[2] File Amount Check')
    time.sleep(0.1)
    print('[*] Press Enter to Return to Menu')
    time.sleep(0.1)
    print('')
    setup = input('==> ')

    if setup.lower() == '1':
        try:
            print('Creating Host Folder...')
            time.sleep(1)
            os.mkdir('{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME))
            print('Host Folder Made!')
            time.sleep(1)
        except:
            print('')
            print('-ERROR-')
            input('')

    if setup.lower() == '2':
        try:
            print('Checking Amount...')
            time.sleep(1)
            print('')
            for fname in os.listdir('{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME)):
                NUMBER_OF_FILES += 1

            print('Number of files - {}'.format(NUMBER_OF_FILES))
            input('')
        except:
            print('')
            print('-ERROR-')
            input('')


def rename():
    ctypes.windll.kernel32.SetConsoleTitleW("Renamer | ThatsNeat | Rename")
    global NUMBER_OF_FILES
    global FILE_NUM
    NUMBER_OF_FILES = 0
    try:
        for fname in os.listdir('{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME)):
            NUMBER_OF_FILES += 1
    except:
        print('')
        print('-ERROR-')
        input('')

    print('')
    print('   ██████╗░███████╗███╗░░██╗░█████╗░███╗░░░███╗███████╗')
    time.sleep(0.1)
    print('   ██╔══██╗██╔════╝████╗░██║██╔══██╗████╗░████║██╔════╝')
    time.sleep(0.1)
    print('   ██████╔╝█████╗░░██╔██╗██║███████║██╔████╔██║█████╗░░')
    time.sleep(0.1)
    print('   ██╔══██╗██╔══╝░░██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░')
    time.sleep(0.1)
    print('   ██║░░██║███████╗██║░╚███║██║░░██║██║░╚═╝░██║███████╗')
    time.sleep(0.1)
    print('   ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝')
    print('')
    print('[1] Start Process')
    time.sleep(0.1)
    print('[+] Files Found - {}'.format(NUMBER_OF_FILES))
    time.sleep(0.1)
    print('[+] Parent Folder - {}'.format(HOST_FOLDER_LOC))
    time.sleep(0.1)
    print('[+] Host Folder Name - {}'.format(HOST_FOLDER_NAME))
    time.sleep(0.1)
    print('[*] Press Enter to Return to Menu')
    time.sleep(0.1)
    print('')
    rename = input('==> ')
    print('')

    if rename.lower() in ['start process', '1', 'one']:
        newName = input('New Name: ')
        print('')
        print('Renaming Files...')
        time.sleep(2)
        #try:
        for file in os.listdir('{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME)):
            src = file
            FILE_NAME, FILE_TYPE = os.path.splitext(src)
            FILE_NAME = newName
            newFile = str(FILE_NAME) + str(FILE_NUM) + str(FILE_TYPE)
            os.rename('{}/{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME, src), '{}/{}/{}'.format(HOST_FOLDER_LOC, HOST_FOLDER_NAME, newFile))
            FILE_NUM += 1
        print('')
        print('Files Renamed!')
        input('')
        stop()

        #except:
            #print('')
            #print('-ERROR-')
            #input('')




def help():
    ctypes.windll.kernel32.SetConsoleTitleW("Renamer | ThatsNeat | Help")
    print('')
    print('   ██╗░░██╗███████╗██╗░░░░░██████╗░')
    time.sleep(0.1)
    print('   ██║░░██║██╔════╝██║░░░░░██╔══██╗')
    time.sleep(0.1)
    print('   ███████║█████╗░░██║░░░░░██████╔╝')
    time.sleep(0.1)
    print('   ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░')
    time.sleep(0.1)
    print('   ██║░░██║███████╗███████╗██║░░░░░')
    time.sleep(0.1)
    print('   ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░')
    print('')
    print('[+] If you already have a host folder (were the files are located) go into the settings and paste the exact parent folder location')
    time.sleep(0.1)
    print('[+] If you dont have a host folder go into setup and create one')
    time.sleep(0.1)
    print('[+] Before you rename make sure the host folder name and parent location are correct')
    time.sleep(0.1)
    print('[+] The parent folder is the folder that is holding the host folder')
    time.sleep(0.1)
    print('[+] If youre getting errors go into the error guide')
    time.sleep(0.1)
    print('[+] Before you make a host folder go into settings and set parent folder and/or host folder name')
    time.sleep(0.1)
    print('[*] Press Enter to Return to Menu')
    time.sleep(0.1)
    print('')
    input('==> ')



def settings():
    ctypes.windll.kernel32.SetConsoleTitleW("Renamer | ThatsNeat | Settings")
    global HOST_FOLDER_LOC
    global HOST_FOLDER_NAME
    print('')
    print('   ░██████╗███████╗████████╗████████╗██╗███╗░░██╗░██████╗░░██████╗')
    time.sleep(0.1)
    print('   ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░██╔════╝')
    time.sleep(0.1)
    print('   ╚█████╗░█████╗░░░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░╚█████╗░')
    time.sleep(0.1)
    print('   ░╚═══██╗██╔══╝░░░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗░╚═══██╗')
    time.sleep(0.1)
    print('   ██████╔╝███████╗░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝██████╔╝')
    time.sleep(0.1)
    print('   ╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░')
    print('')
    print('[1] Host Folder Parent Location - {}'.format(HOST_FOLDER_LOC))
    time.sleep(0.1)
    print('[2] Host Folder Name - {}'.format(HOST_FOLDER_NAME))
    time.sleep(0.1)
    print('[*] Press Enter to Return to Menu')
    time.sleep(0.1)
    print('')
    settings = input('==> ')

    try:
        if settings.lower() == '1':
            HOST_FOLDER_LOC = input('New Parent Folder Location: ')
            print('')
            print('Changing Folder...')
            time.sleep(1)
            print('')
            print('Folder Changed!')
            time.sleep(1.5)

        if settings.lower() == '2':
            HOST_FOLDER_NAME = input('New Host Folder Name: ')
            print('')
            print('Changing Name...')
            time.sleep(1)
            print('')
            print('Name Changed!')
            time.sleep(1.5)
    except:
        print('')
        print('-ERROR-')
        input('')


def error():
    print('placeholder')


while True:
    titleScreen()
    mainMenu = input('==> ')

    if mainMenu.lower() in ['setup', '1', 'one']:
        os.system('cls')
        setup()

    elif mainMenu.lower() in ['rename', '2', 'two']:
        os.system('cls')
        rename()

    elif mainMenu.lower() in ['help', '3', 'three']:
        os.system('cls')
        help()

    elif mainMenu.lower() in ['settings', '4', 'four']:
        os.system('cls')
        settings()

    elif mainMenu.lower() in ['error guide', '5', 'five']:
        os.system('cls')
        error()

    else:
        print('-ERROR-')
        input('')
        os.system('cls')
