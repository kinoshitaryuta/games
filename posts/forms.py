from django.forms import ModelForm, forms
from posts.models import Post
from django_summernote.widgets import SummernoteWidget
from django import forms
from django.contrib.admin import widgets




class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
             'event_type','work_detail','sport_detail','e_sport_detail','hobby_detail','holding_method','title','text',
        ]
        widgets = {
            'text': SummernoteWidget(),
            'event_type': forms.RadioSelect(),
            'work_detail': forms.RadioSelect(),
            'sport_detail': forms.RadioSelect(),
            'e_sport_detail': forms.RadioSelect(),
            'hobby_detail': forms.RadioSelect(),
            'holding_method': forms.RadioSelect(),

        }