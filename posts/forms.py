import bootstrap_datepicker_plus as datetimepicker
from django.forms import ModelForm, forms
from posts.models import Post,Report,MonhanQuest
from django_summernote.widgets import SummernoteWidget
from django import forms





class PostCreateForm(ModelForm):
    class Meta:
        model=Post
        fields=[
            'e_sport_detail','holding_method','title','text',
            'event_date','start_application_date','finish_application_date','sns_url','link_url','start_time','end_time',

        ]
        widgets = {
            'text': SummernoteWidget(),
            'event_type': forms.RadioSelect(),
            'e_sport_detail': forms.RadioSelect(),
            'holding_method': forms.RadioSelect(),
            'event_date': datetimepicker.DatePickerInput(format='%Y-%m-%d',options={'locale': 'ja','dayViewHeaderFormat': 'YYYY年 MMMM',}),
            'start_application_date': datetimepicker.DatePickerInput(format='%Y-%m-%d',options={'locale': 'ja','dayViewHeaderFormat': 'YYYY年 MMMM',}).start_of('期間'),
            'finish_application_date': datetimepicker.DatePickerInput(format='%Y-%m-%d',options={'locale': 'ja','dayViewHeaderFormat': 'YYYY年 MMMM',}).end_of('期間'),
        }

class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','text','event_date','start_application_date','finish_application_date','holding_method','sns_url','link_url',
            'start_time','end_time',
        ]

        widgets = {
            'text': SummernoteWidget(),
            'holding_method': forms.RadioSelect(),
            'event_date': datetimepicker.DatePickerInput(format='%Y-%m-%d', options={'locale': 'ja', 'dayViewHeaderFormat': 'YYYY年 MMMM', }),
            'start_application_date': datetimepicker.DatePickerInput(format='%Y-%m-%d', options={'locale': 'ja','dayViewHeaderFormat': 'YYYY年 MMMM', }).start_of('期間'),
            'finish_application_date': datetimepicker.DatePickerInput(format='%Y-%m-%d', options={'locale': 'ja','dayViewHeaderFormat': 'YYYY年 MMMM', }).end_of('期間'),

        }



class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = [
            'report_us','message'
        ]

class MonhanForm(ModelForm):
    class Meta:
        model = MonhanQuest
        fields = [
            'text','quest_name','hunter_name','room_id','password'
        ]