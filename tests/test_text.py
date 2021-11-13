from unittest import TestCase

from preprocessing.text import extract_vocabulary
import pandas as pd


class TestText(TestCase):

    def test_extract_vocabulary(self):
        data = {'Text': ['a', 'b', 'c', 'd', 'a', 'b']}
        self.assertEqual(extract_vocabulary(pd.DataFrame(data)), ({'a', 'b', 'c', 'd'}, 6))
