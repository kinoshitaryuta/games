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
            ("40", "グランブルーファンタジー"),
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
    lat = models.DecimalField(max_digits=8, decimal_places=6,blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    link_url=models.URLField(max_length=1000,blank=True,null=True)
    sns_url=models.URLField(max_length=1000,blank=True,null=True)


    def __str__(self):
            return str(self.title)

    def get_absolute_url(self):
        return f"/posts/{self.id}"


REPORT =(
    ("10","不審な内容またはスパムである"),
    ("20","不適切な画像または性的内容を含む画像動画を表示している"),
    ("30","不適切または攻撃的な内容を含んでいる"),
    ("40","自傷行為や自殺の意思をほのめかしている"),
    ("50","その他"),
)

class Report(models.Model):
    target = models.ForeignKey(Post,on_delete=models.CASCADE)
    report_us=models.CharField(max_length=20,choices=REPORT)
    message=models.TextField(max_length=1000,null=False, blank=True)

    def __str__(self):
        return self.message




class EventScheduleApex(models.Model):
    title=models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='event_apex', null=True, blank=True)
    start_date= models.DateField(blank=True,null=True)
    finish_date= models.DateField(blank=True,null=True)
    link_url = models.URLField(max_length=1000, blank=True, null=True)

class EventScheduleFortnite(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='event_fortnite', null=True, blank=True)
    start_date= models.DateField(blank=True,null=True)
    finish_date= models.DateField(blank=True,null=True)
    link_url = models.URLField(max_length=1000, blank=True, null=True)


class EventScheduleGuraburu(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='event_guraburu', null=True, blank=True)
    start_date= models.DateField(blank=True,null=True)
    finish_date= models.DateField(blank=True,null=True)
    link_url = models.URLField(max_length=1000, blank=True, null=True)

class EventScheduleMonhan(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='event_monhan', null=True, blank=True)
    start_date= models.DateField(blank=True,null=True)
    finish_date= models.DateField(blank=True,null=True)
    link_url = models.URLField(max_length=1000, blank=True, null=True)


class MonhanQuest(models.Model):
    title = models.CharField(max_length=100)
    master_username = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=200, blank=False, null=False)
    quest_name = models.CharField(max_length=100, blank=False, null=False)
    hunter_name = models.CharField(max_length=100, blank=False, null=False)
    room_id = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    add_time = models.DateTimeField(default=timezone.now)




    def __str__(self):
            return str(self.title)
