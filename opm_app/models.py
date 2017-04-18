from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import os
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	brother_name = models.CharField(max_length=100)
	name = models.CharField(max_length=100, null=True ,blank=True,default=None)
	branch = models.CharField(max_length = 500)
	phno  = models.CharField(max_length = 10)
	url = models.CharField(max_length=1000)
	HighSchool = models.CharField(max_length =500)
	HighSchool_Marks = models.CharField(max_length = 7)
	Intermediate_School = models.CharField(max_length=500)
	Intermediate_Marks = models.CharField(max_length=7)
	BTech_Marks = models.CharField(max_length = 100)
	skills_Set = models.CharField(max_length = 10000)
	Project_Title = models.CharField(max_length = 1000)
	Project_Desc = models.CharField(max_length  = 10000)
	Experience_Desc = models.CharField(max_length = 10000)
	Achieve_Desc = models.CharField(max_length = 10000)
	interest_Desc = models.CharField(max_length = 10000)
	Self_Description = models.CharField(max_length = 10000)
	image = models.FileField(blank= True, null=True)
#User.profile = property(lambda u: UserProfile.object.get_or_create(user=u)[0])
	def __unicode__(self):
		return '%s' % (self.user)

	class Meta:
		db_table = 'at_user_profile'

	def filename(self):
		return os.path.basename(self.image.name)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)	






