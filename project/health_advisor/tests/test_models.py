from unittest import TestCase

from health_advisor.views import *
from user_control.models import UserModel


class AdviceModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='test@example.com', name='name', password='asdf123ASDF', is_doctor=True)

    def test_content(self):
        post = AdviceModel.objects.create(author=self.user, title='test_title', content='test_content',
                                          slug='aa', totalViewCount=3)
        expected_object_author = f'{post.author}'
        expected_object_title = f'{post.title}'
        expected_object_content = f'{post.content}'
        expected_object_slug = f'{post.slug}'
        expected_object_totalViewCount = f'{post.totalViewCount}'
        self.assertEquals(expected_object_author, self.user.email)
        self.assertEquals(expected_object_title, 'test_title')
        self.assertEquals(expected_object_content, 'test_content')
        self.assertEquals(expected_object_slug, 'aa')
        self.assertEquals(expected_object_totalViewCount, '3')

    def tearDown(self):
        self.user.delete()
