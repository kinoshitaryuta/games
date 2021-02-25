from django.db import models
from accounts.models import User
from django.utils import timezone



class Event(models.Model):
    EVENT=(
        ("10","キャリア"),
        ("20","スポーツ"),
        ("30","e-スポーツ"),
        ("40","コミニケーション"),

    )
class EventDetail(models.Model):
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

class HoldingMethod(models.Model):
    TYPE = (
        ("10", "オンライン"),
        ("20", "オフライン"),

    )


class Post(models.Model):
    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    event_type = models.CharField(max_length=30, choices=Event.EVENT)
    work_detail=models.CharField(max_length=30, choices=EventDetail.WORK_DETAIL)
    sport_detail=models.CharField(max_length=30, choices=EventDetail.SPORT_DETAIL)
    e_sport_detail=models.CharField(max_length=30, choices=EventDetail.E_SPORT_DETAIL)
    hobby_detail=models.CharField(max_length=30, choices=EventDetail.HOBBY_DETAIL)
    holding_method = models.CharField(max_length=30, choices=HoldingMethod.TYPE)
    text = models.TextField(max_length=5000,blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
