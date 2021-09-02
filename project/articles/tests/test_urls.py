from django.test import SimpleTestCase
from django.urls import reverse, resolve
from articles.views import *


class TestUrls(SimpleTestCase):

    def test_article_home_view_url_is_resolved(self):
        url = reverse('article-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, article_home_view)

    def test_post_article_view_url_is_resolved(self):
        url = reverse('post-article')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, post_article_view)

    def test_article_details_view_url_is_resolved(self):
        url = reverse('article-details', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, article_details_view)

    def test_edit_article_view_url_is_resolved(self):
        url = reverse('edit-article', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, edit_article_view)

    def test_delete_article_view_url_is_resolved(self):
        url = reverse('delete-article', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, delete_article_view)

    def test_users_articles_view_url_is_resolved(self):
        url = reverse('users-articles', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, users_articles_view)

    def test_category_articles_view_url_is_resolved(self):
        url = reverse('category-articles', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, category_articles_view)
