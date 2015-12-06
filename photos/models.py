from django.db import models

from django.conf import settings


class Photo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	image = models.ImageField(upload_to='%Y/%m/%d/')
	description = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
