from django.db import models




EVENT=(
    ("10","キャリア"),
    ("20","スポーツ"),
    ("30","e-スポーツ"),
    ("40","コミニケーション"),

)
TYPE=(
    ("10", "オンライン"),
    ("20", "オフライン"),
)



class Post(models.Model):
    master_username = models.CharField(max_length=30, null=True, blank=True)
    event = models.CharField(max_length=20, choices=EVENT)
    event_type = models.CharField(max_length=20, choices=TYPE)

