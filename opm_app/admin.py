from django.contrib import admin
from .models import UserProfile
# Register your models here.
class admin_panel(admin.ModelAdmin):
	list_display = ['__unicode__']
	class Meta:
		model = UserProfile
admin.site.register(UserProfile, admin_panel)
