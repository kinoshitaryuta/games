from .models import Post,EventScheduleApex,EventScheduleMonhan,EventScheduleFortnite,EventScheduleGuraburu
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post, BlogAdmin)
admin.site.register(EventScheduleApex, BlogAdmin)
admin.site.register(EventScheduleGuraburu, BlogAdmin)
admin.site.register(EventScheduleFortnite, BlogAdmin)
admin.site.register(EventScheduleMonhan, BlogAdmin)


