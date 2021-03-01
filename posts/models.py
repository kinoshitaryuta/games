from django.db import models
from accounts.models import User
from django.utils import timezone



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




class Post(models.Model):
    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=5000, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=100,choices=EVENT, blank=False, null=False)
    work_detail = models.CharField(max_length=100,choices=WORK_DETAIL,blank=True, null=False)
    sport_detail = models.CharField(max_length=100,choices=SPORT_DETAIL,blank=True, null=False)
    e_sport_detail = models.CharField(max_length=100,choices=E_SPORT_DETAIL,blank=True, null=False)
    hobby_detail = models.CharField(max_length=100,choices=HOBBY_DETAIL, blank=True, null=False)
    holding_method = models.CharField(max_length=100,choices=TYPE, blank=False, null=False)
    event_date= models.DateField(blank=True,null=True)
    start_application_date= models.DateField(blank=True,null=True)
    finish_application_date= models.DateField(blank=True,null=True)


    def __str__(self):
            return str(self.title)