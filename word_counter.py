import glob
import os
from collections import Counter

class Word_counter:
    '''Class to deal with extracting word occurrence from each .txt file of a specified directory
       foldername: name or path to the directory'''
    def __init__(self, foldername):
        self.foldername =          foldername
        self.filenamelist =        []
        self.filetextlist =        []
        #A list of Counter objects giving the frequency of occurrence of each word in a given file
        self.filefrequency =       []
        #A Counter object giving the frequency of occurrence of each word for the whole directory
        self.totalfrequencycount = Counter()

    def separate(self):
        'Open each text file in the folder, store its name and store its text as a list where each element is a single word'
        self.pathlist = glob.glob(os.path.join(self.foldername, '*.txt'))
        if len (self.pathlist) == 0:
            raise IndexError('No files found, either the path was incorrect or the directory has no .txt files.') 
        for filename in self.pathlist:
            self.filenamelist.append(filename.split('\\')[-1])

            with open(filename) as rawtext:
                filetext=[]
                for line in rawtext:
                    #Formating to remove punctuation and other unwanted characters so all words can be counted properly
                    linestring =       line.replace('\t', ' ').replace('\n', '')
                    linelist =         linestring.split()
                    formatedlinelist = [word.strip(',.:;?').lower() for word in linelist]
                    filetext.extend(formatedlinelist)

            self.filetextlist.append(filetext)

    def count_frequency(self):
        'Count the frequency of occurrence for each word for each file and find the total frequency of occurrence in the folder'
        for wordlist in self.filetextlist:
            self.filefrequency.append(Counter(wordlist))
            self.totalfrequencycount += self.filefrequency[-1]


if __name__ == '__main__':
    test_counter=Word_counter('test_data')
    test_counter.separate()
    test_counter.count_frequency()
    print(test_counter.filefrequency)
    print(test_counter.totalfrequencycount)