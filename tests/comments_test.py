import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(body = 'That is Wonderful ')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.save_comment = Comment (body=' ')