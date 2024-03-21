import unittest
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
# from scrapping_stats import get_box_scores
import os
from datetime import datetime


class TestGettingBoxScoresFunctions(unittest.TestCase):

    def setUp(self):
        pass
    #     path = 'sample_box_score.html'
    #     if os.path.exists(path):
    #         with open(path, 'r',encoding='utf-8') as file:
    #             html_content = file.read()
    #     else:
    #         print(f"The file '{path}' does not exist.")
    #     self.sample_html = html_content
    #     self.mock_response = MagicMock()
    #     self.mock_response.content = self.sample_html
    #
    # @patch('main.requests.get')
    # def test_get_html_page(self, mock_get):
    #     mock_get.return_value = self.mock_response
    #     result = get_box_scores.get_html_page('https://www.basketball-reference.com/boxscores/202402140UTA.html')
    #     self.assertIsInstance(result, BeautifulSoup)
    #
    # @patch('main.requests.get')
    # def test_get_html_pages(self, mock_get):
    #     mock_get.return_value = self.mock_response
    #     result = get_box_scores_var.get_html_pages(['https://example.com'])
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result), 1)
    #     self.assertIsInstance(result[0], BeautifulSoup)
    #
    # # Add more test methods for other functions...

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
