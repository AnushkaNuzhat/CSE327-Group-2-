from django.test import SimpleTestCase
from patient_community.views import *


class TestForms(SimpleTestCase):

    # Test the form for creating a new post with valid data
    def test_AddEditPostForm_from_valid_data(self):
        form = AddEditPostForm(data={
            'title': "test_title",
            'content': "test_content"
        })
        self.assertTrue(form.is_valid())

    # Test the form for crating a post with invalid data
    def test_AddEditPostForm_form_no_data(self):
        form = AddEditPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
