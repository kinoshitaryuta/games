from .models import Post
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(Post, BlogAdmin)


