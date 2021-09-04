from unittest import TestCase

from patient_community.views import *
from user_control.models import UserModel


class CommunityPostModelTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = UserModel.objects.create(
            email='test1@example.com', name='name', password='asdf123ASDF')

    def test_content(self):
        # Creating a community post object
        post = CommunityPostModel.objects.create(author=self.user, title='test_title', content='test_content',
                                                 slug='aa', totalViewCount=3)
        expected_object_author = post.author.email
        expected_object_title = post.title
        expected_object_content = post.content
        expected_object_slug = post.slug
        expected_object_totalViewCount = post.totalViewCount
        # Checking if the author is the same as the user by checking the email of the author and the user
        self.assertEquals(expected_object_author,
                          'test1@example.com')  # hard coded email
        self.assertEquals(expected_object_title, 'test_title')
        self.assertEquals(expected_object_content, 'test_content')
        self.assertEquals(expected_object_slug, 'aa')
        self.assertEquals(expected_object_totalViewCount, 3)

    # Deleting the previously created user object
    def tearDown(self):
        self.user.delete()
