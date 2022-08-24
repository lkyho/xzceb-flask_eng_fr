import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        with self.assertRaises(TypeError):
            english_to_french() 

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        with self.assertRaises(TypeError):
            french_to_english() 
      
unittest.main()
