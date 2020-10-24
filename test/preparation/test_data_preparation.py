from src.preparation.data_preparation import *
import unittest


class DataPreparationTest(unittest.TestCase):

    def test_tokenize(self):
        sentence = "The official home of the Python Programming Language."
        tokens = tokenize(sentence)
        self.assertEqual(tokens,
                         ['The', 'official', 'home', 'of', 'the', 'Python', 'Programming', 'Language', '.'])
    #
    #
    # def test_is_stop_word(self):
    #     self.assertTrue(is_stopword("il"))
    #     self.assertTrue(is_stopword("étonné"))
    #     self.assertFalse(is_stopword("Samir"))
    #
    #
    # def test_stem_words(self):
    #     text = "maladive vie continuant faire ceux  continuité maistre travailler"
    #     self.assertEqual(stem_words(tokenize(text)),
    #                  ['malad', 'vi', 'continu', 'fair', 'ceux', 'continu', 'maistr', 'travaill'])
    #
    #
    # def test_remove_special_character(self):
    #     text = "saluf 2  @  dd  === !! 46 mm/s"
    #     self.assertEqual(remove_spacial_characters(text),"saluf 2 dd 46 mm s")
