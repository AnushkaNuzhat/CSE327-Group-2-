from django.test import SimpleTestCase
from django.urls import reverse, resolve
from health_advisor.views import *


class TestUrls(SimpleTestCase):

    def test_advisor_post_create_view_url_is_resolved(self):
        url = reverse('advisor-post-create')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, advisor_post_create_view)

    def test_advisor_home_view_url_is_resolved(self):
        url = reverse('advisor-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, advisor_home_view)

    def test_advisor_post_detail_view_url_is_resolved(self):
        url = reverse('advisor-post-detail', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, advisor_post_detail_view)

    def test_advisor_post_update_view_url_is_resolved(self):
        url = reverse('advisor-post-update', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, advisor_post_update_view)

    def test_advisor_post_delete_view_url_is_resolved(self):
        url = reverse('advisor-post-delete', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, advisor_post_delete_view)
