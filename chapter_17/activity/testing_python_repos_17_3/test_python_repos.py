import requests

import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # Make the API call once for all tests
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.response = requests.get(self.url)
        self.response_dict = self.response.json()

    def test_status_code(self):
        # Assert the API call was successful
        self.assertEqual(self.response.status_code, 200)

    def test_number_of_items(self):
        # For example, we expect at least 30 items
        self.assertGreaterEqual(len(self.response_dict['items']), 30)
        
    def test_id_instance(self):
        # You could check other things, e.g., all IDs are integers
        for submission_id in self.response_dict['items'][:30]:
            self.assertIsInstance(submission_id['id'], int)
    
    def test_stargaze(self):
        items = self.response_dict.get('items', [])
        most_starred = items[0].get("stargazers_count", 0)
        second_most_starred = items[1].get("stargazers_count", 0)
        self.assertGreater(most_starred, second_most_starred)

if __name__ == '__main__':
    unittest.main()