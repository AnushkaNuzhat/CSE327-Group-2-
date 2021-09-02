from unittest import TestCase

from articles.models import *
from user_control.models import UserModel


class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='test3@example.com', name='name', password='asdf123ASDF', is_doctor=True)
        ArticleModel.objects.create(article_author=self.user, article_title='test_title', article_content='test_content')

    def test_content(self):
        post = ArticleModel.objects.get(id=1)
        expected_object_author = f'{post.article_author}'
        expected_object_title = f'{post.article_title}'
        expected_object_content = f'{post.article_content}'
        self.assertEquals(expected_object_author, self.user.email)
        self.assertEquals(expected_object_title, 'test_title')
        self.assertEquals(expected_object_content, 'test_content')
