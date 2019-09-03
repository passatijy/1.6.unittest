import unittest
from unittest.mock import patch
import documents

class DocuTests(unittest.TestCase):
	def setUp(self):
		self.document = [
			{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
			{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
			{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
			]
		self.directories = {
			'1': ['2207 876234', '11-2'],
			'2': ['10006'],
			'3': []
			}
	@patch('builtins.input', return_value = '11-2')
	def test_find(self, mock_input):
			print(documents.search_by_docnumber(self.document))
			self.assertEqual(documents.search_by_docnumber(self.document), "Геннадий Покемонов")

	def test_list(self):
		pass

	def test_add(self):
		pass


if __name__ == '__main__':
	print('name:', __name__)
	unittest.main()