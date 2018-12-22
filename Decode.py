#!/usr/bin/env python
import os
import re
import time
from shutil import get_terminal_size


def display_instructions():
    """
    Displays starting instructions
    """
    print('********************************************************************')
    print('************************** W E L C O M E ***************************')
    print('********************************************************************')
    print('\nInstruction:')
    print('        Paste the folder you want to decode in\n        Location: ', os.getcwd())
    print('        Rename the folder to any name starting with Encoded_message')
    print('\n********************************************************************')


def get_file():
    """
    Obtains the name of file to decode

    :return:
        (str) path_script - Path from where the script is run
        (str) decode_path - Path of the folder to decode
    """
    path_script = os.getcwd()

    # Finding the type of OS for appropriate separator
    if '/' in path_script:
        separator = '/'
    else:
        separator = '\\'

    while True:
        print('\nDo you want to manually enter the name & path of file to decode?')
        manual_input = input("Type 'yes' or 'no'.\n")
        manual_input = manual_input.lower()
        decode_path_obtained_flag = False

        if manual_input == 'yes' or manual_input == 'y' or manual_input == '1':
            while True:
                decode_path = input('\nEnter full path with name of folder you want to decode:\nEnter q to quit....\n')

                if decode_path == 'q' or decode_path == 'Q':
                    print('\nQuitting....')
                    print('************************* T H A N K  Y O U **************************')
                    quit(0)

                if not os.path.exists(decode_path):
                    print('\n********************************************************************')
                    print('The path you entered does not exist.\nPlease enter a valid path.')
                else:
                    decode_path_obtained_flag = True
                    break

        elif manual_input == 'no' or manual_input == 'n' or manual_input == '0':
            print('\nOkay, we will help you out with that....')
            print('********************************************************************')

            file_names = os.listdir(path_script)
            file_names_guessed = []

            # Removing the hidden files
            for index, files in enumerate(file_names):
                if files.startswith('.'):
                    del file_names[index]

            # Removing files if not folder
            for index, files in enumerate(file_names):
                if os.path.isfile(files):
                    del file_names[index]

            # Guessing decodable files
            for index, files in enumerate(file_names):
                if files.startswith('Encoded_message'):
                    file_names_guessed.append(files)

            if len(file_names_guessed):
                while True:
                    print('Select the folder you want to decode: ')

                    response_choice = []
                    for index, file in enumerate(file_names_guessed):
                        print('\t{}) {}'.format(index, file))
                        response_choice.append(str(index))

                    print('\nEnter a number from numbers listed above:')
                    response = input('Press Q if the folder you want to decode is not listed here....\n')
                    response = response.lower()

                    if response == 'q':
                        while True:
                            print('********************************************************************')
                            print('\nIs the folder you want to decode listed here?')
                            print('Select the folder you want to decode: ')

                            response_choice = []
                            for index, file in enumerate(file_names):
                                print('\t{}. {}'.format(index, file))
                                response_choice.append(str(index))

                            print('\nEnter a number from numbers listed above:')
                            response = input('Press Q if the folder you want to decode is not listed here....\n')
                            response = response.lower()

                            if response == 'q':
                                print('\n********************************************************************')
                                print('\nWe are SORRY for inconvenience.')
                                print('Restart the program and choose to manually input the location of file.')
                                print('\n************************* T H A N K  Y O U **************************')
                                quit(0)
                            elif response in response_choice:
                                decode_path = path_script + separator + file_names[int(response)]
                                decode_path_obtained_flag = True
                                break
                            else:
                                print('\nINVALID RESPONSE. Please choose a number from the available options.')
                    elif response in response_choice:
                        decode_path = path_script + separator + file_names_guessed[int(response)]
                        decode_path_obtained_flag = True
                        break
                    else:
                        print('\n********************************************************************')
                        print('INVALID INPUT. Please choose from the available options.\n')

                    # If decode path is obtained then exiting
                    if decode_path_obtained_flag:
                        break
            else:
                while True:
                    print('********************************************************************')
                    print('\nIs the folder you want to decode listed here?')
                    print('Select the folder you want to decode: ')

                    response_choice = []
                    for index, file in enumerate(file_names):
                        print('\t{}. {}'.format(index, file))
                        response_choice.append(str(index))

                    print('\nEnter a number from numbers listed above:')
                    response = input('Press Q if the folder you want to decode is not listed here....\n')
                    response = response.lower()

                    if response == 'q':
                        print('\n********************************************************************')
                        print('\nWe are SORRY for inconvenience.')
                        print('Restart the program and choose to manually input the location of file.')
                        print('\n************************* T H A N K  Y O U **************************')
                        quit(0)
                    elif response in response_choice:
                        decode_path = path_script + separator + file_names[int(response)]
                        decode_path_obtained_flag = True
                        break
                    else:
                        print('\nINVALID RESPONSE. Please choose a number from the available options.')
        else:
            print('\n********************************************************************')
            print("INVALID INPUT. Type 'yes' or 'no'.")

        # Breaking if decode path is obtained
        if decode_path_obtained_flag:
            break
    return path_script, decode_path


def check_decodable(decode_folder_path, path_script):
    """
    Checks whether file can be decodable or not

    :param:
        (str) decode_folder_path - Path of the folder containing encrypted message to decode
        (str) path_script - Path of the script from where it was run
    """
    # Checking whether folder can be decoded
    if not os.path.isdir(decode_folder_path):
        print('\n**************************** E R R O R ******************************')
        print('\nSelected folder can not be decoded')
        print('\nQuitting....')
        print('************************* T H A N K  Y O U **************************')
        quit(0)

    # Checking whether the path is a folder
    try:
        os.chdir(decode_folder_path)
    except:
        print('**************************** E R R O R ******************************')
        print('\n Selected folder can not be decoded')
        print('\nQuitting....')
        print('************************* T H A N K  Y O U **************************')
        quit(0)

    file_names = os.listdir(decode_folder_path)

    if not len(file_names):
        print('**************************** E R R O R ******************************')
        print('\n Selected folder is empty')
        print('\nQuitting....')
        print('************************* T H A N K  Y O U **************************')
        quit(0)


def decode_file(decode_folder_path, path_script):
    """
    Decodes the hidden letters to their original visible format

    :param:
        (str) decode_folder_path - Path of the folder containing encrypted message to decode
        (str) path_script - Path of the script from where it was run
    """
    os.chdir(decode_folder_path)

    print('***************** F O L D E R   T O   D E C O D E *******************')
    print('\nFolder name: ', decode_folder_path)

    start_time = time.time()
    file_names = os.listdir(decode_folder_path)

    # Decoding the message
    print('\n**************** D E C O D I N G    M E S S A G E *******************')
    for file in file_names:
        modified_file_name = file

        # Removing fake extensions
        extensions = ['.sys', '.ini']

        for ext in extensions:
            if modified_file_name.endswith(ext):
                modified_file_name = modified_file_name.rstrip(ext)

        # Removing the garbage numbers and . from names
        modified_file_name = re.sub('[^A-Za-z]', '', modified_file_name)

        # Converting the files to .jpg format
        modified_file_name = modified_file_name + '.jpg'

        # Renaming files
        os.rename(file, modified_file_name)
        print('Decoded hidden file {} to {}'.format(file, modified_file_name))

    print('\n********************************************************************')
    print('\nMESSAGES HAVE BEEN SUCCESSFULLY DECODED IN FOLDER: ', decode_folder_path)
    print('\nThis took about {} seconds.'.format(time.time() - start_time))
    print('\n********************************************************************')

    # Changing to original path for successful subsequent run of the same script
    os.chdir(path_script)


def main():
    display_instructions()
    path_script, decode_folder_path = get_file()
    check_decodable(decode_folder_path, path_script)
    decode_file(decode_folder_path, path_script)

    while True:
        response = input("\nDo you want to decode some mother messages? Type 'yes' or 'no'\n")
        response = response.lower()

        if response == 'no' or response == 'n' or response == '2':
            print('\nQuitting....')
            print('************************* T H A N K  Y O U **************************')
            quit(0)
        elif response == 'yes' or response == 'y' or response == '1':
            print('\n'*get_terminal_size().lines)
            main()
            quit(0)


if __name__ == '__main__':
    main()
