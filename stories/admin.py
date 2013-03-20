from django.contrib import admin

from stories.models import Story

class StoryAdmin(admin.ModelAdmin):
	list_display = ("__unicode__", "domain", "moderator", "created_at", "updated_at")
	list_filter = ("created_at", "updated_at")
	search_fields = ("title", "moderator__username", "moderator__first_name", "moderator__last_name")

	readonly_fields = ("created_at", "updated_at")

	#Documentation: https://docs.djangoproject.com/en/1.5/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
	fieldsets = (
		("Story", {
			"fields": ("title", "url", "points")
		}),
		("Moderator", {
			"classes": ("collapse",),
			"fields": ("moderator",)
		}),
		("Change History", {
			"classes": ("collapse",),
			"fields": ("created_at", "updated_at")
		}),
	)
	

admin.site.register(Story, StoryAdmin)