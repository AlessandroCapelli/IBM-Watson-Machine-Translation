import unittest

from translator import englishtofrench
from translator import englishtogerman

class TestEnglishToFrench(unittest.TestCase):
    def test_null(self):
        self.assertEqual(englishtofrench(None), "")

    def test_empty(self):
        self.assertEqual(englishtofrench(""), "")

    def test_sentence1(self):
        self.assertEqual(englishtofrench("Hello everyone"), "Bonjour tout le monde")

    def test_sentence2(self):
        self.assertEqual(englishtofrench("How old are you?"), "Quel âge as-tu?")

class TestEnglishToGerman(unittest.TestCase):
    def test_null(self):
        self.assertEqual(englishtogerman(None), "")

    def test_empty(self):
        self.assertEqual(englishtogerman(""), "")

    def test_sentence1(self):
        self.assertEqual(englishtogerman("Hello everyone"), "Hallo alle")

    def test_sentence2(self):
        self.assertEqual(englishtogerman("How old are you?"), "Wie alt sind Sie?")

unittest.main()
