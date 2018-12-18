#!/usr/bin/env python
import os
import time
from random import random, randrange, seed
import shutil
from shutil import get_terminal_size


def check_dependencies():
    """
    Checks whether the required files are present or not.

    :return:
        (str) path_script - Path from where the script is run
        (str) source_letter_path - Path where the alphabets are to be found.
    """
    # Path from where the script is run
    path_script = os.getcwd()

    # Finding the path of the alphabets folder depending on OS
    if os.name == 'nt':
        source_letter_path = path_script + '\\Alphabets'
    else:
        source_letter_path = path_script + '/Alphabets'

    # If Alphabets folder does not exist then display error and quit
    if not os.path.exists(source_letter_path):
        print('\nChecking dependencies....')
        print('************************ E R R O R *************************')
        print('Alphabets folder is not found in\nLocation: ', path_script)
        print('\n\nTroubleshooting tips:\
        \nDownload and copy the Alphabets folder in above location from the git repository: ')
        print('\n******************** T H A N K  Y O U **********************')
        quit(0)

    # If Alphabets folder exists then checking whether all the letters are present or not.
    else:
        os.chdir(source_letter_path)

        original_files = ['austin.jpg', 'athens.jpg', 'cairo.jpg', 'hyderabad.jpg', 'istanbul.jpg',
                          'bangalore.jpg', 'berkeley.jpg', 'chennai.jpg', 'houston.jpg', 'madrid.jpg',
                          'gainesville.jpg', 'bristol.jpg', 'edinbrugh.jpg', 'london.jpg', 'chicago.jpg',
                          'bogota.jpg', 'beijing.jpg', 'karachi.jpg', 'buenos aires.jpg', 'kiev.jpg',
                          '.DS_Store', 'delhi.jpg', 'bucharest.jpg', 'jacksonville.jpg', 'colombo.jpg',
                          'barcelona.jpg', 'dallas.jpg', 'los angeles.jpg', 'ithaca.jpg']

        files_present = os.listdir(source_letter_path)
        missing_files = []

        # Checking for missing alphabets in Alphabet folder
        for file in original_files:
            if file not in files_present:
                missing_files.append(file)

        # If some files are missing form alphabet folder then showing error and exiting.
        if len(missing_files):
            print('\nChecking dependencies....')
            print('************************ E R R O R *************************')
            print('Total number of missing files: ', len(missing_files))
            print('\nLocation of missing files: ', source_letter_path)
            print('\nMissing file-names from Alphabets folder:')

            for file in missing_files:
                print(file, end=', ')

            print('\n\nKindly paste the missing files in specified location and try again later.')
            print('\n******************** T H A N K  Y O U **********************')
            quit(0)

    os.chdir(path_script)
    return path_script, source_letter_path


def display_rules():
    """
    Displays the rules of entering message and what characters will be ignored.
    """
    print('************************************************************')
    print('\nINSTRUCTIONS:\n    \t1. Alphabets from A-Z or a-z are allowed.\n    \t2. Words can be separated by spaces.\
         \n    \t3. Sentences can be terminated by full stop(.)\
         \n    \t4. No numeric or special characters are allowed.')
    print('\nWARNING: Characters not mentioned above will be ignored.')


def get_message():
    """
    Message is taken as input from user. If invalid characters are found user is prompted to take necessary actions.

    :return:
        (str) valid_message - The valid message after removing the invalid characters(if any).
    """
    while True:
        print('\n*********************** INPUT MESSAGE **********************')
        message = input('\nPLEASE ENTER YOUR MESSAGE:\n')

        valid_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .')
        invalid_characters = []
        valid_message = []

        # Finding the invalid characters which will be ignored.
        for letter in message:
            if letter not in valid_characters:
                invalid_characters.append(letter)
            else:
                valid_message.append(letter)

        # If whole message is invalid
        if len(invalid_characters) == len(message):
            print('\n************************ E R R O R *************************')
            print('\nAll the characters entered in your message are invalid.')

            # Asking whether user wants to reenter the message
            while True:
                reenter_message = input('\nWould you like to re-enter your message? \nType:\n    1. yes\n    2. no\n')
                reenter_message = reenter_message.lower()

                if reenter_message == '1' or reenter_message == 'yes' or reenter_message == 'y':
                    print()
                    display_rules()
                    break
                elif reenter_message == '2' or reenter_message == 'no' or reenter_message == 'n':
                    print('\n******************** T H A N K  Y O U **********************')
                    quit(0)
                else:
                    print('\n************************************************************')
                    print("\nInvalid input. Please enter 'yes' or 'no'")

        # If there are invalid character in message then print this block
        elif len(invalid_characters):
            print('\n********************* INVALID CHARACTERS *******************')

            for letter in invalid_characters:
                print(letter, end=' ')

            print('\n\n************** MESSAGE AFTER REMOVING INVALIDS *************')
            print(''.join(valid_message))
            print('\n************************ CONFIRMATION **********************')

            while True:
                reenter_message = input('Do you want to encode the message as displayed above?\
                \nPress 1 to ENCODE it.\nPress 2 to RE-ENTER message.\nPress 3 to QUIT.\nEnter your response:\n')
                reenter_message = reenter_message.lower()

                if reenter_message == '3' or reenter_message == 'quit':
                    print('\n******************** T H A N K  Y O U **********************')
                    quit(0)
                elif reenter_message == '2' or reenter_message == 're-enter':
                    print()
                    display_rules()
                    get_message()
                    break
                elif reenter_message == '1' or reenter_message == 'encode':
                    print('\n************************************************************')
                    print('\nOkay, your message will be encoded.\nThis might take a few moments. Please wait....')
                    break
                else:
                    print('\n************************************************************')
                    print('Invalid Response. Press 1, 2 or 3.\n')
        else:
            print('\n******************* MESSAGE TO BE ENCODED ******************\n')
            print(''.join(valid_message))
            print('\n********************** ENCODING MESSAGE ********************')
            print('\nJust a few moments....')

        return ''.join(valid_message).lower()


def encode_message(path_script, source_letter_path, message):
    """
    Copies the required alphabets to a folder named Encoded_message_output according to message,
    then it encodes the same with numbers and renames the file.

    Also renames the destination folder to new name if aleady folder with same name exists.

    :param:
        (str) path_script - Path from where the script is originally run
    :param:
        (str) source_letter_path - Path of the alphabets folder
    :param:
        (str) message - The message to be encoded
    """

    start_time = time.time()

    # Creating output folder path name
    if os.name == 'nt':
        destination_path = path_script + '\\Encoded_message_output'
    else:
        destination_path = path_script + '/Encoded_message_output'

    # Creating output folder and changing name if already some folder is present with same name
    count = 0
    while True:
        if os.path.exists(destination_path):
            destination_path = destination_path + str(count)
            count += 1
        else:
            try:
                os.makedirs(destination_path)
            except:
                print('\nCould not make output folder in Location: ', destination_path)
            finally:
                break

    # Reading alphabet files from alphabet directory
    source_alphabet_name = os.listdir(source_letter_path)
    source_alphabet_name.sort()

    # Deleting hidden file-names of system starting with dot (.)
    for index, file in enumerate(source_alphabet_name):
        if file.startswith('.'):
            del source_alphabet_name[index]

    # Creating list of letters to find index of alphabets later
    alphabets = list('abcdefghijklmnopqrstuvwxyz. ')

    # Copying and encoding the the pictures by letters contained in message
    for letter in message:

        # Finding the alphabet name according to letter in message
        letter_name = source_alphabet_name[alphabets.index(letter)]

        # Copying the files in destination folder
        os.chdir(source_letter_path)
        shutil.copy(letter_name, destination_path)

    # Changing back to initial directory
    os.chdir(path_script)

    print('\nMessage has been encoded successfully.\nOutput Folder: ', destination_path)
    print('\nThis took about {} seconds'.format(time.time() - start_time))


def main():
    while True:
        print('************************************************************')
        print('********************** W E L C O M E ***********************')

        path_script, source_letter_path = check_dependencies()
        display_rules()
        message = get_message()
        encode_message(path_script, source_letter_path, message)

        # Checking whether user wants to encode some other message
        while True:
            print('\n************************************************************')
            restart = input("Do you want to encode some other secret message? Type 'yes' or 'no'\n")
            restart = restart.lower()

            if restart == 'yes' or restart == 'y' or restart == '1':
                restart = 'yes'
                break
            elif restart == 'no' or restart == 'n' or restart == '2':
                restart = 'no'
                break
            else:
                print("\nInvalid Input. Type yes or no.")

        # Quitting if user doesn't want to restart, else restarting
        if restart == 'no':
            print('\nQuitting....')
            print('******************** T H A N K  Y O U **********************')
            quit(0)
        else:
            print('\n'*get_terminal_size().lines)
            main()


if __name__ == '__main__':
    main()
