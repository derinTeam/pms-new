from user.models import Comment
from django.contrib import admin

# Register your models here.

@admin.register(Comment)
class ProjectsAdmin(admin.ModelAdmin):

    list_display = ["comment_author","comment_content"]
    list_display_links = ["comment_author"]
    search_fields = ["comment_author"]
    list_filter = ["comment_date"]

    class Meta:
        model = Comment