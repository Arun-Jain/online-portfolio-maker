from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)

#User.profile = property(lambda u: UserProfile.object.get_or_create(user=u)[0])
	def __unicode__(self):
		return '%s' % (self.user)

	class Meta:
		db_table = 'at_user_profile'

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)		
