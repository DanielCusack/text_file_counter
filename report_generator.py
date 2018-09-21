import os
import time
from collections import Counter

class Report:
    '''Class to deal with creating a report of the most frequently occuring words in a folder.
       archivefoldername:   the name of the archive directory
       countedfoldername:   the name of the folder in which word counting was done
       filenamelist:        a list of the filenames that were counted
       filefrequency:       list of Counter objects containing the word and frequency of
                            occurrence for each file
       totalfrequencycount: Counter object containing total word and frequency of occurrence
                            for the directory
       topwordnumber:       integer representing the top number of words to report'''
    def __init__(self, archivefoldername, countedfoldername, filenamelist, filefrequency, totalfrequencycount, topwordnumber=10):
        self.archivefoldername = archivefoldername
        self.countedfoldername = countedfoldername
        self.filenamelist =      filenamelist
        self.topwordnumber =     int(topwordnumber)
        self.topnfilelist =      []
        #Find the n most frequently used words per file 
        for freqcounter in filefrequency:
            self.topnfilelist.append(freqcounter.most_common(self.topwordnumber))
        #Find the n most frequently used words for the whole directory 
        self.foldertopn=totalfrequencycount.most_common(self.topwordnumber)
    
    def check_archive_exists(self):
        'Check if archive folder exists'
        return os.path.isdir(self.archivefoldername)

    def create_archive_folder(self):
        'Check if archive folder exists and, if not, create it'
        if not self.check_archive_exists():
            os.makedirs(self.archivefoldername)
    
    def create_report(self):
        'Create a .txt report in the archive folder for the top words in each file and the directory as a whole'
        self.report=open(self.archivefoldername 
                         + '/' + self.countedfoldername + '_report_{0}.txt'.format(time.strftime("%Y-%m-%d_%H-%M-%S")),'w')
        
        #Write report introduction
        opener = 'This is a report on the frequency of word use of text files in the folder '
        self.report.write(opener + '"{0}":\n\n'.format(self.countedfoldername))

        #Write total word occurrence across all files
        self.report.write('Top {0} most frequently used words across all files: \n\n'.format(self.topwordnumber))
        for topn in self.foldertopn:
            self.report.write('{0}: {1}\n'.format(topn[0], topn[1]))

        #Then write word occurrence for each file
        for i in range(len(self.filenamelist)):
            self.report.write('\nFor file {0}:\n'.format(self.filenamelist[i]))
            for topn in self.topnfilelist[i]:
                self.report.write('{0}: {1}\n'.format(topn[0], topn[1]))
        self.report.close()