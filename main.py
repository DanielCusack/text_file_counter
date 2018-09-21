import sys
from report_generator import *
from word_counter import *

while True:
    folderpath = input('Please enter the directory you want to check: ')
    try:
        word_counter = Word_counter(folderpath)
        word_counter.separate()
        word_counter.count_frequency()
        break
    except IndexError:
        print('An error occurred. Either the path was incorrect or the directory was void of .txt files.')
        keep_going = input('Would you like to quit y/n? ')
        if keep_going.lower() == 'y':
            sys.exit()

while True:
    archivepath = input('Please enter the directory you want to archive the report in: ')
    report = Report(archivepath, folderpath, word_counter.filenamelist,
                    word_counter.filefrequency, word_counter.totalfrequencycount)
    if report.check_archive_exists():
        report.create_report()
        break
    else:
        create_directory = input('Directory does not exist. Create it y/n? ')
        if create_directory.lower() == 'y':
            report.create_archive_folder()
            report.create_report()
            break
        else:
            keep_going = input('Would you like to quit y/n? ')
            if keep_going.lower() == 'y':
                sys.exit()
    