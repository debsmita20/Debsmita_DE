import unittest
import csv
import json

class TestCSVJSON(unittest.TestCase):
    def test_csv_columns(self):
        with open('profiles1.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(len(header), 12)

    def test_csv_rows(self):
        with open('profiles1.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader)
            self.assertGreaterEqual(row_count, 900)

    def test_json_properties(self):
        with open('data.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                self.assertTrue('Givenname' in item)
                self.assertTrue('Surname' in item)
                # Add assertions for other properties

    def test_json_lines(self):
        with open('data.json', 'r') as jsonfile:
            line_count = sum(1 for line in jsonfile)
            self.assertGreaterEqual(line_count, 900)

if __name__ == '__main__':
    unittest.main()
