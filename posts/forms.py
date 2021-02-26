from django.forms import ModelForm, forms
from posts.models import Post
from django_summernote.widgets import SummernoteWidget
from django import forms
from django.contrib.admin import widgets

EVENT=(
    ("10","キャリア"),
    ("20","スポーツ"),
    ("30","e-スポーツ"),
    ("40","コミニケーション"),

)
WORK_DETAIL=(
    ("10","セミナー"),
    ("20","朝活"),
    ("30","意見交換会"),
    ("40","名刺交換会"),
    ("50","学生向け"),
    ("60","その他"),

)
SPORT_DETAIL = (
    ("10", "誰でもOK"),
    ("20", "経験者のみ"),
    ("30", "観戦"),
    ("40", "その他"),

)
E_SPORT_DETAIL= (
    ("10", "FORTNITE"),
    ("20", "PUBG"),
    ("30", "荒野行動"),
    ("40", "APEX"),
    ("50", "スプラトゥーン"),
    ("60", "大乱闘スマッシュブラザーズ"),
    ("70", "鉄拳"),
    ("80", "ストリートファイター"),
    ("90", "リーグオブレジェンド"),
    ("100", "ウイニングイレブン"),
    ("110", "パズル＆ドラゴンズ"),
    ("120", "ぷよぷよ"),
    ("130", "その他"),

)
HOBBY_DETAIL = (
    ("10", "読書会"),
    ("20", "飲み会"),
    ("30", "カフェ会"),
    ("40", "もくもく会"),
    ("50", "その他"),

)
TYPE = (
    ("10", "オンライン"),
    ("20", "オフライン"),

)


class PostCreateForm(ModelForm):
    event_type = forms.ChoiceField(choices=EVENT,widget=forms.RadioSelect,required=True)
    work_detail=forms.ChoiceField(choices=WORK_DETAIL,widget=forms.RadioSelect,required=False)
    sport_detail=forms.ChoiceField(choices=SPORT_DETAIL,widget=forms.RadioSelect,required=False)
    e_sport_detail=forms.ChoiceField(choices=E_SPORT_DETAIL,widget=forms.RadioSelect,required=False)
    hobby_detail=forms.ChoiceField(choices=HOBBY_DETAIL,widget=forms.RadioSelect,required=False)
    holding_method = forms.ChoiceField(choices=TYPE,widget=forms.RadioSelect,required=True)
    class Meta:
        model=Post
        fields=[
             'event_type','work_detail','sport_detail','e_sport_detail','hobby_detail','holding_method','title','text',
        ]
        widgets = {
            'text': SummernoteWidget(),

        }