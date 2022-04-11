import os
import unittest

from main import Ranking
from pathlib import Path


class TestRanking(unittest.TestCase):
    input_file = os.path.join(Path(os.path.dirname(__file__)), 'league.txt')

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(TestRanking.input_file), f"{TestRanking.input_file} does not exists")

    def test_file_readable(self):
        self.assertTrue(os.access(TestRanking.input_file, os.R_OK), f"{TestRanking.input_file} is not readable")

    def test_file_size(self):
        self.assertNotEqual(0, os.stat(TestRanking.input_file).st_size, "File is empty")

    def test_delimiters(self):
        with open(TestRanking.input_file, 'r') as data:
            rows = data.readlines()
            for row in rows:
                self.assertIn(",", row, "Wrong delimiter found instead of ',' ")
                get = row.strip().split(', ')
                for matches in get:
                    team = matches[0].strip().split(" ")
                    self.assertTrue(team[-1], isinstance(team[-1], int))
                    self.assertTrue(team[0], isinstance(team[0], str))


if __name__ == "__main__":
    unittest.main()
