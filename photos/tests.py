import os
from django.test import TestCase
from django.test import Client

from django.contrib.auth import get_user_model
from django.conf import settings

from .models import Photo
from .forms import PhotoForm


from django.core.files.uploadedfile import SimpleUploadedFile

class PhotoTest(TestCase):

	def _login(self, username, password):
		return self.client.post(settings.LOGIN_URL, {
				'username': username,
				'password': password
			})

	def setUp(self):
		user_model = get_user_model()
		self.user1 = user_model.objects.create_user(
			username='test1',
			password='1'
		)
		self.client = Client()

	def test_save_photo_by_model(self):
		new_photo = Photo()
		new_photo.user = self.user1
		new_photo.image = os.path.join(settings.MEDIA_ROOT, 'lethita01.jpg')
		new_photo.description = ''
		
		self.assertIsNone(new_photo.pk)
		new_photo.save()
		self.assertIsNotNone(new_photo.pk)

		new_photo2 = Photo()
		new_photo2.image = os.path.join(settings.MEDIA_ROOT, 'lethita01.jpg')
		new_photo2.description = ''
		
		with self.assertRaises(ValueError):
			new_photo2.user = 'hannal'
			new_photo2.save()
		self.assertIsNone(new_photo2.pk)


	def test_save_photo_by_model_with_form(self):
		form = PhotoForm(data={
			'image': os.path.join(settings.MEDIA_ROOT, 'lethita01.jpg'),
			'description': 'asdf'	
		})
		validation_result = form.is_valid()
		self.assertFalse(validation_result)

		with open(os.path.join(settings.MEDIA_ROOT, 'lethita01.jpg'), 'rb') as fp:
			form = PhotoForm(
			{
				'description': 'asdf'
			}, 
			{
				'image': SimpleUploadedFile(fp.name, fp.read()),
			})

		validation_result = form.is_valid()
		self.assertTrue(validation_result)
		new_photo = form.save(commit=False)
		new_photo.user = self.user1
		new_photo.save()

		self.assertIsNotNone(new_photo.pk)

	def test_view_get_create_photo(self):
		url = '/photos/create/'
		res = self.client.get(url, follow=True)
		self.assertEqual(res.status_code, 200)

		self.assertIsNotNone(res.context)
		self.assertIn('form', res.context)

	def test_view_post_create_photo(self):
		url = '/photos/create/'
		filepath = os.path.join(settings.MEDIA_ROOT, 'lethita01.jpg')

		with open(filepath, 'rb') as fp:
			res = self.client.post(url, {
				'image': fp,
				'description':'hi',
			}, follow=True)

		self.assertEqual(res.resolver_match.func.__name__, 'login')
		self._login('test1', '1')

		with open(filepath, 'rb') as fp:
			res = self.client.post(url, {
				'image': fp,
				'description':'hi',
			}, follow=True)

		self.assertEqual(res.resolver_match.func.__name__, 'view_photo')