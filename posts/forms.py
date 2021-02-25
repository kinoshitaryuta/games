from django.forms import ModelForm, forms
from posts.models import Post
from django_summernote.widgets import SummernoteWidget


class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
             'event_type','work_detail','sport_detail','e_sport_detail','hobby_detail','holding_method','title','text',
        ]
        widgets = {
            'text': SummernoteWidget(),

        }