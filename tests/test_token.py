from unittest import TestCase

from preprocessing.text import tokenize
from preprocessing.token import lemma, stem


class Test(TestCase):
    def test_lemma(self):
        input = ['21-jähriger', 'fällt', 'wohl', 'bis', 'saisonende', 'aus', '.', 'wien', '–', 'rapid', 'muss', 'wohl',
                 'bis', 'saisonende', 'auf', 'offensivspieler', 'thomas', 'murg', 'verzichten', '.']

        expected = ['21-jähriger', 'fällen', 'wohl', 'bis', 'saisonende', 'aus', 'wien', 'rapid', 'muss', 'wohl', 'bis',
                    'saisonende', 'auf', 'offensivspieler', 'thomas', 'murg', 'verzichten']

        result = lemma(input)
        self.assertEqual(result, expected)

    def test_stem(self):
        input = ['21-jähriger', 'fällt', 'wohl', 'bis', 'saisonende', 'aus', '.', 'wien', '–', 'rapid', 'muss', 'wohl',
                 'bis', 'saisonende', 'auf', 'offensivspieler', 'thomas', 'murg', 'verzichten', '.']
        expected = ['21-jahrig', 'fallt', 'wohl', 'bis', 'saison', 'aus', 'wien', 'rapid', 'muss', 'wohl', 'bis',
                    'saison', 'auf', 'offensivspiel', 'thomas', 'murg', 'verzicht']

        result = stem(input)

        self.assertEqual(result, expected)
