from unittest import TestCase

from preprocessing.text import extract_vocabulary
import pandas as pd


class Test(TestCase)

    def test_extract_vocabulary(self):
        data = {'Text':['a', 'b', 'c', 'd']}
        print(extract_vocabulary(data))
