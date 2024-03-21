import unittest
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
# import scrapping_stats.get_all_box_score_links as get_all_box_score_links_var

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        pass
        # self.sample_html = '<html><head></head><body><a href="/boxscores/example.html">Example Link</a></body></html>'
        # self.mock_response = MagicMock()
        # self.mock_response.content = self.sample_html

    # @patch('main.requests.get')
    # def test_get_page(self, mock_get):
    #     mock_get.return_value = self.mock_response
    #     result = get_all_box_score_links_var.get_page('https://example.com')
    #     self.assertIsInstance(result, BeautifulSoup)
    #
    # def test_get_box_score_links(self):
    #     sample_page = BeautifulSoup(self.sample_html, 'html.parser')
    #     result = get_all_box_score_links_var.get_box_score_links(sample_page)
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result), 1)
    #     self.assertEqual(result[0], 'https://www.basketball-reference.com/boxscores/example.html')
    #
    # @patch('main.get_page')
    # def test_all_box_score_links_2024_games(self, mock_get_page):
    #     mock_get_page.side_effect = [
    #         BeautifulSoup('<html></html>', 'html.parser'),
    #         BeautifulSoup('<html></html>', 'html.parser'),
    #         BeautifulSoup('<html></html>', 'html.parser'),
    #         BeautifulSoup('<html></html>', 'html.parser'),
    #         BeautifulSoup('<html></html>', 'html.parser')
    #     ]
    #     result = get_all_box_score_links_var.all_box_score_links_2024_games()
    #     self.assertIsInstance(result, list)
    #     self.assertGreater(len(result), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
