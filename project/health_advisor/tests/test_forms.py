from django.test import SimpleTestCase
from health_advisor.views import *


class TestForms(SimpleTestCase):

    def test_AddEditPostForm_from_valid_data(self):
        form = AddEditPostForm(data={
            'title': "test title",
            'content': "test content",
        })
        self.assertTrue(form.is_valid())

    def test_AddEditPostForm_form_no_data(self):
        form = AddEditPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
