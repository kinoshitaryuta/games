from django.db import models
from accounts.models import User
from django.utils import timezone



class Tag(models.Model):
    EVENT=(
        ("10","キャリア"),
        ("20","スポーツ"),
        ("30","e-スポーツ"),
        ("40","コミニケーション"),

    )
    TYPE = (
        ("10", "オンライン"),
        ("20", "オフライン"),

    )
    class Detail(models.Model):
        WORK_DETAIL=(
            ("10","セミナー"),
            ("20","意見交換会"),
            ("30","名刺交換会"),
            ("40","学生向け"),
            ("50","その他"),

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
            ("30", "APEX"),
            ("40", "MINECRAFT"),
            ("50", "League of Legends"),
            ("60", "その他"),

        )
        HOBBY_DETAIL = (
            ("10", "読書会"),
            ("20", "懇親会"),
            ("30", "朝活"),
            ("40", "その他"),

        )




class Post(models.Model):
    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=5000, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=100,choices=Tag.EVENT, blank=False, null=False)
    work_detail = models.CharField(max_length=100,choices=Tag.Detail.WORK_DETAIL,blank=True, null=False)
    sport_detail = models.CharField(max_length=100,choices=Tag.Detail.SPORT_DETAIL,blank=True, null=False)
    e_sport_detail = models.CharField(max_length=100,choices=Tag.Detail.E_SPORT_DETAIL,blank=True, null=False)
    hobby_detail = models.CharField(max_length=100,choices=Tag.Detail.HOBBY_DETAIL, blank=True, null=False)
    holding_method = models.CharField(max_length=100,choices=Tag.TYPE, blank=False, null=False)
    event_date= models.DateField(blank=True,null=True)
    start_application_date= models.DateField(blank=True,null=True)
    finish_application_date= models.DateField(blank=True,null=True)


    def __str__(self):
            return str(self.title)

    def get_absolute_url(self):
        return f"/posts/{self.id}"



