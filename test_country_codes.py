import unittest
from country_codes import get_country_code


class TestCountryCodes(unittest.TestCase):
	def test_return_codes(self):
		country_name = 'Armenia'
		result = get_country_code(country_name)
		self.assertEqual('am', result)

	def test_error_name(self):
		country_name = "HUB"
		result = get_country_code(country_name)
		self.assertEqual(None, result)


if __name__ == '__main__':
        unittest.main()