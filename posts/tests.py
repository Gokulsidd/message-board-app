from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='sample text')
        Post.objects.create(text='second text')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        post2 = Post.objects.get(id=2)
        expected_object_name = f'{post.text}'
        expected_object_name2 = f'{post2.text}'
        self.assertEqual(expected_object_name, 'sample text')  
        self.assertEqual(expected_object_name2, 'second text')  


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='another text')

    def test_viewUrl_exits_at_properLocation(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)     

    def test_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')         