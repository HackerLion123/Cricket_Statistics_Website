from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
	#ip_address =
	content_type = models.ForeignKey(ContentType)
	object_id = models.PostiveIntegerField()
	object_name = models.CharField(max_length=120,primary_key=True)
	content_object = GenericForeignKey('content_type','object_id','object_name')
	
	player = models.ForeignKey(Player)
	team = models.ForeignKey(Team)
