import unittest
import documents

class DocuTests(unittest.TestCase):
	def setUp(self):
		self.documents = [
			{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
			{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
			{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
			]
		self.directories = {
			'1': ['2207 876234', '11-2'],
			'2': ['10006'],
			'3': []
			}

	def test_find(self):
		self.assertEqual(search_by_docnumber(self.documents))

	def test_list(self):
		pass

	def test_add(self):
		pass


if __name__ == '__main__':
	unittest.main()