from django.db import models
from accounts.models import User
from django.utils import timezone



class Tag(models.Model):
    TYPE= (
        ("10", "オンライン"),
        ("20", "オフライン"),

    )

    class Detail(models.Model):
        E_SPORT_DETAIL= (
            ("10", "FORTNITE"),
            ("20", "APEX"),
            ("30", "MONSTER HUNTER RISE"),
            ("40", "ポケットモンスター ソード&シールド"),
            ("50", "グランブルーファンタジー"),
        )




class Post(models.Model):

    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)
    e_sport_detail = models.CharField(max_length=100,choices=Tag.Detail.E_SPORT_DETAIL,blank=True, null=False)
    holding_method = models.CharField(max_length=100,choices=Tag.TYPE, blank=False, null=False)
    event_date= models.DateField(blank=True,null=True)
    start_application_date= models.DateField(blank=True,null=True)
    finish_application_date= models.DateField(blank=True,null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    address = models.CharField(max_length=150,blank=True, null=True)
    lat = models.DecimalField( max_digits=8, decimal_places=6,blank=True, null=True)
    lng = models.DecimalField( max_digits=9, decimal_places=6,blank=True, null=True)
    link_url=models.URLField(max_length=1000,blank=True,null=True)
    sns_url=models.URLField(max_length=1000,blank=True,null=True)


    def __str__(self):
            return str(self.title)

    def get_absolute_url(self):
        return f"/posts/{self.id}"



