from unittest import TestCase
from unittest.mock import patch
from main import Calculator

class TestCalculator(TestCase):

    def setUp(self):
        self.calc = Calculator()

    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)

    def test_sum2(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)