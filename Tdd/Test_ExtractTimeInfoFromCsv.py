import csv
import os
import unittest


from CsvTimeInfoExtractor import extractTargetTimingsFromsCsv as cse
from CsvTimeInfoExtractor import IP_FILENAME,OP_FILENAME

class targettimings(unittest.TestCase):
    csv_data = []

    def setUp(self):
        self.csv_data = cse.intialize_csv_data()

    def test_data_is_read(self):
        self.assertNotEqual(len(self.csv_data),0)

    def test_file_is_written(self):
        cse.remove_file_if_it_exists()
        self.assertFalse(os.path.exists(OP_FILENAME))
        cse.write_csv_to_file()
        self.assertTrue(os.path.exists(OP_FILENAME))
        self.assertTrue(os.stat(OP_FILENAME).st_size > 0)

if __name__ == '__main__':
    unittest.main()