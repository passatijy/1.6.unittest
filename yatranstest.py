import unittest
from unittest.mock import patch
import yatranslate

class YaTests(unittest.TestCase):
	def setUp(self):
		self.API_KEY = input('Please enter Ya.Tranlsate API key: ')
		self.result = yatranslate.translate_some(self.API_KEY, 
			'hello','en','ru')

	def test_translate_some_first(self):
		with self.assertRaises(IndexError):
			self.assertNotEqual(self.result[0], 403, 'Forbidden, probably API key wrong')

	def test_translate_some(self):
		with self.assertRaises(IndexError):
			self.assertEqual(self.result[1], 'привет')
			self.assertEqual(self.result[0], 200)


if __name__ == '__main__':
	unittest.main()
