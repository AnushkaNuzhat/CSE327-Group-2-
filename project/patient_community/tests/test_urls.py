from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_community.views import *


class TestUrls(SimpleTestCase):

    # Test the url for the community home page
    def test_community_home_view_url_is_resolved(self):
        url = reverse('community-home')
        self.assertEquals(resolve(url).func, community_home_view) # Hard coded

    # Test the url for the community post create page
    def test_community_post_create_view_url_is_resolved(self):
        url = reverse('community-post-create')
        self.assertEquals(resolve(url).func, community_post_create_view)

    # Test the url for the community post detail page
    def test_community_post_detail_view_url_is_resolved(self):
        url = reverse('community-post-detail', args=[1])
        self.assertEquals(resolve(url).func, community_post_detail_view)

    # Test the url for the community post update page
    def test_community_post_update_view_url_is_resolved(self):
        url = reverse('community-post-update', args=[1])
        self.assertEquals(resolve(url).func, community_post_update_view)

    # Test the url for the community post delete page
    def test_community_post_delete_view_url_is_resolved(self):
        url = reverse('community-post-delete', args=[1])
        self.assertEquals(resolve(url).func, community_post_delete_view)
