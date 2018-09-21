import unittest
from report_generator import *
from word_counter import *

class Test_word_counter(unittest.TestCase):
    def setUp(self):
        self.testwordcounter = Word_counter('test_data')
        self.testwordcounter.separate()
        self.testwordcounter.count_frequency()

    def test_separator(self):
        'Test that the separator method is functioning properly'

        #Check that IndexError is raised if the directory doesn't exist
        self.testseparate=Word_counter('a_folder_that_doesnt_exist')
        with self.assertRaises(IndexError):
            self.testseparate.separate()

        for filetext in self.testwordcounter.filetextlist:
            #Check that there are no empty spaces, punctuation or other unwanted characters in the file word list 
            self.assertNotIn('', filetext)
            for word in filetext:
                self.assertNotIn(',', word)
                self.assertNotIn('.', word)
                self.assertNotIn(';', word)
                self.assertNotIn(':', word)
                self.assertNotIn('?', word)
                self.assertNotIn('\n', word)
                self.assertNotIn('\t', word)

    def test_count_frequency(self):
        'Test that the count_frequency method has worked properly'

        #Check that all files have been included
        self.assertEqual(len(self.testwordcounter.filefrequency), len(self.testwordcounter.filenamelist))

        #Check that all words are counted in the total frequency count
        wordno=0
        for wordlist in self.testwordcounter.filetextlist:
            wordno+=len(wordlist)
        self.assertEqual(sum(self.testwordcounter.totalfrequencycount.values()), wordno)


class Test_report_generator(unittest.TestCase):
    def setUp(self):
        self.testwordcounter = Word_counter('test_data')
        self.testwordcounter.separate()
        self.testwordcounter.count_frequency()
        self.testreport=Report('Test_case_reports', 'test_data', self.testwordcounter.filenamelist, 
                               self.testwordcounter.filefrequency, self.testwordcounter.totalfrequencycount)
        self.testreport.create_archive_folder()
        self.testreport.create_report()

    def test_setUp(self):
        #Check that the list giving the top 10 most used words is only 10
        self.assertEqual(len(self.testreport.foldertopn), 10)

    def test_check_archive_exists(self):
        self.assertTrue(self.testreport.check_archive_exists())



if __name__ == '__main__':
    unittest.main()